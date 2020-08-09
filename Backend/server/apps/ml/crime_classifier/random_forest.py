from django.conf import settings
import os
import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.ensemble import RandomForestClassifier # for training the algorithm
import joblib # for saving algorithm and preprocessing objects

class RandomForestClassifier:
    def __init__(self):
        path_to_artifacts = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/")
        self.encoders = joblib.load(path_to_artifacts + "encoders(RFC).joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest_model.joblib")

    def create_features(self, df):
        df['DAY_OF_YEAR'] = df['Date'].dt.dayofyear
        df['Day'] = df['Date'].dt.day
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['WEEK_OF_YEAR'] = df['Date'].dt.isocalendar().week
        df['Hour'] = pd.DataFrame(np.arange(0,24))

        X = df[['Day', 'Month', 'Year', 'DAY_OF_YEAR', 'WEEK_OF_YEAR']]
        
        return X

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        # input_data format: {'Date': '2019-10-13','Lat': '42.25951','Long': '-71.121563'}
        input_data = pd.DataFrame(input_data, index=[0])
        input_data['Date'] = pd.to_datetime(input_data['Date'])
        self.create_features(input_data)
        input_data = input_data.drop(['Date'], axis=1)
        input_data = pd.concat([input_data]*24, ignore_index=True)
        input_data['Hour'] = pd.DataFrame(np.arange(0,24))
        input_data = input_data[['Day', 'Month', 'Year', 'Hour', 'DAY_OF_YEAR', 'WEEK_OF_YEAR', 'Lat', 'Long']]

        return input_data

    def predict(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data, df):
        todays_forcast = []
        labels = ['Larceny', 'Burglary', 'Assault', 'Robbery']
        #unique_predictions = input_data.PREDICTED_OFFENSE_GROUP.unique()
        predictions = input_data.PREDICTED_OFFENSE_GROUP
        
        for i in predictions.index:
            todays_forcast.append(
                {
                    'Crime': predictions[i],
                    'Hour': df['Hour'][i]
                }
            )
        
        fc = pd.DataFrame(todays_forcast, columns=['Crime', 'Hour'])
        forcast_list = fc.to_json(orient='records')
        forcast_list = json.loads(forcast_list)

        return {"forcast": forcast_list, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)  # only one sample
            df = pd.DataFrame({'PREDICTED_OFFENSE_GROUP': prediction})
            prediction = self.postprocessing(df, input_data)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction