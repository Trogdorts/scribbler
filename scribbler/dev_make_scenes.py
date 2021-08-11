from copy import copy
import random

wordcount = 110000

average_scene_length = 3000

def get_number_of_scenes(wordcount, average_scene_length):
    num_scenes = round(wordcount / average_scene_length)
    if not num_scenes % 2 == 0:
        num_scenes +=1
    return num_scenes

def define_scenes(wordcount, num_scenes, average_scene_length):
    # each entry should have a scene number, a word count start number, and end number
    # Brute Force!
    # loop through building scenes until getting a proper fit
    loop = 0

    while True:
        loop += 1
        scenes = {}
        wordsleft = copy(wordcount)
        high = average_scene_length + (average_scene_length * .5)
        low = average_scene_length - (average_scene_length * .5)
        for n in range(1, num_scenes + 1):
            rand_lenght = random.randint(low, high)
            rand_lenght = round(rand_lenght, -2)
            wordsleft = wordsleft - rand_lenght
            data = {"length": rand_lenght,
                    "start": wordcount-(wordsleft+rand_lenght),
                    "stop": wordcount-(wordsleft+rand_lenght) + ( rand_lenght - 1 )
                    }
            scenes[n] = data
        if wordsleft == 0:
            print("Loops:", loop)
            break
    return scenes



num_scenes = get_number_of_scenes(wordcount, average_scene_length)
scenes_dict = define_scenes(wordcount, num_scenes, average_scene_length)

import pprint
pprint.pprint(scenes_dict)

print("Number of scenes:", num_scenes)

cnt = int(wordcount / 100)
print("wordcount divided by 100", cnt, wordcount)
for i in range(1, cnt + 1):
    s_list = []
    new_num = last_num += 100
    s_list.append(new_num)
    print("Entry", last_num)

cnt = int(wordcount / 100)
for i in range(1, cnt + 1):
    new_num = last_num + 1
    self.timeline.loc[new_num] = [i * 100, story_num]

# print("Story Number {}, Last item in timeline {}".format(story_num, last_num) )

import pprint

pprint.pprint(self.timeline)
