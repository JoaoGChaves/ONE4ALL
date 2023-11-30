from django.test import TestCase 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 
import random 
import string 
import time 
import os 
import tempfile 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-gpu") 
browser = webdriver.Chrome(options=chrome_options) 
wait = WebDriverWait(browser, 10) 
username = ''.join(random.choices(string.ascii_lowercase, k=8)) 
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TesteProjetos (TestCase):
  def teste_a_objetivo (self):
      browser.get('url da pagina')
      time.sleep(3)
      browser.find_element(By.ID, 'tabela').click()
      time.sleep(3)
      browser.get('url da pagina')
      time.sleep(3)
      browser.find_element(By.ID, 'queroAjudar').click()
      time.sleep(3)
      browser.find_element(By.ID, 'mensal').click()
      time.sleep(3)
      browser.find_element(By.ID, '80').click()
      time.sleep(3)
      browser.find_element(By.ID, 'continuar').click()
      time.sleep(3)
      browser.find_element(By.ID, 'finalizar').click()
      time.sleep(3)