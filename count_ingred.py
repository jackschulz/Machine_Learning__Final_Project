# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:19:33 2019

@author: lefty
"""
import operator

def count_ingred():
    file = open("ingredients_spaces_alt.csv", 'r')
    l = file.readlines()
    file.close()
    
    n = len(l)
    count = {}
    for i in range(n):
        l[i] = l[i].strip('\n')
        l[i] = l[i].split(',')
        
    for i in range(n):
        mini_n = len(l[i])
        for j in range(mini_n):
            if count.get(l[i][j]) == None:
                count[l[i][j]] = 1
            else:
                count[l[i][j]] += 1
                
    count_list = []
    for i,j in count.items():
        count_list.append((i,j))
    
    count_list.sort(key= operator.itemgetter(1))
    print(count_list)
    file = open("most_popular_alt.csv", 'w+')
    m = len(count_list)
    for i in range(m-1, -1, -1):
        temp = count_list[i][0] + ',' + str(count_list[i][1]) + '\n'
        file.write(temp)
    file.close()
def main():
    count_ingred()
    
main()