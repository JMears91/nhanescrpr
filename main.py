# Imported packages
from selenium import webdriver
import pandas as pd
import os
import chromedriver_binary
import config
from Scraper_Functions import Scrape_Saver as SS


SS.Yearselector()
SS.Componentselector()
SS.ScrapeSaveMain()

print('Download complete')
