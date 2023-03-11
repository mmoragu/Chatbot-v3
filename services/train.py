import json
import pickle
import random
import numpy as np
import tflearn
from tensorflow.python.framework import ops
from Cleaner import Cleaner


# cleaner = Cleaner.Cleaner()
with open('utils/content.json') as json_data:
    intents = json.load(json_data)

words = []
documents = []
classes = []
for intent in intents:
    for pattern in intent['patterns']:
        tokenized_patterns=Cleaner.get_cleaner().clean_up_sentence(pattern)
        words.extend(tokenized_patterns)
        documents.append((tokenized_patterns, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

classes = sorted(list(set(classes)))

training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

ops.reset_default_graph()
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='/utils/train_logs')
model.fit(train_x, train_y, n_epoch=20000, batch_size=500, show_metric=True)
model.save('utils/model.tflearn')

pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y},
            open('utils/trained_data', "wb"))







