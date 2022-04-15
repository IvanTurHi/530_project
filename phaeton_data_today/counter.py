import json

with open("today.json", encoding="utf8") as f:
    jf = json.load(f)
l = 0
for i in range(len(jf)):
    l += len(jf[i]['flight'])
print(l)