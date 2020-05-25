from django.shortcuts import render
from ..info_handler import get_info
from ..models.news import News
from  ..models.lunar_date import LunarDate


def index(request):
    content_list = get_info.get_news();

    news_list = []

    for item in content_list:
        title = item['title']
        digest = item['digest']
        url = item['url']
        news = News(title=title, digest=digest, url=url)
        news_list.append(news)

    almanac_list = get_info.get_almanac()
    almanac_list = almanac_list[0]
    lunar_year = almanac_list['tiangandizhiyear']
    lunar_month = almanac_list['lubarmonth']
    lunar_day = almanac_list['lunarday']
    fitness = almanac_list['fitness']
    taboo = almanac_list['taboo']
    lunar_date = LunarDate(year=lunar_year,month=lunar_month,
                           day=lunar_day, fitness=fitness, taboo=taboo)

    date = almanac_list['lunardate']
    date = date.split('-')
    year = date[0]
    month = date[1]
    day = date[2]

    context = {
        'news_list': news_list,
        'lunar_date': lunar_date,
        'year': year,
        'month': month,
        'day': day,
    }

    return render(request, 'today_news.html', context)
