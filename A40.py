def dict_sort(x):
    list = sorted(x.items(), key=lambda x: x[1])
    return list

    
dict1={ "Japan" : 100, "China" : 50, "Australia" : 75 } 
dict2={ "Korea" : 100, "Switzerland" : 50, "Zurich" : 75 } 
dict3={ "USA" : 100, "Turkey" : 50, "Portugal" : 75 } 
dict4={ "Italy" : 100, "Belgium" : 50, "the United Kingdom" : 75 } 
print(type(dict_sort(dict1)))
print(dict_sort(dict2))
print(dict_sort(dict3))
print(dict_sort(dict4))
