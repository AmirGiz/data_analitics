# {"predict_data": ["i hate you, die please", "im so happy cause today i found my friends", "trump is my president", "i learn colors white, yellow, green"]}

from rest_framework.response import Response
from rest_framework.views import APIView
import json

import pandas as pd
import pickle


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

        result = {"logical_regression": log_reg_res, "naive_baes": naive_b_res.tolist()}

        return Response(json.dumps(result))
