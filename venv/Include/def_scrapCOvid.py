import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import numbers
import pandas as pd
import time


def browser ():
    site = ('www.bmkg.go.id')
    driver = webdriver.Chrome(r"D:\New folder\chrome driver\chromedriver.exe")
    driver.get(site)



browser()


