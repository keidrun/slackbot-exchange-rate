from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import requests
import json

BASE_URL = "http://www.floatrates.com/"

JPY_URI = "daily/jpy.json"
USD_URI = "daily/usd.json"
CAD_URI = "daily/cad.json"


def getFloatRatesAPI(uri):
  floatrates_api_url = BASE_URL + uri
  res = requests.get(
      floatrates_api_url
  )
  return res


@respond_to('hi', re.IGNORECASE)
def hi(message):
  message.reply('Hi!')
  message.react('+1')


@respond_to('What is your name', re.IGNORECASE)
def name(message):
  message.reply("I'm 'mybot'")


@respond_to('rates', re.IGNORECASE)
def mention_func(message):
  message.reply("Today's exchange rates are ...")
  jpy_data = getFloatRatesAPI(JPY_URI).json()
  usd_data = getFloatRatesAPI(USD_URI).json()
  uca_data = getFloatRatesAPI(CAD_URI).json()

  message.reply('[USD/JPY] ' + str(jpy_data['usd']['rate']) + "\n"
                + '[CAD/JPY] ' + str(jpy_data['cad']['rate']) + "\n"
                + '[JPY/USD] ' + str(usd_data['jpy']['rate']) + "\n"
                + '[JPY/CAD] ' + str(uca_data['jpy']['rate'])
                )
