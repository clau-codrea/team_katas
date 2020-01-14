import collections

def pairing(a):
    dic = {}
    for string in a:
        split_string = string.split()
        dic[split_string[0]] = int(split_string[1])

    return dic

def stock_list(b, c):
    string = ""

    if b and c:
        pairs = pairing(b)
    
        dic_1 = {}
    
        for elem in c:
            dic_1[elem] = 0
            for key, value in pairs.items():
                if key[0] == elem:
                    dic_1[elem] = dic_1[elem] + value
    
    
        for key, value in dic_1.items():
            string = string + "(" + key + " : " + str(value) + ") - "
        string = string[:-3]
       
    return string
