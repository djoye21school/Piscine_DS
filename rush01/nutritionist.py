#!/usr/bin/env python3
import numpy as np
from sys import argv, exit
from forecast import Forecast
from SimilarRecipes import SimilarRecipes
from NutritionFacts import NutritionFacts


def main():
    if len(argv) < 2:
        return
    try:
        ingredients = argv[1:]
        alt_names = {'cream': 'milk', 
                 'yam': 'sweet potato',
                 'scallion': 'green onion',
                 'armagnac': 'cognac',
                 'stew': 'soup',
                 'butterscotch': 'caramel',
                 'jelly': 'jam'}
        ingredients, indeces = np.unique(np.array([alt_names.get(n, n) for n in ingredients]),
                                     return_index=True)
        ingredients = ingredients[indeces.argsort()]
        names = np.loadtxt('data/names.csv', dtype='object', delimiter=',')
        for ing in ingredients:
            if ing not in names:
                print(f"""Ingredient '{ing}' not found in base.
Sorry forecast cannot be done, please try again""")
                exit()
        print('I. OUR FORECAST')
        fcst = Forecast(ingredients)
        print(fcst.predict_rating_category()[1])
        print('\n')
        print('II. NUTRITION FACTS')
        nf = NutritionFacts(ingredients)
        nf.retrieve()
        print(nf.filter(['Protein', 'Total Carbohydrate', 'Total Fat'], 30))
        print('\n')
        print('III. TOP-3 SIMILAR RECIPES')
        sr = SimilarRecipes(ingredients)
        print(sr.top_similar(3))
    except Exception:
        print('An error occured while executing, please reinstall the app')


if __name__ == '__main__':
    main()


