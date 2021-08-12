import logging
import pandas as pd

class Timeline:
    def __init__(self):
        logging.info("Initializing a new Timeline class instance.")
        self.timeline = pd.DataFrame(columns=['story', 's_block', 't_block'])
        logging.info(self.__dict__)

    def expand_timeline(self, story_num, wordcount):
        logging.info("Expanding timeline with story {}, {} words and {} blocks.".format(story_num, wordcount, int(wordcount / 100)))

        try:
            s_last_num = self.timeline.tail(1).index[0]
        except IndexError as e:
            s_last_num = 0
        try:
            t_last_num = self.timeline['t_block'].iloc[-1]
        except IndexError as e:
            t_last_num = 0

        for n in range(1, int(wordcount / 100)+1):
            s_block = int(n*100)
            t_last_num = t_last_num + 100
            entrydict = {'story': int(story_num), 's_block':s_block, 't_block':t_last_num}
            self.timeline = self.timeline.append(entrydict, ignore_index=True)

    def display_timeline(self):
        import matplotlib.pyplot as plot
        from matplotlib.pyplot import text
        bookends = self.timeline.groupby(['story'])['t_block'].min()

        for n in bookends:
            plot.axvline(n, linestyle="dashed", color="grey", linewidth=2, alpha=0.3)

        for i, x in enumerate(bookends):
            tmp = int(i+1)
            text(x, 0, "Book %d" % tmp, rotation=90, verticalalignment='center')

        plot.axhline(y=0, color='black', linestyle=':', alpha=0.3)
        plot.ylim(-10, 10)
        plot.xlim(0, self.timeline['t_block'].iloc[-1])
        plot.show()

if __name__ == "__main__":
    from mylogmd import startlogging
    import random
    startlogging()

    timeline = Timeline()

    stories = []
    for i in range(1, 12):
        stories.append(random.choice(range(1000,5000,1000)))
    story_num = 0
    for wordcount in stories:
        story_num += 1
        timeline.expand_timeline(story_num, wordcount)

    print("testing the expand timline function")
    timeline.expand_timeline(story_num=12, wordcount=2000)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(timeline.timeline)

    timeline.display_timeline()






