import json

with open("flights_data.json", encoding="utf8") as f:
    jf = json.load(f)
num_of_good = 0
num_of_errors = 0
for i in range(len(jf)):
    try :
        l = len(jf[i]['aircraft'])
        num_of_good += 1
    except TypeError:
        num_of_errors += 1
    #print(jf[i]['aircraft'])
    #print(i)
print(num_of_good)
print(num_of_errors)