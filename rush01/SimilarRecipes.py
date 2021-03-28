import pandas as pd


class SimilarRecipes:
    """
    Recommending similar recipes with additional information
    """
    def __init__(self, list_of_ingredients):
        """
        Put here any fields that you think you will need.
        """
        df = pd.read_csv('data/epi_r_cut.csv')
        self.ingredients = list_of_ingredients
        for ing in list_of_ingredients:
            df = df[df[ing] == 1]
        if df.shape[0] == 0:
            self.part = None
        else:
            self.part = df

    def find_all(self):
        """
The method returns a list of indexes of the recipes that contain the given list of ingredients. If there is no recipe that contains all the ingredients, handle it.
        """
        if self.part is None:
            return None
        return self.part.index
    
    def top_similar(self, n):
        """
The method returns a text formatted as in the example above with title, rating, and URL. Before that, it finds top-n most similar recipes by the number of additional ingredients that are required in the recipes using indexes from the find_all method. The most similar is the one that does not require any other ingredients. Next is the one that requires only one, etc. If it takes 5 more ingredients, do not return those recipes.
        """
        self.part['add'] = self.part.iloc[:, 6:].sum(axis=1) - len(self.ingredients)
        part = self.part
        part = part[part['add'] < 5]
        part = part.sort_values(by='rating', ascending=False).iloc[:n, :]
        urls = pd.read_csv('data/recipes.csv')
        text_with_recipes = ''
        for i in range(part.shape[0]):
            name = part.iloc[i].title  
            text_with_recipes += f"-{name.strip()}, rating: {part.iloc[i].rating}, URL: "
            if name in urls.title.values:
                text_with_recipes += str(urls[urls.title == name].recipies.values[0])
            text_with_recipes += '\n'
        return text_with_recipes[:-1]
