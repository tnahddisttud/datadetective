from django.test import TestCase

from apps.ml.crime_classifier.random_forest import RandomForestClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "Date": "2019-10-13",
            "Lat": "42.25951",
            "Long": "-71.121563"
        }

        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual("OK", response["status"])
        self.assertTrue("forcast" in response)
        self.assertEqual([["Larceny", 0], ["Larceny", 1], ["Larceny", 2], ["Assault", 3], ["Assault", 4], ["Assault", 5], ["Assault", 6], ["Assault", 7], ["Assault", 
8], ["Assault", 9], ["Assault", 10], ["Larceny", 11], ["Assault", 12], ["Larceny", 13], ["Larceny", 14], ["Larceny", 15], ["Larceny", 16], ["Larceny", 17], ["Assault", 18], ["Larceny", 19], ["Larceny", 20], ["Larceny", 21], ["Larceny", 22], ["Larceny", 23]], response["forcast"])