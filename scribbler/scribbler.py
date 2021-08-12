from .timeline import Timeline
import logging
import random
from copy import copy

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
        if kwargs is not None and 'backfill' in kwargs:
            self.backfill = kwargs.get('backfill')
        else:
            self.backfill = 5
        if kwargs is not None and 'forwardfill' in kwargs:
            self.forwardfill = kwargs.get('forwardfill')
        else:
            self.forwardfill = 5

        self.timeline = Timeline()
        self.workingstory = self.backfill+1
        self.backfill_forwardfill(self.wordcount, self.backfill, self.forwardfill)
        self.num_scenes = self.get_number_of_scenes(self.wordcount, self.avg_scene_length)
        self.scenes_dict = self.define_scenes(self.wordcount, self.num_scenes, self.avg_scene_length)

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
    
    def backfill_forwardfill(self, wordcount, backfill, forwardfill):
        # Create stories to backfill and forwardfill the timeline
        series = []
        for num in range(1, (backfill + 1)):
            wordcnt = self.get_wordcount()
            series.append(wordcnt)
        series.append(wordcount)
        for num in range(1, (forwardfill + 1)):
            wordcnt = self.get_wordcount()
            series.append(wordcnt)

        # Expand the timeline with the backfill books and the forward fill books
        # this is the building block for all the plot lines layered throughout a
        # series or even just a single book. the farther back you backfill, the more
        # intricate and layered the plots will be.
        story_num = 0
        for wordcount in series:
            story_num+=1
            self.timeline.expand_timeline(story_num, wordcount)

    def get_number_of_scenes(self, wordcount, avg_scene_length):
        num_scenes = round(wordcount / avg_scene_length)
        if not num_scenes % 2 == 0:
            num_scenes += 1
        logging.info("Split {} words into {} scenes.".format(wordcount, num_scenes))
        return num_scenes

    def define_scenes(self, wordcount, num_scenes, avg_scene_length):
        # each entry should have a scene number, a word count start number, and end number
        # Brute Force!
        # loop through building scenes until getting a proper fit
        loop = 0
        while True:
            loop += 1
            scenes = {}
            wordsleft = copy(wordcount)
            high = avg_scene_length + (avg_scene_length * .5)
            low = avg_scene_length - (avg_scene_length * .5)
            for n in range(1, num_scenes + 1):
                rand_lenght = random.randint(low, high)
                rand_lenght = round(rand_lenght, -2)
                wordsleft = wordsleft - rand_lenght
                data = {"length": rand_lenght,
                        "start": wordcount - (wordsleft + rand_lenght),
                        "stop": wordcount - (wordsleft + rand_lenght) + (rand_lenght - 1)
                        }
                scenes[n] = data
            if wordsleft == 0:
                logging.info("Looped {} times to create {} randomly sized scenes.".format(str(loop), num_scenes))
                break
        return scenes





