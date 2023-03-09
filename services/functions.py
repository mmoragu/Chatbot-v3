# from nltk.stem.lancaster import LancasterStemmer
# from nltk.stem.porter import PorterStemmer
# import nltk
# from nltk.corpus import stopwords
# import string

# # stemmer = LancasterStemmer()
# stemmer = PorterStemmer()
# ignore_words=set(stopwords.words('english'))
# punctuations = set(string.punctuation)

# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words=filter(lambda word : word not in ignore_words and word not in punctuations ,sentence_words )
#     return stemming (sentence_words)

# def stemming (sentence):
#     return [stemmer.stem(word.lower()) for word in sentence]