import requests
from bs4 import BeautifulSoup
# word = input( '請輸入英文字:' )
    
def read( word ):   
    url = f'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtiZwrT3Bmxysilxx7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANtSU9xUFFNYlNIYXV6YUZJdW1EX19BBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DdHcuZGljdGlvbmFyeS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM0BHF1ZXJ5A2hvcGUEdF9zdG1wAzE3MTg2MzYzMzg-?p={word}&fr=sfp&iscqry=&fr2=sb-top-search'



    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('div', class_="layoutCenter")
    try:
        row = data.find_all('li')[0]
        english = row.find('span').text
        phones = row.find_all('span')
        phone = [e.text for e in phones]
        s = " ".join( phone )
        # s = row.find('sub')
        return( english + ' => ' + s )
    except:
        return( '查無此字' )
    data
        
read('wish')