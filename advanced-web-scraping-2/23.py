from selenium import webdriver


url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome()
driver.get(url)
input('Press ENTER to close the automated browser')
driver.quit()