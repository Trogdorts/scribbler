import logging
from scribbler.scribbler import Scribbler
from scribbler.mylogmd import startlogging

def main():
    startlogging()
    logging.info("Beginning a new program execution.")
    novel = Scribbler(genre='science_fiction', fiction_type='novel', backfill=2, forwardfill=1)
    logging.info('Ending program execution.')

    novel.timeline.display_timeline()


if __name__ == "__main__":
    main()
