import requests
from bs4 import BeautifulSoup
import time

links = []



for i in range(26):
    url =  'http://example.webscraping.com/places/default/index/' + str(i)
    responce = requests.get(url)
    print(responce)
    if responce.ok:
        print("page: " + str(i))
        soup = BeautifulSoup(responce.text, "html.parser")
        countrys = soup.findAll('td')

        for country in countrys:
            a = country.find("a")
            link = a["href"]
            links.append('http://example.webscraping.com/' + link)
        time.sleep(1)
print (len(links))

with open("urls.txt" , "w") as file:
    for link in links:
        file.write(link + "\n")


with open ('urls.txt', 'r') as inf:
    with open ("pays.csv" , "w") as outf:
        outf.write('pays, population\n')
        for row in inf:
            url = row.strip()
            responce = requests.get(url)
            if responce.ok:
                soup = BeautifulSoup(responce.text, "html.parser")
                countryName = soup.find('tr' , {'id' : 'places_country__row'}).find('td', {"class" : "w2p_fw"})
                pop = soup.find('tr' , {'id' : 'places_population__row'}).find('td', {"class" : "w2p_fw"})
                print ("Pays: " + str(countryName.text) + ',' + "POP : " + str(pop.text))
                outf.write(countryName.text + ',' + pop.text.replace(',', '') + '\n')
                time.sleep(1)

