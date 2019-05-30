# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:31:46 2019

@author: lefty
"""

def one_hot_meat(meat_list, exclusion_list):
    file = open("ingredients_spaces_alt.csv", "r")
    l = file.readlines()
    file.close()
    recipes = []
    for item in l:
        temp = item.strip('\n')
        temp = temp.split(',')
        recipes.append(temp)
        
    nb_recipes = len(recipes)
    nb_target_items = len(meat_list)
    #build ingredient dictionary
    one_hot_meat = [[0 for col in range(nb_target_items)] for row in range(nb_recipes)]
    d = {}
    for i in range(nb_target_items):
        d[meat_list[i]] = i

    print(d)
    for i in range(nb_recipes):
        temp = recipes[i]
        mini_n = len(temp)
        found = False
        found_meat = False
        for j in range(mini_n):
            for meat in meat_list:
                if meat in temp[j]:
                    found = True
                    break
            ignore = False
            if (found):
                for exclude in exclusion_list:
                    if temp[j] == exclude:
                        ignore = True
                        found = False
                        break
                        
            if (found == True and ignore == False):
                # if no meat is found set Non val to 1
                    one_hot_meat[i][d[meat]] = 1
                    found_meat = True
                    found = False
        if (found_meat == False):

            one_hot_meat[i][-1] = 1
        #print(one_hot_meat[i])
        #if sum(one_hot_meat[i]) > 2:
            #print("check this index:", i)
        
                
    file = open("one_hot_meat.csv", "w+")
    for i in range(nb_recipes):
        temp= str(one_hot_meat[i][0])
        for j in range(1, nb_target_items):
            temp+= "," + str(one_hot_meat[i][j])
        
        temp += '\n'
        file.write(temp)
        
    file.close()
    
def sort_data(file):
    # run this check to see the distrubtion in the database of meat and no meat
    f = open(file, "r")
    l = f.readlines()
    f.close()
    one_hot = []
    for item in l:
        temp = item.strip('\n')
        temp = temp.split(',')
        one_hot.append(temp)
        
    nb_meat = 0
    nb_no_meat = 0
    n = len(one_hot)
    for i in range(2500,3000):
        row = one_hot[i]
        if nb_meat < 10:
            print(row)
        if row[-1] == "1":
            nb_no_meat += 1
        else:
            nb_meat += 1
            
    print("There are", nb_no_meat, "recpies without meat")
    print("There are", nb_meat, "recpies with some meat")
        
    
    
def main():
    run_meat = False
    #run_veg = 
    if (run_meat):
        meat_exclusion_list = ['beef consomme', 'beef stock', 'beef tomato', 'chicken soup', 'chicken stock', 'fish sauce', 'lamb stock', 'oyster mushroom', 'oyster sauce', 'sirlion', 'steak']
        meat_list = ['beef', 'chicken', 'crab','eel', 'fish', 'lamb', 'oyster', 'pork', 'salmon', 'turkey', 'veal', "No Meat"]
        one_hot_meat(meat_list, meat_exclusion_list)
    #ohmf = one_hot_meat_file
    ohmf = "one_hot_meat.csv"
    sort_data(ohmf)
    
    
main()
