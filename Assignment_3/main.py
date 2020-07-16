from selenium import webdriver
import requests
from save_images import make_directory, save_images
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

driver_path = 'D:/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
dirnames = ['half sleeve tshirts for men','full sleeve shirts for men','sarees']


start = 1
end = 3
for dirname in dirnames:
    current_page_url = driver.get('https://www.flipkart.com/search?q='+dirname)
    make_directory(dirname)
    for page in range(start,end+1):
        try:
            product_details = scrap_image_url(driver=driver)
            print('Scrapping page {}'.format(page))

            save_images(data=product_details, dirname=dirname, page=page)

            print('Moving to the next page')
            button_type = driver.find_element_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')
            if button_type=='Next':
                driver.find_element_by_xpath("//a[@class='_3fVaIS']").click()
            else:
                driver.find_element_by_xpath("//a[@class='_3fVaIS'][2]").click()


        except StaleElementReferenceException as Exception:
            print('We are facing an Exception')

            exp_page = driver.find_element_by_xpath('//a[@class="_2Xp0TH fyt9Eu"]').text
            print('The page value at the time of exception is {}'.format(exp_page))

            value= driver.find_element_by_xpath('//a[@class="_2Xp0TH fyt9Eu"]')
            link = value.get_attribute('href')
            driver.get(link)

            product_details=scrap_image_url(driver=driver)

            save_images(data=product_details, dirname=dirname, page=page)

            print('Moving to the next page')
            button_type = driver.find_element_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')
            if button_type=='Next':
                driver.find_element_by_xpath("//a[@class='_3fVaIS']").click()
            else:
                driver.find_element_by_xpath("//a[@class='_3fVaIS'][2]").click()


