# {"predict_data": ["i hate you, die please", "im so happy cause today i found my friends", "trump is my president", "i learn colors white, yellow, green"]}

from rest_framework.response import Response
from rest_framework.views import APIView
import json

import pickle
import pandas
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')


class AnswerView(APIView):
    def post(self, request):
        predict_data = request.data["predict_data"]
        predict_df = pandas.DataFrame(data=predict_data, columns=['tweet'])

        snowball = SnowballStemmer(language="english")
        stop_words = stopwords.words("english")

        def tokenize_sentence(sentence: str):
            sanitized_sentence = sentence.replace("'", "").replace('"', "")
            tokens = word_tokenize(sanitized_sentence, language="english")
            tokens = [i for i in tokens if i not in string.punctuation]
            tokens = [i for i in tokens if i not in stop_words]
            tokens = [snowball.stem(i) for i in tokens]
            return tokens

        # log_reg_pickle_in = open('models/nail_work.pickle', 'rb')
        # log_reg_pickle_clf = pickle.load(log_reg_pickle_in)
        # log_reg_res = log_reg_pickle_clf.predict(predict_df['tweet']).tolist()

        naive_b_pickle_in = open('models/naive_b.pickle', 'rb')
        naive_b_pickle_clf = pickle.load(naive_b_pickle_in)
        naive_b_res = naive_b_pickle_clf.predict(predict_df['tweet']).tolist()

        result = {"logical_regression": naive_b_res, "naive_baes": naive_b_res}

        return Response(json.dumps(result))
