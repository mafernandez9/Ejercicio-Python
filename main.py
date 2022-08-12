import json

def most_retweeted(info):
    return list[info.items[:10]]

def most_tweets(info):
    pairs = {}
    for key in info:
        if 

def main(option):
    with open('farmers-protest-tweets-2021-03-5.json') as file:
        if option == '1':
            data = json.load(file)
            data_sorted = sorted(data.items, key=lambda item: item[10])
            most_retweeted(data_sorted)
        else if option == '2':

