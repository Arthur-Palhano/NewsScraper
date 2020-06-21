from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

news = []

def MSN():
  firefox = webdriver.Firefox(options=options)
  firefox.get("https://www.msn.com/pt-br/")

  bruteNews = firefox.find_elements_by_class_name("title")

  news = []

  for new in bruteNews:
      if new.text != "":
          news.append(new.text)
  firefox.close()

###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

def MSNNews():
  firefox = webdriver.Firefox(options=options)
  firefox.get("https://www.msn.com/pt-br/noticias")

  bruteNews = firefox.find_elements_by_tag_name("h3")

  for new in bruteNews:
      if new.text != "":
          news.append(new.text)
  firefox.close()

def search():
  MSN()
  MSNNews()

search()

for new in news:
    print(f"° {new}")
    print()