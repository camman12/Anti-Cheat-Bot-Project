#This will not run on online IDE 
import requests 
import html2text
from bs4 import BeautifulSoup 
  
URL = "https://quizlet.com/197813332/cs-271-final-review-flash-cards/"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib 

print(soup.get_text())




test = soup.prettify()
if "What is a register?" in test:
    print("CHEAT PAGE DETECTED")
else:
    print("no worky")