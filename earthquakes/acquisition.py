import csv
import eventlet
import requests


class Acquisition:

    @classmethod
    def request(cls, start,end):
        eventlet.monkey_patch()
        with eventlet.Timeout(60):
            try:
                with requests.Session() as s:
                    download = s.get(
                        "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={}&endtime={}".format(
                            start, end))
                    decoded_content = download.content.decode('utf-8')
                    eq_csv = csv.reader(decoded_content.splitlines(), delimiter=',')
                    eq_list = list(eq_csv)
                    return eq_list
            except:
                print("Request error")
