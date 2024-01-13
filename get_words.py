import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import bs4
import csv
import requests
from typing import NoReturn
import datetime

script_path_my = os.path.dirname(os.path.abspath(__file__))
day = datetime.datetime.now().strftime('%y-%m-%d')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
start_url = 'https://wordsonline.ru/'

dict_alphabet = {
    'А': ['a', '@', 'A'],
    'Б': ['B', 'b', '6'],
    'В': ['V', 'v'],
    'Г': ['G', 'g'],
    'Д': ['D', 'd'],
    'Е': ['E', 'e'],
    'Ж': ['J', 'j'],
    'З': ['Z', 'z'],
    'И': ['I', 'i', '1'],
    'Й': ['I', 'i'],
    'К': ['K', 'k'],
    'Л': ['L', 'l'],
    'М': ['M', 'm'],
    'Н': ['N', 'n'],
    'О': ['O', 'o', '0'],
    'П': ['P', 'p'],
    'Р': ['R', 'r'],
    'С': ['S', 's', 'C', 'c'],
    'Т': ['T', 't'],
    'У': ['U', 'u', 'Y', 'y'],
    'Ф': ['F', 'f'],
    'Х': ['H', 'h', 'X', 'x'],
    'Ц': ['C', 'c', 'Ts', 'ts'],
    'Ч': ['Ch', 'ch', '4'],
    'Ш': ['Sh', 'sh', '6'],
    'Щ': ['Sh', 'sh', '6'],
    'Э': ['E', 'e'],
    'Ю': ['Iu', 'iu', 'iU'],
    'Я': ['ya', 'Ya', 'Ia', 'ia']
}
