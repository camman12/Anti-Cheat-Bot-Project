
from requests_html import HTMLSession
from parsel import Selector
import pandas as pd
import time
import sqlite3
import uuid

DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
    db = connect_db()
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

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
        path = f'{str(int(time.time()))}.xlsx'
        with pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
            df.to_excel(writer, index=False, encoding='utf-8-sig')

        task_id = self.taskid
        print(self.data_list)
        for item in self.data_list:
            print(item)
            url = item['url']

            datas = query_db('select * from datas where url = \'' + url + '\'', one=True)
            if datas == None:
                data_id = str(uuid.uuid4())
                with sqlite3.connect("database.db") as con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO datas (data_id,task_id,keyword,page,title,desc,url) VALUES (?,?,?,?,?,?,?)",(data_id,task_id,item['keyword'],item['page'],item['title'],item['desc'],item['url']) )
                        con.commit()
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
    except:
        n = 1
    keywords = []
    for i in range(n):
        keyword = input('>>>>>>Please enter the request keyword:\n').strip()
        keywords.append(keyword)
    delay_sec = input('>>>>>>Please enter the request delay interval (seconds):\n').strip()
    try:
        delay_sec = int(delay_sec)
    except:
        delay_sec = 1
    c = Crawler(keywords, delay_sec)
    c.main()
