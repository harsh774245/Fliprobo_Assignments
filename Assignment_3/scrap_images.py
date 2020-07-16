def scrap_image_url(driver):
    images=driver.find_elements_by_xpath("//img[@class='_3togXc']")

    product_data={}
    product_data['image_urls']=[]

    for image in images:
        source=image.get_attribute('src')
        product_data['image_urls'].append(source)

    # product_data=product_data['image_urls'][0:100]
    return product_data