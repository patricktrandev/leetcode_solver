s='MCMXCIV'
dict_roman= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def solveRomanToInteger(s):
    num=0
    for i in range(len(s)-1):     
        if dict_roman.get(s[i])<dict_roman.get(s[i+1]):
            num-=dict_roman.get(s[i])
        else:
            num+=dict_roman.get(s[i])

    return num+dict_roman.get(s[-1])

test=solveRomanToInteger(s)
print(test)

def solveRomanToInteger2(s):
    num=0
    for i in range(len(s)-1,-1,-1):
    
            
        if i <len(s)-1 and dict_roman.get(s[i]) < dict_roman.get(s[i+1]):
        
            num= num-dict_roman.get(s[i])
            continue
        if len(s)==2 and i==0 and dict_roman.get(s[i]) < dict_roman.get(s[i+1]):
            num= num-dict_roman.get(s[i])
            continue
        num+=dict_roman.get(s[i])
    return num

test2=solveRomanToInteger2(s)
print(test2)