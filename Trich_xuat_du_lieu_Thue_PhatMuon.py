#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Trích xuất dữ liệu
#-------------------
# data hxml
# ------------------------------------
import urllib.request, urllib.parse, urllib.error
with urllib.request.urlopen('https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7') as response:
   xml = response.read()
#print(xml)

from bs4 import BeautifulSoup
soup = BeautifulSoup(xml, 'html.parser')
#print(soup.prettify())
#print(soup.tax)
#print('Count thuế thu nhập cá nhân tại Việt Nam:', len(soup.find_all('tax')))
# ------------------------------------
list_max=[]
max = soup.find_all('max')
for n in max:
    #print(max)
    #print(n.contents)
    list_max.append(n.contents)
'print(list_max)'                                   # [['5'], ['10'], ['18'], ['5'], ['32'], ['52'], ['80']]
# ------------------------------------
n3_list_max=[]
for n in list_max:
    n3_list_max.append(int(n[0]))
'print(n3_list_max)'                                # [5, 10, 18, 5, 32, 52, 80]
# ------------------------------------
list_min=[]
min=soup.find_all('min')
for n in min:
    #print(n.contents)
    list_min.append(n.contents)
'print(list_min)'                                   # [['0'], ['5'], ['10'], ['0'], ['18'], ['32'], ['52'], ['80']]
# ------------------------------------
n1_list_min=[]
for n in list_min:
    n1_list_min.append(int(n[0]))
'print(n1_list_min)'                                # [0, 5, 10, 0, 18, 32, 52, 80]
# ------------------------------------
list_value=[]
value = soup.find_all('value')
for n in value:
    #print(n.contents)
    list_value.append(n.contents)
'print(list_value)'                                 # [['5'], ['10'], ['15'], ['5'], ['20'], ['25'], ['30'], ['35']]
# ------------------------------------
n2_list_value=[]
for n in list_value:
    n2_list_value.append(int(n[0]))
'print(n2_list_value)'                              # [5, 10, 15, 5, 20, 25, 30, 35]
# ------------------------------------
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('data Xml')
print('Dữ liệu về Thuế thu nhập cá nhân')
print('__________________________')

for n1,n3,n2 in zip(n1_list_min,n3_list_max,n2_list_value):
    print('min < lương chịu thuế* <= max |', f'{n1} < {n3}% luong <= {n2} |')




#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# data Json
# ------------------------------------
import json
response = urllib.request.urlopen('https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de')
json = json.loads(response.read().decode())
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('data Json')
print('Quy định thưởng phạt của công ty, nhân viên của công ty dựa trên số ngày đi muộn (late_coming_days)')
#print(json)
print('__________________________')
for n in json:
    try:
        print('min <= late_coming_days * < max |', f'{n["min"]} <= *{n["value"]} <= {n["max"]}')

    except KeyError:
        print('min <= late_coming_days * < max |', f'{n["min"]} <= *{n["value"]} <= no max')
        pass
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
