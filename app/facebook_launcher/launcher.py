import pandas as pd
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from os import listdir

file_path_friends = "app/facebook_launcher/data/facebook_data/messages/inbox/"
person_chat_count = {}
chat_title_dictionary = {}
total_counts = {}
participation_info = {}

def create_dictionary():
    files = [f for f in listdir(file_path_friends)]
    message_files = [file_path_friends + f + "/message.json" for f in files if f != ".DS_Store"]
    chat_titles = [f[:f.find("_")] for f in listdir(file_path_friends) if f != ".DS_Store"]
    total_count = 0
    for i in range(len(message_files)):
        json_file = open(message_files[i])
        json_str = json_file.read()
        json_data = json.loads(json_str)
        participants = json_data["participants"]
        person_chat_count[chat_titles[i]] = len(json_data["messages"])
        temp_dict = {}
        messages = json_data["messages"]
        for p in participants:
            name = p["name"]
            temp_dict[name] = 0
            if name in chat_title_dictionary.keys():
                chat_title_dictionary[name].append(chat_titles[i])
                total_counts[name] += len(json_data["messages"])
            else:
                chat_title_dictionary[name] = [chat_titles[i]]
                total_counts[name] = len(json_data["messages"])

        for m in messages:
            if "sender_name" in m.keys():
                sender = m["sender_name"]
                if sender not in chat_title_dictionary.keys():
                    chat_title_dictionary[sender] = [chat_titles[i]]
                    total_counts[sender] = len(json_data["messages"])
                elif chat_titles[i] not in chat_title_dictionary[sender]:
                    chat_title_dictionary[sender].append(chat_titles[i])
                    total_counts[sender] += len(json_data["messages"])
                if sender in temp_dict.keys():
                    temp_dict[sender] += 1
                else:
                    temp_dict[sender] = 1
        participation_info[chat_titles[i]] = temp_dict

def get_chats_and_messages(user):
    list_of_chats = chat_title_dictionary[user]
    ret_dic = {}
    for c in list_of_chats:
        ret_dic[c] = person_chat_count[c]
    return ret_dic

def get_message_count(user):
    return total_counts[user]

def get_chat_participation(user):
    list_of_chats = chat_title_dictionary[user]
    ret_dic = {}
    for c in list_of_chats:
        ret_dic[c] = participation_info[c][user]
    return ret_dic

def get_chat_count_dict():
    return person_chat_count
