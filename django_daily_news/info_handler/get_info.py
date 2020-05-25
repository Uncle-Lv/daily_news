from urllib import request
import json
import time


def get_news():
    url = 'http://api.tianapi.com/bulletin/index?key=27d9ea9bfc47704230d5899cc697b09d'

    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    info = json.loads(content)
    news_list = info['newslist']
    return news_list


def get_almanac():
    date = get_date()
    url = 'http://api.tianapi.com/txapi/lunar/index?key=27d9ea9bfc47704230d5899cc697b09d&date=' + date
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    info = json.loads(content)
    news_list = info['newslist']
    return news_list


def get_date():
    year = time.strftime('%Y', time.localtime())
    month = time.strftime('%m', time.localtime())
    month = remove_prefix_zero(month, 13)
    day = time.strftime('%d', time.localtime())
    date = year + '-' + month + '-' + day
    return date

def remove_prefix_zero(operate_num, num):
    result = int(operate_num) % num
    return str(result)


get_almanac()