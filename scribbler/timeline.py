import logging
import pandas as pd

class Timeline:
    def __init__(self):
        logging.info("Initializing a new Timeline class instance.")
        self.timeline = pd.DataFrame(columns=['story', 'block'])
        logging.info(self.__dict__)

    def expand_timeline(self, story_num, wordcount):
        logging.info("Expanding timeline with story {}, {} words and {} blocks.".format(story_num, wordcount, int(wordcount / 100)))
        try:
            last_num = self.timeline.tail(1).index[0]
        except IndexError as e:
            last_num = 0
        data = []
        for n in range(1, int(wordcount / 100)+1):
            entrydict = {'story': story_num, 'block':n*100}
            self.timeline = self.timeline.append(entrydict, ignore_index=True)






if __name__ == "__main__":
    from mylogmd import startlogging
    import random
    startlogging()

    timeline = Timeline()

    stories = []
    for i in range(1, 12):
        stories.append(random.choice(range(1000,12500,1000)))
    story_num = 0
    for wordcount in stories:
        story_num += 1
        timeline.expand_timeline(story_num, wordcount)

    print("testing the expand timline function")
    timeline.expand_timeline(story_num=12, wordcount=2000)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(timeline.timeline)

    import matplotlib.pyplot as plot
    timeline.timeline.plot.line()
    plot.show()








