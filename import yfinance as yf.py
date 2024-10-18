import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib_inline
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Exercise 1

tesla = yf.Ticker("TSLA")

url = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html.data.content')

# Excersice 2
tesla_data = pd.DataFrame(columns=["Date_1", "Anual_Revenue", "Date_2", "Revenue", "Sector", "Industry","Market cap", "tesla_Revenue"])

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", regex=True)

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Exercise 3
Game_Stop = yf.Ticker("GME")

Game_Stop ["max"]

Game_Stop_share_price_data = Game_Stop.history(period="max")

Game_Stop_share_price_data.reset_index(inplace=True)

# Exercise 4

url = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html_data_2')
soup.find_all("tbody")[1]

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    Game_Stop_data = pd.concat([Game_Stop_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)  

Game_Stop_data = pd.DataFrame(columns=["Date_1", "Anual_Revenue", "Date_2", "Revenue", "Sector", "Industry","Market cap", "tesla_Revenue"])

Game_Stop_revenue["Revenue"] = Game_Stop_revenue['Revenue'].str.replace(',|\$',"", regex=True)

Game_Stop_revenue.dropna(inplace=True)

Game_Stop_revenue = Game_Stop_revenue[tesla_revenue['Revenue'] != ""]

# Exercise 5

tesla_share_price_data.plot(x="Date", y="Open")

tesla.dividends

tesla.dividends.plot()

# Exercise 6

Game_Stop_share_price_data.plot(x="Date", y="Open")

Game_Stop.dividends

Game_Stop.dividends.plot()