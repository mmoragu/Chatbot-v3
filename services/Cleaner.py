from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.corpus import stopwords
import string


class Cleaner(object):
    
    instance = None

    @classmethod
    def get_cleaner(cls):
        if cls.instance is None:
            cls.instance = Cleaner()
        return cls.instance

    def __init__(self):
        
        if self.instance is not None:
            raise ValueError()

        self.stemmer= PorterStemmer()
        self.ignore_words=set(stopwords.words('english'))
        self.punctuations = set(string.punctuation)


    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words=filter(lambda word : word not in self.ignore_words and word not in self.punctuations ,sentence_words )
        return self.stemming (sentence_words)

    def stemming (self, sentence):
        return [self.stemmer.stem(word.lower()) for word in sentence]




