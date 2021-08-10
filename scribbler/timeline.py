import logging
import pandas as pd

class Timeline:
    def __init__(self):
        logging.info("Initializing a new Timeline class instance.")
        self.timeline = pd.DataFrame(index=pd.Series(range(10000,20000)))
        logging.debug("Timeline pandas dataframe created: {}, {}".format(type(self.timeline), self.timeline))
        logging.info(self.__dict__)
