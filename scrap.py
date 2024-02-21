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

rows = soup.find('table').find('tbody').find_all('tr')

#List to store data
data = []

#Loop through each cell in the row
for row in rows:
    #Find all cells in the row
    cells = row.find_all(['th', 'td'])
    #List to store data for each row
    row_data = []
    #Loop through each cell in the row
    for cell in cells:
        #Append cell data to the raw data list
        row_data.append(cell.get_text(strip=True))
    #Append the row data to the data list
    data.append(row_data)

#Convert the data list to a DataFrame
df = pd.DataFrame(data)

#Save DataFrame to Excel file
df.to_excel('scraped_data.xlsx', index=False)

print("Data Saved Successfully!!")
