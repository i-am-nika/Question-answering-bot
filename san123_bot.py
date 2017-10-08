#!/bin/env python3

""" 
SUMMARY:

The San123 is a question-answering system that implements 
Levenshtein Distance to calculates differences between sequences
and can answer about 30.000 questions from WikiQA Dataset. 

Examples of questions:
"how are glacier caves formed?"
"How are the directions of the velocity and force vectors related in a circular motion"
"how a beretta model 21 pistols magazines works"
"how much is 1 tablespoon of water"
"how a rocket engine works"
"how bruce lee died"
"how old were golden girls at time of show"

* Microsoft Research WikiQA Corpus
@InProceedings{YangYihMeek:EMNLP2015:WikiQA,
  author    = {Yang, Yi  and  Yih, Wen-tau  and  Meek, Christopher},
  title     = {{WikiQA}: {A} Challenge Dataset for Open-Domain Question Answering},
  booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  month     = {September},
  year      = {2015},
  address   = {Lisbon, Portugal},
  publisher = {Association for Computational Linguistics}
}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
BEFORE YOU START:

- Install python-leventshtein

- Download WikiQA Corpus (http://research.microsoft.com/en-US/downloads/4495da01-db8c-4041-a7f6-7984a4f6a905/default.aspx). 
Save the WikiQA.tsv file from this Corpus in a separate folder. 
Write the whole name of this folder instead of <YOUR FOLDER> for "path_dic" in the following code.

- Write the HTTP API of your bot instead of <YOUR BOT TOKEN> for "token" in the following code.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Please cite it if you use this code:

#__author__ = "Tetyana Chernenko"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "tatjana.chernenko@gmail.com"
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

VERSION 1.0.0: October 8, 2017

"""

#san123_bot.py
#usage:
#$ ./san123_bot.py
 #__author__ = "Tetyana Chernenko"
#__copyright__ = "Copyright (c) 2017 Tetyana Chernenko. All rights reserved."
#__credits__ = ["Tetyana Chernenko"]
#__license__ = "GNU General Public License v3.0"
#__version__ = "1.0.0"
#__maintrainer__ = "Tetyana Chernenko"
#__email__ = "tatjana.chernenko@gmail.com"
#__status__ = "Development"


import os
import requests
import datetime
import fuzzywuzzy
from fuzzywuzzy import process
 
token = "<YOUR BOT TOKEN>"    # your Telegram bot HTTP API

path_dic = "<YOUR FOLDER>"    # your folder with WikiQA.tsv file from the WikiQA Corpus

class BotHandler:
 
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
 
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
 
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
 
    def get_last_update(self):
        get_result = self.get_updates()
 
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result          
        return last_update

def read_dictionary(our_file):
    with open(path_dic + our_file, "r") as fi:
        data = fi.readlines()
    return data 

greet_bot = BotHandler(token)  

now = datetime.datetime.now()

def write_chats(filename, information, today):
    new = open(filename, "a")
    new.write(today+"\n")
    new.write(str(information) + "\n") 

rate = 77

def main():  
    new_offset = None
    hour = now.hour
    dicti = []  
    resp = read_dictionary("WikiQA.tsv")
    dicti.append(resp)

    while True:
        greet_bot.get_updates(new_offset)
 
        last_update = greet_bot.get_last_update()
        print("LAST UPDATE: ", type(last_update), "\n", last_update)

        if type(last_update) != list:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            print(last_chat_text, len(last_chat_text), type(last_chat_text))
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']
            try:
                first_chat_name = last_update['message']['chat']['last_name']
            except:
                first_chat_name = "none"
            
            counter = 0
            greet_bot.send_message(last_chat_id, 'I start searching, {}.\n'.format(last_chat_name))
            n = 0
            for el in dicti[0]:
                phrase = el.split("\t")
                leven = fuzzywuzzy.fuzz.partial_ratio(last_chat_text.lower(), phrase[1])
               
                if leven >= rate and leven>counter:
                    print("Understand")
                    counter = leven
                    possible_match = phrase[1]
                    print("L ", leven)
                    print("P ", possible_match)

                    if phrase[1] == possible_match:
                        if phrase[6] == "1\n":
                            print("yesss")
                            greet_bot.send_message(last_chat_id, 'Match {first}%, {last}.\n\n'.format(first=leven, last = last_chat_name) + phrase[5]+"\n\nI continue searching...")
                            n+=1
                            print("dodod")
                        else:
                            greet_bot.send_message(last_chat_id, 'Match {first}%, {last}.\n\n'.format(first=leven, last = last_chat_name) + phrase[5]+"\n\nThis answer can be incomplete. I continue searching...")
                            n+=1
                    else:
                        pass
                      
                if leven < rate:
                    phrase = el.split("\t")
                    leven = fuzzywuzzy.fuzz.partial_ratio(last_chat_text.lower(), phrase[3])
                    if leven > rate: 
                        if phrase[6] == "1\n":
                            print("Count ", leven)
                            greet_bot.send_message(last_chat_id, 'Match {first}% with {second}, {last}:\n\n'.format(first=leven, second = phrase[3], last = last_chat_name)+phrase[5]+"\n\nI continue searching...")
                            n+=1
                        else:
                            greet_bot.send_message(last_chat_id, 'Match {first}% with {second}, {last}:\n\n'.format(first=leven, second = phrase[3], last = last_chat_name)+phrase[5]+"\n\nThis answer can be incomplete. I continue searching...")
                            n+=1
                    else:
                        pass 

            if n == 0:
                greet_bot.send_message(last_chat_id, 'I don\'t know the answer, {}.'.format(last_chat_name))
            else:
                greet_bot.send_message(last_chat_id, 'That\'s all I know now, {}.'.format(last_chat_name))
                
            write_chats(last_chat_name+"_"+first_chat_name, last_update, str(datetime.datetime.now())) 
            new_offset = last_update_id + 1

        else:
             print("No updates")

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
