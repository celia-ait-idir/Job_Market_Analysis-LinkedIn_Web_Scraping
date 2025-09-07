from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re


service = Service("chromedriver.exe")
dr = webdriver.Chrome(service=service)


url = "https://www.linkedin.com/jobs/search?keywords=data%20science&location=United%20States"
dr.get(url)
time.sleep(3)

start = time.time()
while True:
    if time.time()-start > 300:
        break
    last_height = dr.execute_script("return document.body.scrollHeight")

    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    new_height = dr.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            button = dr.find_element(By.CLASS_NAME, "infinite-scroller__show-more-button")
            dr.execute_script("arguments[0].click();", button)
            time.sleep(3)
        except:
            pass
        


jobs = dr.find_elements(By.CLASS_NAME, "base-card")
jobsies = []

for job in jobs:
    new_job = {}
    try:
        new_job["title"] = job.find_element(By.CLASS_NAME, "base-search-card__title").text.strip()
    except:
        new_job["title"] = None

    try:
        new_job["company"] = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip()
    except:
        new_job["company"] = None

    try:
        new_job["location"] = job.find_element(By.CLASS_NAME, "job-search-card__location").text.strip()
    except:
        new_job["location"] = None
        
    try:
        job_link = job.find_element(By.CLASS_NAME, 'base-card__full-link')
        new_job['href'] = job_link.get_attribute('href')
 
    except:
        new_job['id'] = None

    print(new_job)
    jobsies.append(new_job)


jobss = pd.DataFrame(jobsies)
jobss.to_csv("data/jobs.csv", index=False)

dr.quit()
print("YAY we are done ")
