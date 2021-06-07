# {"predict_data": ["i hate you, die please", "im so happy cause today i found my friends", "trump is my president", "i learn colors white, yellow, green"]}

from rest_framework.response import Response
from rest_framework.views import APIView
import json

import pandas as pd
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


class AnswerView(APIView):
    def post(self, request):
        predict_data = request.data["predict_data"]
        predict_df = pd.DataFrame(data=predict_data, columns=['tweet'])

        log_reg_pickle_in = open('models/nail_work.pickle', 'rb')
        log_reg_pickle_clf = pickle.load(log_reg_pickle_in)
        log_reg_res = log_reg_pickle_clf.predict(predict_df['tweet']).tolist()

        naive_b_pickle_in = open('models/naive_b.pickle', 'rb')
        naive_b_pickle_clf = pickle.load(naive_b_pickle_in)
        naive_b_res = naive_b_pickle_clf.predict(predict_df['tweet'])

        def predict(texts, the_tokenizer, the_model):
            seq = the_tokenizer.texts_to_sequences(texts)
            paded = pad_sequences(seq, maxlen=150)
            return the_model.predict(paded)

        loadedmodel = keras.models.load_model('models/model.nn')
        tokenizer_in = open('models/tokenizer.pickle', 'rb')
        tokenizer = pickle.load(tokenizer_in)
        loadedmodel_res = predict(predict_data, tokenizer, loadedmodel)

        result = {"logical_regression": log_reg_res, "naive_baes": naive_b_res.tolist(), "neuro_net": loadedmodel_res.tolist()}

        return Response(json.dumps(result))
