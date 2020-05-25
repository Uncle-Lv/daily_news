from django.shortcuts import render
from ..info_handler import get_info
from ..models.news import News


def index(request):
    content_list = get_info.get_news();

    news_list = []

    for item in content_list:
        title = item['title']
        digest = item['digest']
        news = News(title=title, digest=digest)
        news_list.append(news)

    almanac_list = get_info.get_almanac()
    almanac_list = almanac_list[0]
    fitness = almanac_list['fitness']
    taboo = almanac_list['taboo']

    date = almanac_list['lunardate']
    date = date.split('-')
    year = date[0]
    month = date[1]
    day = date[2]

    lunar_year = almanac_list['tiangandizhiyear']
    lunar_month = almanac_list['lubarmonth']
    lunar_day = almanac_list['lunarday']

    context = {
        'news_list': news_list,
        'fitness': fitness,
        'taboo': taboo,
        'year': year,
        'month': month,
        'day': day,
        'lunar_year': lunar_year,
        'lunar_month': lunar_month,
        'lunar_day': lunar_day
    }


    return render(request, 'today_news.html', context)