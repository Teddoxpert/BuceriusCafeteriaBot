from urllib.request import urlopen
import sys
import webbrowser
from bs4 import BeautifulSoup
import time
import datetime

def reloadMenu():
    html = urlopen("http://speiseplan.studierendenwerk-hamburg.de/en/410/2014/0/")
    bsObj = BeautifulSoup(html.read(),'lxml')

    nameList = bsObj.find_all('td',class_="dish-description")
    nameList = [(name.get_text()).strip() for name in nameList]

    masterPriceList = bsObj.find_all('td',class_="price")
    masterPriceList = [(price.get_text()).strip() for price in masterPriceList]

    studentPriceList = masterPriceList[0:15:3]
    psPriceList = masterPriceList[1:15:3]
    otherPriceList = masterPriceList[2:15:3]

    return nameList, masterPriceList, studentPriceList, psPriceList, otherPriceList

def displayMenu(userInput):
    dataList = reloadMenu()
    menuDict = {}
     #names, master prices, student prices, public servant prices, other prices
    nameList = dataList[0]
    studentPriceList = dataList[2]
    psPriceList = dataList[3]

    if datetime.datetime.now().isoweekday() in range (6,8):
        return "It's the weekend, the cafeteria is closed today. Don't disturb the cooks and me!"

    displayText ='The menu for today, ' + time.strftime("%d/%m/%Y")+ ', is:\n\n'
    if userInput == 'student':
        for name in nameList:
            menuDict[name] = studentPriceList[nameList.index(name)]

        for key,value in menuDict.items():
            displayText = displayText + (key + "\n" + "Price: " + value + "\n" + "\n")
        return (displayText)

    elif userInput == 'publicservant':
        for name in nameList:
            menuDict[name] = psPriceList[nameList.index(name)]
        for key,value in menuDict.items():
            displayText = displayText + (key + "\n" + "Price: " + value + "\n" + "\n")
        return (displayText)
    else:
        print ('Try again')
        pass
