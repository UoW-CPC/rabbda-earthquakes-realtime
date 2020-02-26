import time
from datetime import datetime,timedelta

from acquisition import Acquisition
from preprocessing import Preprocessing

def main():
    period = 1
    now = datetime.utcnow()
    start = now - timedelta(minutes=period)
    while True:
        print now
        print start
        eq_list_raw = Acquisition.request(period, now, start)
        eq_list_temp = Preprocessing.clean(eq_list_raw)
        eq_list = Preprocessing.splitDateTime(eq_list_temp)
        for eq in eq_list:
            print(eq)
        time.sleep(period*60)
        now = datetime.utcnow()
        start = now - timedelta(minutes=period)


if __name__ == "__main__":
    main()

