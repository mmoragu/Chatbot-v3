import json
import pickle
import random
from .Cleaner import Cleaner
import numpy as np
import tflearn


class ChatBot(object):

    instance = None

    @classmethod
    def getBot(cls):
        if cls.instance is None:
            cls.instance = ChatBot()
        return cls.instance

    def __init__(self):
        self.cleaner= Cleaner()

        if self.instance is not None:
            raise ValueError("Did you forgot to call getBot function ? ")

        data = pickle.load(open('utils/trained_data', "rb"))
        self.words = data['words']
        self.classes = data['classes']
        train_x = data['train_x']
        train_y = data['train_y']
        with open('utils\content.json') as json_data:
            self.intents = json.load(json_data)
        net = tflearn.input_data(shape=[None, len(train_x[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net, tensorboard_dir='utils/train_logs')
        self.model.load('utils/model.tflearn')

    def bow(self, sentence, words, show_details=False):
        sentence_words = self.cleaner.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)
        return np.array(bag)

    def classify(self, sentence):
        ERROR_THRESHOLD = 0.05
        results = self.model.predict([self.bow(sentence, self.words)])[0]
        results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((self.classes[r[0]], r[1]))
        return return_list

    def response(self, sentence, userID='111', show_details=False):
        results = self.classify(sentence)
        context = {}
        if results:
            while results:
                for i in self.intents:
                    if i['tag'] == results[0][0]:
                        if 'context_set' in i:
                            if show_details: print('context:', i['context_set'])
                            context[userID] = i['context_set']
                        if not 'context_filter' in i or \
                                (userID in context and 'context_filter' in i and i['context_filter'] ==
                                 context[
                                     userID]):
                            if show_details: print('tag:', i['tag'])
                            return random.choice(i['responses'])
                return "I can't guess"
        else:
            return "I cannot answer"

# def clean_up_sentence(self, sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]
#     return sentence_words
