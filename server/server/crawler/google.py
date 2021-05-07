from requests_html import HTMLSession
from parsel import Selector
import pandas as pd
import time
from app import app, db, Data


class Crawler():
    def __init__(self, taskid, keywords, delay):
        self.session = HTMLSession()
        self.keyword_list = keywords
        self.taskid = taskid
        self.base_url = 'https://www.google.com/'
        self.data_list = []
        self.delay = delay

    def get_keywords(self):
        with open('keywords.txt', 'r', encoding='utf-8-sig') as f:
            keywords = [i.strip() for i in f.readlines() if i.strip()]
        return keywords

    def search(self, url, keyword, page):
        time.sleep(self.delay)
        print(f'>>>>>>Processing keywords <{keyword}> {page}:{url}')
        r = self.session.get(url)
        if page > 3:
            return
        for i in Selector(r.text).xpath('//*[@id="rso"]//div[@class="g"]'):
            item = {}
            item['keyword'] = keyword
            item['page'] = page
            item['title'] = i.xpath('./div/div/a/h3/span/text()').get('').strip()
            item['desc'] = i.xpath('string(./div/div[2]/div/span)').get('').replace('\n', '').replace('\t', '').replace(
                '\r', '').replace(' ', '').replace('\xa0', '').strip()
            item['url'] = i.xpath('./div/div[2]/div/div/div/a[1]/@href').get('').strip()
            if not item['url']:
                item['url'] = i.xpath('./div/div[1]/a/@href').get('').strip()
            print(item)
            self.data_list.append(item)

        next_page_url = r.html.xpath('//a[@id="pnnext"]/@href')
        if next_page_url:
            next_page_url = self.base_url + next_page_url[0]
            self.search(next_page_url, keyword, page + 1)

    def save(self):
        df = pd.DataFrame(self.data_list)
        path = f'{str(int(time.time()))}.csv'
        df.to_csv(path)

        task_id = self.taskid
        print(self.data_list)
        for item in self.data_list:
            print(item)
            url = item['url']

            with app.app_context():
                datas = Data.query.filter_by(url=url).first()

                if datas is None:
                    db.session.add(Data(
                        task_id=task_id,
                        keyword=item['keyword'],
                        page=item['page'],
                        title=item['title'],
                        desc=item['desc'],
                        url=item['url'],
                    ))

                    db.session.commit()

        msg = "Record successfully added"
        return msg

    def main(self):
        for keyword in self.keyword_list:
            url = self.base_url + 'search?q=' + keyword
            page = 1
            self.search(url, keyword, page)
        self.save()
        return self.data_list


if __name__ == '__main__':
    n = input('>>>>>>Please enter the keyword number:\n').strip()
    try:
        n = int(n)
    except Exception:
        n = 1
    keywords = []
    for i in range(n):
        keyword = input('>>>>>>Please enter the request keyword:\n').strip()
        keywords.append(keyword)
    delay_sec = input('>>>>>>Please enter the request delay interval (seconds):\n').strip()
    try:
        delay_sec = int(delay_sec)
    except Exception:
        delay_sec = 1
    c = Crawler(keywords, delay_sec)
    c.main()
