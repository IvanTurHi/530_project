import json
from os import listdir
from pymongo import MongoClient

file_debug = open("Push_II_debug.txt", mode='w', encoding='utf-8')
file_debug.close()

#----------- Получение имен файлов ----------
files = listdir(".")

x = []
i = 0
while i < len(files):
    if files[i].find('.json') != -1:
        x.append(files[i])
        del files[i]
    else:
        i += 1

print(x)

#----------- Запись в MongoDB ----------
client = MongoClient('localhost', 27017)
print(client)
db = client['flights_today']
print(db)
collection_currency = db['flights']
print(collection_currency)
print(1)
for i in collection_currency.find():
    print(i, end='\n')

y = collection_currency.drop()
print(y)

k = 0
i = 0
while i < len(x):
    try:
        with open(x[i]) as f:
            file_data = json.load(f)
        collection_currency.insert_one(file_data)

    except BaseException:
       k += 1
       print(k)
    i += 1

#print(1)
#for i in collection_currency.find():
#    print(i, end='\n')

client.close()

file_debug = open("Push_II_debug.txt", mode='w', encoding='utf-8')
file_debug.write("Working well")
file_debug.close()
