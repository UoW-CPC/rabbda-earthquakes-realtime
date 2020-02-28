import sys
import time
from datetime import datetime, timedelta

from acquisition import Acquisition
from preprocessing import Preprocessing
from storeData import StoreData


def main():
    StoreData.createFolder()
    try:
        interval = int(sys.argv[1])
        print "Interval parameter passed: ", interval
    except:
        interval = 10
        print "No interval parameter passed, interval default value ", interval
    end = datetime.utcnow() - timedelta(minutes=10)
    start = end - timedelta(minutes=interval)
    while True:
        print "Data acquisition starts"
        print "Requesting earthquakes data"
        print "from ", start
        print "to   ", end
        eq_list_raw = Acquisition.request(start, end)
        eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
        eq_list = Preprocessing.splitDateTime(eq_list_temp)
        StoreData.toFile(eq_list)
        print "Data acquisition ended"
        print "Process starts again in {} minutes".format(interval)
        time.sleep(interval * 60)
        end = datetime.utcnow() - timedelta(minutes=10)
        start = end - timedelta(minutes=interval)


if __name__ == "__main__":
    main()
