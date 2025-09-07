import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
time.sleep(3)

jobs = pd.read_csv('data\jobs.csv')
start = time.time()
details = []
i = 0
start= time.time()
for i,link in jobs['href'].items():
    
    if time.time()-start > 1000:
        break
    i+=1
    driver.get(link)
    time.sleep(2)
    det = {}
    det['href'] = link
    try:
        det['payment'] = driver.find_element(By.CSS_SELECTOR, ".compensation__salary").text.strip()
    except:
        det['payment'] = None
    try:
        det['description'] = driver.find_element(By.CSS_SELECTOR, ".description__text.description__text--rich").text.strip()
    except:
        det['description'] = None
    try:
        det['details'] = driver.find_element(By.CSS_SELECTOR, ".description__job-criteria-item").text.strip()
    except:
        det['details'] = None
    details.append(det)
    print(det)

print(f'total is :{i}')
driver.quit()
detailss = pd.DataFrame(details)
detailss.to_csv('data\details.csv', index=False)
