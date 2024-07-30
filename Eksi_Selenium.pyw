from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
url = input("Enter your URL: ")
#url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p=" örnek olarak bu url i kullanabilirsiniz.
#url'in sonu örnekte olduğu gibi eşitir ile bitmeli yani sayfa sayısının değişebeleceği şekilde ayarlanmalıdır.

pagerange = int(input("Enter the page range: "))
pageCount = 1

texts = []

entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,pagerange)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
        texts.append(element.text)
    time.sleep(2)
    pageCount += 1

with open("entries.txt","w",encoding = "utf-8") as file:
    for text in texts:
        file.write(str(entryCount) + ".\n" + text + "\n")
        file.write("***********************************\n")
        entryCount += 1

browser.close()
