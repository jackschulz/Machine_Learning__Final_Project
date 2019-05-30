# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
When importing the data due to sql pulling errors, turn each line into a set.
Exlcusion List
["Oils and Dressings", "Spices and Seasonings", "Bakery", "Baking", "Sauces and Condiments", "Canned and Jarred Goods", "Beverages", "Wine, Beer and Spirits"]
"""
### add dairy exclusion

import io
#import csv

def load_data(data):
    
    file = io.open(data, "r", encoding='utf-8')
    l = file.readlines()
    file.close()
    return l

def clean_data(file, exclude):
    new = io.open("recipies.csv", "w+", encoding='utf-8')
    data = load_data(file)
    n = len(data)
    d = {}
    temp = data[0].split(',')
    temp = ','.join(temp)
    temp = temp[:-4]
    temp+='\n'
    new.write(temp)
    #key = ''
    for i in range(1, n):
        temp = data[i].split(',')
        #print(temp)
            
        if temp[4] not in exclude:
            if "Milk" not in temp[3]:
                #print('past round 1')
                if d.get(temp[1]) != None:
                    #print('past round 2')
                    if temp[3] not in d[temp[1]]:
                        #print('fire off')
                        d[temp[1]] += [temp[3]]
                        temp = ','.join(temp)
                        temp = temp[:-4]
                        temp+='\n'
                        new.write(temp)
                else:
                    item = [temp[3]]
                    d[temp[1]] = item
                    #print('add new key')
                    #print(item)
    
                    temp = ','.join(temp)
                    temp = temp[:-4]
                    temp+='\n'
                    new.write(temp)
        
            
        #print(d)
    new.close()
    #print(d)    
def cnt():
    file = "recipies.csv"
    ingred = load_data(file)
    n = len(ingred)
    s = set()
    """
    d = {}
    temp_key = ""
    
    for i in range(n):
        temp  = ingred.split(',')
        item = temp[3]
        if item.find(' ') != -1:
            l = item.split(' ')
            ingred = set(l)
            for word in ingred:
                for key in d.keys
            
            
    
    """
    ing = []
    for i in range(1, n):
        temp = ingred[i].split(',')
        #print(temp)
        item = temp[3]
        if item.find(' ') != -1:
            item.split(' ')
            if len(item) > 1:
                
                
        s.add(item)
    f = list(s)
    f.sort()
    print(f)
    print(len(f))
    """
    """
            
        
    
def main():
    file = "temp.csv"
    
    exclude = ["Oils and Dressings", "Spices and Seasonings", "Bakery", "Baking", "Sauces and Condiments", "Canned and Jarred Goods", "Beverages", "Wine, Beer and Spirits"]
    #clean_data(file, exclude)
    cnt()
        
    
main()