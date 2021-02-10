from datetime import datetime as date
import os
import sys
import io
ctime = date.now()
yeardir = f"{os.path.dirname(os.path.abspath(__file__))}/{ctime.year}"
monthdir = f"{yeardir}/{ctime.month}"
daydir = f"{monthdir}/{ctime.day}"
hourdir = f"{daydir}/{ctime.hour}"
if not os.path.exists(yeardir):
    print(f"{ctime.year} isimli klasör oluşturuldu")
    os.makedirs(yeardir)
if not os.path.exists(monthdir):
    print(f"{ctime.month} isimli klasör oluşturuldu")
    os.makedirs(monthdir)
if not os.path.exists(daydir):
    print(f"{ctime.day} isimli klasör oluşturuldu")
    os.makedirs(daydir)
if not os.path.exists(hourdir):
    print(f"{ctime.hour} isimli klasör oluşturuldu")
    os.makedirs(hourdir)
print("Kaç Adet Link Kısaltılacak")
try:
    urlcount = int(input())
except ValueError:
    print('Geçersiz Sayı')
    sys.exit()
else:
    pass
curcount = 0
import requests
while urlcount > curcount:
    print(str(curcount+1)+". Link nedir")
    url = input()
    data = {
  'url': url
  }
    response = requests.post('https://cleanuri.com/api/v1/shorten', data=data)
    print(f"Kısaltılan Link : {response.json()['result_url']}")
    curcount = curcount +1
    with io.open(hourdir+"/"+str(ctime.minute)+"-"+"shorted.txt","x",encoding="utf-8") as myfile:
        myfile.write("------------------------------ \n")
        myfile.write("Orjinal URL : "+url+"\n")
        myfile.write("Kısaltılan URL : "+response.json()['result_url']+"\n")
        myfile.write("------------------------------"+"\n")