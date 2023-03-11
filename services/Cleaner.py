from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer 
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

        self.stemmer= WordNetLemmatizer()
        self.ignore_words=set(stopwords.words('english'))
        self.punctuations = set(string.punctuation)


    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence.lower())
        sentence_words=filter(lambda word : word not in self.ignore_words and word not in self.punctuations ,sentence_words )
        return self.lemmaning (sentence_words)

    def stemming (self, sentence):
        return [self.stemmer.stem(word) for word in sentence]

    def lemmaning (self, sentence):
        return [self.stemmer.lemmatize(word) for word in sentence]




