from cloudant.client import Cloudant
import tweepy
from tweepy import Stream
import json as js
import argparse
from datetime import datetime
import time
import json

USERNAME = 'user'
PASSWORD = 'pass'
URL = 'http://172.26.132.223:5984'
client = Cloudant(USERNAME, PASSWORD, url=URL, connect=True, auto_renew=True)
print(client.all_dbs())
db = client.create_database('db_brisbane', partitioned=False)

def account_info():

    account = {
        "accounts": {
            "xwqian2":{
                "Consumer_Key" : "Up5cFxl1QjkHvqiDf7aehROw8",
                "Consumer_Secret" : "eyEbW9Rit5ANOt5bdSiOfBp124GqaJvtNxn0MObMSd4uPAKij8",
                "Access_Token" : "2527414171-8eUKlK9Z8k4FAIDRvPJ35JtLedXxjloAA9Xqf2h",
                "Access_Token_Secret" : "94Do2on02xCemCwpfg9PyCikFswDsAcufuYQTisJTrtWh"
                },
            "christina": {
                "Consumer_Key": "5KHYDpEavEvWs6f07gqA7FSYU",
                "Consumer_Secret": "15T8ePaIu7IfU0X7VnhPHAsgSjvIqpsYTpDEKjI596w6mUoTLe",
                "Access_Token": "1517696674243948545-ozARJ8xRdGarhfknxGHqvMs51uPXp3",
                "Access_Token_Secret": "rN3JxUTER0PjMXqsy4WSgzqGk10IF29IBG7JXSotRUAxG",
                "bearer_token":"AAAAAAAAAAAAAAAAAAAAAEo9bwEAAAAA40DLUb109523Heu6ePJD3vtThCc%3DjIH9qTJi0qCyhH9V98DtTQLLMmoV9V2mSRr4W5f9tF8m8Iee8y"
            },
            "christina2": {
                "Consumer_Key": "NiN2E5xgpBPCVkfYywHqc14ZE",
                "Consumer_Secret": "g1mlvEAI9JlVvzgDFjlilGewtbrfsd3W6IyYtG9fqghOIm6nwn",
                "Access_Token": "1517696674243948545-wBmsqL0LgXlHyxgCnBIgjWH305hGLe",
                "Access_Token_Secret": "mM9CbWlNbH9be0cMOlGDLV2sc2CLvWcD2Nyt4FDh5Glk9",
                "bearer_token":"AAAAAAAAAAAAAAAAAAAAALOtbwEAAAAAS6GIbpYYMDLRdsVcFeEPqkfDizc%3DjwkHEy4hesjdPiXRMKLmYAlrF7GkLfL27mD9UOcLe6LI6C2nTz"
            },
            "christina3": {
                "Consumer_Key": "XwIG0yNQExqRoON18fpY8cW98",
                "Consumer_Secret": "dZWwg1daAHLezqbFIJ8dnWZDS34s8dv0erI8MKYPDmrjTlMh1c",
                "Access_Token": "1517696674243948545-xLPlqXaBKOsQQXkBVkFZQ4EUSrHKja",
                "Access_Token_Secret": "83MIicJjO1hYxvpKaHUjIve0cihjTCodmZ7YHYJjqvBsm",
                "bearer_token":"AAAAAAAAAAAAAAAAAAAAANmtbwEAAAAAdxNdCIq24x2lcpJoS0TWjCxv2Ck%3Dh3lQ1EueBEQnMenBgk8ZeOZ3sXQXJ9ciayy4VnbZNL3Rq78uc4"
            },
            "wendy": {
                "Consumer_Key": "mPbAIQI6GiUKsR89tBZ1dOVte",
                "Consumer_Secret": "0Vsm4cXRuLutFREUj0elbpF92PyyIb29TSR1BdwGXivLUftVD9",
                "Access_Token": "1510827213339623431-U1mlt70yY2bAd9v7WHlYGpTg3RCUJK",
                "Access_Token_Secret": "gftHoztKdJ5em60kms3aqqRIsswcAGLRZDPYGbf6ESf1X",
                "bearer_token":"AAAAAAAAAAAAAAAAAAAAAJZqbAEAAAAAiiSxVh7G3TjQIB0UajmQrZJWPIE%3DibLwxyjeQOyLRYps5puQq4jtgPDkrz9tM9uDUAtx3pwurWerON"
            }
        },
        "db": {
            "user": "user",
            "password": "pass",
            "url": "http://172.26.132.223:5984"
        }
    }
    return account


class IDPrinter(tweepy.Stream):
    def on_data(self, data):
        tweetJson = js.loads(data, encoding= 'utf-8')
# need to filter out the retweet
        if not tweetJson["text"].startswith('RT') and tweetJson["retweeted"] == False:
            if ((tweetJson["id_str"] not in db)):
                tweetJson["_id"] = tweetJson["id_str"]
                db.create_document(tweetJson)
                print("get")
            # print(newJSON)
    
    def on_status(self, status):
        print(status.id)
        print(status.place)

if __name__ == '__main__':
    account = account_info()
    Consumer_Key = account["accounts"]["wendy"]["Consumer_Key"]
    Consumer_Secret = account["accounts"]["wendy"]["Consumer_Secret"]
    Access_Token = account["accounts"]["wendy"]["Access_Token"]
    Access_Token_Secret = account["accounts"]["wendy"]["Access_Token_Secret"]
    stream = tweepy.Stream(
    Consumer_Key, Consumer_Secret,
    Access_Token, Access_Token_Secret
)
    printer = IDPrinter(
    Consumer_Key, Consumer_Secret,
    Access_Token, Access_Token_Secret
    )
    printer.filter(locations = [152.0734,-28.3640,153.5467,-26.4523])
    
    