from .timeline import Timeline
import logging
import random

#TODO Load config from file

#TODO Pick a genre

# Wordcounts for each type of story broken out by different genres
wordcounts = {
    'general': {
            'micro' :     {'low': 100,      'high':100,     "avg_scene_length":100},
            'flash' :     {'low': 100,      'high':1000,    "avg_scene_length":1000},
            'short' :     {'low': 1000,     'high':7500,    "avg_scene_length":1500},
            'novelette' : {'low': 7500,     'high':20000,   "avg_scene_length":2000},
            'novella' :   {'low': 20000,    'high':50000,   "avg_scene_length":2500},
            'novel' :     {'low': 50000,    'high':125000,  "avg_scene_length":3000},
            'epic' :      {'low': 125000,   'high':200000,  "avg_scene_length":3500}
            },
    'science_fiction': {
            'micro' :     {'low': 100,      'high':100,     "avg_scene_length":100},
            'flash' :     {'low': 100,      'high':1000,    "avg_scene_length":1000},
            'short' :     {'low': 1000,     'high':7500,    "avg_scene_length":1500},
            'novelette' : {'low': 7500,     'high':20000,   "avg_scene_length":2000},
            'novella' :   {'low': 20000,    'high':90000,   "avg_scene_length":2500},
            'novel' :     {'low': 90000,    'high':125000,  "avg_scene_length":3000},
            'epic' :      {'low': 125000,   'high':200000,  "avg_scene_length":3500}
            },
}




class Scribbler:


    def __init__(self, **kwargs):
        logging.info("Initializing a new Scribbler class instance.")
        if kwargs is not None and 'genre' in kwargs:
            self.genre = kwargs.get('genre')
        else:
            self.genre = 'general'
        if kwargs is not None and 'fiction_type' in kwargs:
            self.fiction_type = kwargs.get('fiction_type')
        else:
            self.fiction_type = 'novel'
        if kwargs is not None and 'avg_scene_length' in kwargs:
            self.fiction_type = kwargs.get('avg_scene_length')
        else:
            self.avg_scene_length = wordcounts[self.genre][self.fiction_type]['avg_scene_length']

        if kwargs is not None and 'wordcount' in kwargs:
            self.wordcount = kwargs.get('wordcount')
        else:
            self.wordcount = self.get_wordcount()





        self.timeline = Timeline()
        logging.info(self.__dict__)




    def get_wordcount(self):
        low = wordcounts[self.genre][self.fiction_type]['low']
        high = wordcounts[self.genre][self.fiction_type]['high']
        rand_lenght = random.randint(low, high)
        if rand_lenght > 80000:
            rounded_length = round(rand_lenght, -4)
        elif rand_lenght > 50000:
            rounded_length = round(rand_lenght, -3)
        elif rand_lenght > 7500:
            rounded_length = round(rand_lenght, -2)
        elif rand_lenght > 100:
            rounded_length = round(rand_lenght, -1)
        elif rand_lenght == 100:
            rounded_length = rand_lenght
        return rounded_length




