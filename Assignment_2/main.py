from selenium import webdriver
import requests
from save_images import make_directory, save_images
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

driver_path = 'D:/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
dirnames = ['tshirts for men','shirts for men','sarees']


start = 1
end = 2
for dirname in dirnames:
    current_page_url = driver.get('https://www.amazon.com/s?k='+dirname)
    make_directory(dirname)
    for page in range(start,end+1):
        try:
            page_value = driver.find_element_by_xpath('//li[@class="a-selected"]//a').text
            print('The current scraped page is {}'.format(page_value))

            product_details = scrap_image_url(driver=driver)
            print('Scrapping page {}'.format(page))


            save_images(data=product_details, dirname=dirname, page=page)

            print('Moving to the next page')
            value= driver.find_element_by_xpath('//li[@class="a-last"]//a')
            link = value.get_attribute('href')
            driver.get(link)


        except StaleElementReferenceException as Exception:
            print('We are facing an Exception')

            exp_page = driver.find_element_by_xpath('//li[@class="a-selected"]//a]').text
            print('The page value at the time of exception is {}'.format(exp_page))

            value= driver.find_element_by_xpath('//li[@class="a-selected"]//a')
            link = value.get_attribute('href')
            driver.get(link)

            product_details=scrap_image_url(driver=driver)

            save_images(data=product_details, dirname=dirname, page=page)

            print('Moving to the next page')
            value= driver.find_element_by_xpath('//li[@class="a-last"]//a')
            link = value.get_attribute('href')
            driver.get(link)


