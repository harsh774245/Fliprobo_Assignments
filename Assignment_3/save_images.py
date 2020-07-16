import shutil
import os
import requests
import pandas as pd
import csv

def make_directory(dirname):
    current_path=os.getcwd()
    path=os.path.join(current_path,dirname)
    if not os.path.exists(path):
        os.makedirs(path)

def save_images(data, dirname, page):
        for index, link in enumerate(data['image_urls']):
            # If we want to download just 100 images, uncomment the lines below
            # if index>=20 and page==4:
            #     break
            print('Downloading {0} image'.format(index+1))
            response = requests.get(link)
            with open('{0}/img_{1}{2}.jpg'.format(dirname,page,index), 'wb') as file:
                file.write(response.content)
            