import bs4 as bs
import urllib.request as ur


url=input("Πληκτρολόγησε το url: ")
try:
    response=ur.urlopen(url).read()
    html=(bs.BeautifulSoup(response,'lxml'))
    body=html.body

    allagi=0
    for url in body.find_all('p'):
        allagi+=1
    for url in body.find_all('br'):
        allagi+=1

    links=0
    for url in body.find_all('a'):
       
        links+=1

    print("Υπάρχουν %i αλλαγές γραμμής και %i λινκς."%(allagi,links))
except:
    print("Κάτι πήγε στραβά.😕")