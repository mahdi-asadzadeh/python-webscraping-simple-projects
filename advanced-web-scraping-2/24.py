from selenium import webdriver


url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome()
driver.get(url)

for quote in driver.find_elements_by_class_name('quote'):
    print(quote.text)
    print(quote)

print(driver.find_elements_by_class_name('quote'))

input('Press ENTER to close the automated browser')
driver.quit()
