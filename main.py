from selenium import webdriver
import os
import numpy as np
import pandas as pd

class Crawler:
    def __init__(self):
        self.data = []
        
    def findItems(self, alpList):
        for i in alpList:
            try:
                self.driver = webdriver.Chrome(os.getcwd() + "\cd.exe")
                # url gets search keyword from i 
                print(i)
                url = "https://play.google.com/store/search?q=" + i + "&c=apps&hl=en_US"             
                self.driver.get(url)
                tempData = self.driver.find_elements_by_class_name('Vpfmgd');
                data = []
                for title in tempData:
                    data.append(title.text)
                self.driver.close()
                self.refineData(data)
                self.driver.close()
            except:
                print(url)
                print("ERROR")
        
                continue                                                                 
    def refineData(self, tempData):
        
        for x in tempData:
            x = list(x)
            cur = ''
            for i in range(len(x)):
                char = x[i]
                if char == '\n':
                    break
                else: 
                    cur += char       
            self.data.append(cur)
        print(self.data)
        
    def crawlAll(self): # 1
        alpList = ['a','b','c','d','e','f','g',
                   'h','i','j','k','l','m','n','o','p','q','r'
                   ,'t','u','v','w','x','y','z']
        alpList_DEBUG = ['a','b'] # debug
        self.findItems(alpList); # search keyword in alpList

#        for x in alpList:
#            self.findItems(x)
#        for x in alpList:
#            self.findItems(x)
#            if x == 'e':
#                break

    def save(self):
        result = list(set(self.data))
        result = np.array(result)
        pd.DataFrame(result).to_csv(os.getcwd() + "/result.csv")
        
a = Crawler()
a.crawlAll()