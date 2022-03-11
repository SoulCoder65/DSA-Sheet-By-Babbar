def printDuplicate(string):
    string_dict={}
    for item in string:
        if item not in string_dict.keys():
            string_dict[item]=1
        else:
            string_dict[item]+=1
    #  Filter letter occur more than 1
    filter_dict={k:v for (k,v) in string_dict.items() if v>1}

    return filter_dict

string="test string"

print(printDuplicate(string))