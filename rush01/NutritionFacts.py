import pandas as pd


class NutritionFacts:
    """
    Offering nutritional facts on given ingredients.
    """
    def __init__(self, list_of_ingredients):
        """
        Put here any fields that you think you will need.
        """
        self.ingredients = list_of_ingredients

    def retrieve(self):
        """
The method gets all the nutrient facts about the given ingredients from the file with pre-collected information. It returns any structure that you find useful.
        """
        nutrients = pd.read_csv('data/nutrients_norm.csv', index_col=[0])
        self.facts = nutrients.loc[self.ingredients]
        return self.facts

    def filter(self, must_nutrients, n):
        """
The method selects from the nutrient facts only nutrients from the list of must_nutrients and the top-n nutrients with the highest values of daily value norms for the given ingredient. It returns a text formatted as in the example above.
        """
        text_with_facts = ''
        for ing in self.ingredients:
            text_with_facts += ing.title() + '\n'
            for nutr in must_nutrients:
                text_with_facts += f"{nutr} - {int(self.facts.loc[ing, nutr] * 100)}% of Daily Value\n"
            rest_facts = self.facts.drop(must_nutrients, axis=1).loc[ing].sort_values(ascending=False)
            for nutr in rest_facts.index[:n]:
                value = int(self.facts.loc[ing, nutr] * 100)
                if value == 0:
                    break
                text_with_facts += f"{nutr} - {value}% of Daily Value\n"
            text_with_facts += '\n'
        return text_with_facts[:-1]
