import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://kmpdc.go.ke/Registers/General_Practitioners.php'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}




response = requests.get(url,headers=headers)
response.raise_for_status()
#Create soup object
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)