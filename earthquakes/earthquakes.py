import sys
import time
from datetime import datetime, timedelta

from acquisition import Acquisition
from preprocessing import Preprocessing
from store import Store


def main():
    try:
        interval = int(sys.argv[1])
        print "Interval parameter passed: ", interval
    except:
        interval = 10
        print "No interval parameter passed, interval default value ", interval
    end = datetime.utcnow() - timedelta(minutes=10)
    beginning = end - timedelta(minutes=interval)
    while True:
        print "Data acquisition starts"
        print "Requesting earthquakes data"
        print "from ", beginning
        print "to ", end
        eq_list_raw = Acquisition.request(end, beginning)
        eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
        eq_list = Preprocessing.splitDateTime(eq_list_temp)
        Store.toFile(eq_list)
        print "Data acquisition ended"
        print "Process starts again in {} minutes".format(interval)
        time.sleep(interval * 60)
        end = datetime.utcnow() - timedelta(minutes=10)
        beginning = end - timedelta(minutes=interval)


if __name__ == "__main__":
    main()
