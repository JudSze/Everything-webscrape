from bs4 import BeautifulSoup
import requests 
import lxml
import pandas as pd 

# The page to scrape
url = "https://portals.broadinstitute.org/ctrp/?page=#ctd2Dataset"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"}
response = requests.get(url) 

soup=BeautifulSoup(response.text, 'html.parser')
soup

targets_table = soup.find('table',attrs={"id":"summaryDatasetTableTable"})
print(targets_table)

headers=[]
for i in targets_table.findall('thead'):
    title = i.text
    headers.append(title)
    
