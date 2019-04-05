import requests
from bs4 import BeautifulSoup
import csv

attri=[ 'Name', 'URL', 'Author', 'Price' , 'Number of Ratings' , 'Average Rating']


with open('in_book.csv','a') as fil:
          wriat= csv.writer(fil)
          wriat.writerow(attri)
          attri.clear()
      

for pg in range(1,5):
     infor=requests.get("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg="+str(pg))
     data=infor.text
     soup=BeautifulSoup(data,'lxml')
     mov=soup.find_all('div',class_='zg_itemImmersion')

     for bst in range(20):
             try: 
                   name=mov[bst].find_all('a',class_='a-link-normal')
                   attri.append(name[0].text)
             except:
                   attri.append("NOT AVAILABLE")            
             try:
                   url=mov[bst].find_all('a',class_='a-section a-spacing-none p13n-asin')
                   attri.append(url[0].a['href'])
             except:
                  attri.append("NOT AVAILABLE")
             
             try:
                   auth=mov[bst].find_all('a',class_='a-row a-size-small')
                   attri.append(auth[0].text)
             except:
                  attri.append("NOT AVAILABLE")
             
             try:
                   ratnum=mov[bst].find_all('a',class_='a-link-normal a-text-normal')
                   attri.append("Rs"+str(name[0].text))
             except:
                  attri.append("NOT AVAILABLE")
               
             try:
                   avgrat=mov[bst].find_all('a',class_='a-size-small a-link-normal')
                   attri.append(avgrat[0].text)
             except:
                  attri.append("NOT AVAILABLE")

             try:
                   name=mov[bst].find_all('a',class_='a-link-normal')
                   attri.append(name[0].a['title'])
             except:
                  attri.append("NOT AVAILABLE")
      
             with open('in_book.csv','a') as fil:
                       wriat= csv.writer(fil)
                       wriat.writerow(attri)
                       attri.clear()

