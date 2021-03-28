import numpy as np
import pickle
from sys import exit


class Forecast:
    """
    Predicting the rating or the class
    """
    def __init__(self, list_of_ingredients):
        """
        Put here any fields that you think you will need.
        """
        self.names = np.loadtxt('data/names.csv', dtype='object', delimiter=',')
        self.ingredients = list_of_ingredients
        self.clf = pickle.load(open('data/finalized_clf.sav', 'rb'))
        self.reg = pickle.load(open('data/finalized_regression.sav', 'rb'))
        self.X = self.preprocess()

    def get_reg_text(self):
        if self.reg_rating < 2:
            return "You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"
        elif self.reg_rating < 4:
            return "You might find it tasty and in our opinion, it is so-so idea to have a dish with that list of ingredients"
        else:
            return "You might find it tasty and in our opinion, it is a great idea to have a dish with that list of ingredients!"

    def get_clf_text(self):
        if self.clf_rating == 'bad':
            return "You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"
        elif self.clf_rating == 'so-so':
            return "You might find it tasty and in our opinion, it is so-so idea to have a dish with that list of ingredients"
        else:
            return "You might find it tasty and in our opinion, it is a great idea to have a dish with that list of ingredients!"
    
    def preprocess(self):
        """
The method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
        vector = np.zeros(self.names.shape)
        for ing in self.ingredients:
            vector[self.names == ing] = 1.
        return vector.reshape(1, -1)
        
    def predict_rating(self):
        """
The method returns the rating for the list of ingredients using the regression model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.
        """
        rating = self.reg.predict(self.X)
        self.reg_rating = rating
        text = self.get_reg_text()
        self.reg_text = text
        return rating, text
        
    def predict_rating_category(self):
        """
The method returns the rating category for the list of ingredients using the classification model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.
        """
        rating = self.clf.predict(self.X)
        self.clf_rating = rating
        text = self.get_clf_text()
        self.clf_text = text
        return rating, text
