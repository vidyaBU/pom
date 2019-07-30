from selenium import webdriver as wd
driver =wd.Firefox(executable_path='C:\Program Files\geckodrive\geckodriver')
driver.get('https://www.google.com')

driver.find_element_by_name('q').send_keys('Software Testing')
driver.find_element_by_name('btnK').click()

