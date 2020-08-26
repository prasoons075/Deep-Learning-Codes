# Deep Learning Codes
 My Deep Learning library for being updated at on going updates in AI/ML insdustry.
 
 from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib
from datetime import datetime, timedelta
from threading import Timer
import pandas as pd
import bs4 as bs
import urllib.request

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_data(self):
        #try:
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath("//table[@id='main_table_countries_today']")
        columnnames=['Country','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','Active Cases','Serious/Critical','Tot Cases per 1M pop','Deaths per 1M pop']
        data = pd.DataFrame(columns=columnnames)
        for row in table.find_elements_by_xpath(".//tr"):
                to_append=[td.text.replace(",","") for td in row.find_elements_by_xpath(".//td")]
                if len(to_append)!=0:
                    a_series = pd.Series(to_append, index = data.columns)
                    data = data.append(a_series, ignore_index=True)
        
        data.to_csv(r'coronavirus_data.csv', index = False, header=True)

        self.driver.close()
        self.driver.quit()

bot = Coronavirus()
bot.get_data()


