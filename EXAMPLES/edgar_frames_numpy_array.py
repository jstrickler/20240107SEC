import io
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from edgar_user_agent import EDGAR_USER_AGENT

# headers for GET requests
GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

TAXONOMY = 'us-gaap'
CONCEPT = "AccountsPayableCurrent"
YEAR = 2022
QUARTER = 3

# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json
url = f"https://data.sec.gov/api/xbrl/frames/{TAXONOMY}/{CONCEPT}/USD/CY{YEAR}Q{QUARTER}I.json"

response = requests.get(url, headers=GET_HEADERS)

raw_data = response.json().get('data')

data = np.array(raw_data)

print(f"{type(data) = }")

print(f"{data[0] = }")

print(data)



