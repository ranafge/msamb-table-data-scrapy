
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

cookies = {
    'ASP.NET_SessionId': 'ncecz1gsax2jusfkbjkwogmm',
    '__RequestVerificationToken': '-wxVmWHXligDDbyhoG8ByXFmt8Ec6TENDnZvLqdTXmp00R2w2qORtBn_QZDiPd5_HWW7kA24qwrxTBs-jDqmjKrzrLAcLntTltSgGXHTG0o1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ASP.NET_SessionId=ncecz1gsax2jusfkbjkwogmm; __RequestVerificationToken=-wxVmWHXligDDbyhoG8ByXFmt8Ec6TENDnZvLqdTXmp00R2w2qORtBn_QZDiPd5_HWW7kA24qwrxTBs-jDqmjKrzrLAcLntTltSgGXHTG0o1',
    'Referer': 'https://www.msamb.com/ApmcDetail/APMCPriceInformation',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'commodityCode': '08004',
    'apmcCode': 'null',
}

response = requests.get('https://www.msamb.com/ApmcDetail/DataGridBind', params=params, cookies=cookies, headers=headers)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())
print('Starting ...')
header = [
"APMC",
"Variety",
"Unit",
"Quantity",
"Lrate",
"Hrate",
"Modal"]
table_data = soup.find_all('tr')[1:]
original_data = [data.text.replace("\n", " ").strip().split(' ') for data in table_data]

print(tabulate(original_data, headers=header))



