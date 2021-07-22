from selenium import webdriver


url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

for quote in driver.find_elements_by_class_name('quote'):
    print(quote.text)

input('Press ENTER to close the automated browser')
driver.quit()