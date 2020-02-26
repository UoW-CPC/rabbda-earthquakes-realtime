import sys
import time
from datetime import datetime, timedelta

from acquisition import Acquisition
from preprocessing import Preprocessing
from store import Store


def main():
    try:
        period = int(sys.argv[1])
        print "Period parameter passed: ",period
    except:
        period = 10
        print "No period parameter passed, period default value ",period
    end = datetime.utcnow() - timedelta(minutes=10)
    beginning = end - timedelta(minutes=period)
    while True:
        print end
        print beginning
        eq_list_raw = Acquisition.request(end, beginning)
        eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
        eq_list = Preprocessing.splitDateTime(eq_list_temp)
        Store.toFile(eq_list)
        time.sleep(period * 60)
        end = datetime.utcnow()  - timedelta(minutes=10)
        beginning = end - timedelta(minutes=period)


if __name__ == "__main__":
    main()
