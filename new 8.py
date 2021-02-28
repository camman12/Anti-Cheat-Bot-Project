# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.chrome.options import Options





# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Firefox()


# print("enter search term")
# cheat = input()
# driver.get("https://www.google.com/")
# f = open("demofile2.txt", "a")
# cam = driver.find_element_by_name("q")
# cam.send_keys(cheat)
# cam.send_keys(Keys.ENTER)

# for x in range(1,8):
#     time.sleep(3)
#     xpath_ = '//*[@id="rso"]/div[' + str(x) + ']/div/div[1]/a'
#     driver.find_element_by_xpath(xpath_).click()
#     html_source = driver.page_source
#     if "chegg" in driver.current_url:
#         print("chegg will be implemented later")
#         driver.back()
#     elif cheat in html_source:
#         print("SITE THAT CONTAINS CLASS MATERIALS:" + driver.current_url)
#         f.write(driver.current_url + '\n')
#         driver.back()
    
# f.close()



#print(html_source)

from requests_html import HTMLSession
from parsel import Selector
import pandas as pd
import time


class Crawler():
    def __init__(self, keyword, delay):
        self.session = HTMLSession()
        # self.keyword_list = self.get_keywords()
        self.keyword_list = [keyword]
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

    def main(self):
        for keyword in self.keyword_list:
            url = self.base_url + 'search?q=' + keyword
            page = 1
            self.search(url, keyword, page)
        self.save()


if __name__ == '__main__':
    keyword = input('>>>>>>Please enter the request keyword:\n').strip()
    delay_sec = input('>>>>>>Please enter the request delay interval (seconds):\n').strip()
    try:
        keyword = str(keyword)
        delay_sec = int(delay_sec)
    except:
        delay_sec = 1
    c = Crawler(keyword, delay_sec)
    c.main()
