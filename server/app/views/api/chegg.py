from flask import request
from flask_praetorian import auth_required, current_user
from app import app, db, Task
def get_links(cheat):
    driver.get("https://www.chegg.com/study/tbs")
    f = open("demofile2.txt", "a")
    user = driver.find_element_by_id("chegg-searchbox")
    user.send_keys(cheat)
    user.send_keys(Keys.RETURN);
    time.sleep(4);
    links  = []
    for i in range(1,8):
        questions = driver.find_element_by_xpath('//*[@id="serp_tabs_tabpanel_2"]/div[1]/div[2]/div/div[' + str(i) + ']/div/div/a')
        link = questions.get_attribute("href");
        links.append(link)
    #f.close()
    return links

def scrape_page(link, cheat):
    client = ScraperAPIClient('6173123344c04a4f3dc5b367e956cfe9')
    result = client.get(url = link).text
   # print (result)
    #print(cheat)
    if cheat in result:
        f = open("CheggResults.txt" , "a")
        f.write(link + "\n")
        #print("CHEATER")
 

@app.route('/api/chegg', methods=['POST'])
@auth_required
def chegg():
    user = current_user()
    keywords = request.form['keywords']
    links = get_links(keywords)
    for i in links:
        scrape_page(i, cheat)