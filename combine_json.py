# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:25:27 2019

@author: lefty
"""

import json
import glob
from fuzzywuzzy import process


def pull_data():
    result = {}
    counter = 1
    for f in glob.glob("C:/Users/lefty/OneDrive/Desktop/Yummly28K/metadata27638/*.json"):
        with open(f, "rb") as infile:
            obj = (json.load(infile))
            result[counter] = obj['ingredientLines']
            counter += 1
            if counter % 1000 == 0:
                print(counter)
                
    return result

def clean_data(ingred_dict):
    file = open("ingredients.csv", "r")
    l = file.readlines()
    file.close()
    nb_ingred = len(l)
    for i in range(nb_ingred):
        l[i] = l[i].strip('\n')
    n = len(ingred_dict)
    
    
    
    temp = ingred_dict[1]
    delete_list = []
    result = []
    counter = 0
    for h in range(1, n+1):
        temp = ingred_dict[h]
        mini_n = len(temp)
        for i in range(mini_n):
            change = False
            choices = []
            for j in range(nb_ingred):
                if l[j] in temp[i]:
                    choices.append(l[j])
                    change = True
                
            if (change == False):
                delete_list.append(temp[i])
            else:
                target = temp[i]
                best_match = process.extractOne(target, choices)
                temp[i] = best_match[0]
                
                
        for item in delete_list:
            try:
                temp.remove(item)
            except:
                continue

        result.append(temp)
        if counter % 1000 == 0:
            print(counter)
        counter += 1
    
    file = open("ingredients_spaces_alt.csv", "w+")
    for ingred in result:
        try:
            temp = ",".join(ingred)
        except:
            temp = ingred
            
        temp += '\n'
        file.write(temp)
        
    file.close()
        
    

def main():
    d = pull_data()
    clean_data(d)
    
main()
    
        
         
