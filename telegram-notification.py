#! python3

import requests
import json
from pprint import pprint
import datetime, time
import sys

class TelegramNotification:
    def __init__(self):
        self.API_URL = 'https://api.telegram.org/bot'
        with open('/home/andy/.telegram-bot/.telegram-api-token', 'r') as f:
            self.API_ID = f.read().strip('\n')
    
    def send_message(self, chat_id='969768646', torrent_name='Torrent name'):
        """
        Send me a telegram message when the Torrent file has been downloaded.
        """
        url = self.API_URL + self.API_ID + '/sendMessage'
        current_time = datetime.datetime.fromtimestamp(time.time())
        msg = '"<b>' + torrent_name + '</b>" downloaded at ' +  current_time.strftime("%H:%M.")
        params = {'chat_id': chat_id, 'text': msg, 'parse_mode': 'html'}
        response = requests.post(url, data=params)
        if response.status_code == 200:
            json_response = json.loads(response.text)
            pprint(json_response)            
        else:
            print(f'Failed sending the message.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        bot = TelegramNotification()
        bot.send_message(torrent_name=' '.join(sys.argv[1:]))