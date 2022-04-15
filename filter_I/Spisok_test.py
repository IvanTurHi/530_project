import json
import re

f1_name = "../phaeton/phaeton_data_today/today.json"
f1 = open(f1_name, mode='r', encoding='utf-8')

file_j = open('all_fligth_today.json', "w", encoding='utf-8')
file_j.close()

file_debug = open("Spisok_debug.txt", mode='w', encoding='utf-8')
file_debug.close()

Garbage1 = []
Garbage2 = []


# --------------------- Удалить отмененые рейсы ---------------------
day_json_data = json.load(f1)
for user in day_json_data:
    Status = user['status']
    Flight = user['flight']
    z = len(Status)
    i = 0
    while i < len(Status):
        if Status[i] != None:
            if 'тменен' in Status[i]:
                Garbage1.append(Status[i])
                Garbage2.append(Flight[i])
                del Status[i]
                del Flight[i]
            else:
                i += 1
        else:
            i += 1

    file_json = open('all_fligth_today.json', "a", encoding='utf-8')
    file_list = Flight
    json.dump(file_list, file_json)
    file_json.close()

#подсчитываем сколько осталось после удаления
file_json = open('all_fligth_today.json', "r", encoding='utf-8')
line = file_json.readline()
list_of_line = list(line.split(','))
print('Количество после удаления отмененных', len(list_of_line))
file_json.close()

# --------------------- Удалить пустые массивы, пробелы и тире в рейсах ---------------------
with open('all_fligth_today.json', "r", encoding='utf-8') as f:
  old_data = f.read()
n1_data = old_data.replace('[]', '')
n2_data = n1_data.replace('][', ', ')
n3_data = n2_data.replace(' ', '')
new_data = n3_data.replace('-', '')
with open('all_fligth_today.json', "w", encoding='utf-8') as f:
  f.write(new_data)

# --------------------- Удалить повторяемые рейсы ---------------------
f2 = open('all_fligth_today.json', mode='r', encoding='utf-8')
day_j_data = json.load(f2)
b = []
for v in day_j_data:
   if v not in b:
        b.append(v)

file_json = open('all_fligth_today.json', "w", encoding='utf-8')
file_list = b
r = re.compile("[а-яА-Я]+") # регулярное выражение для Русского языка
russian = [w for w in filter(r.match, file_list)] # проверка массива на Русский язык
result = list(set(file_list) - set(russian)) # извличение Русского языка
json.dump(result, file_json)
file_json.close()

#еще раз посчитаем
file_json = open('all_fligth_today.json', "r", encoding='utf-8')
line = file_json.readline()
list_of_line = list(line.split(','))
print('Количество после удаления дубликатов', len(list_of_line))
file_json.close()

# --------------------- Запись рейсов в файл для генирации ссылок для краулера II ---------------------
file_fligth_today_w_name = "fligth_today.txt"
file_fligth_today_w = open(file_fligth_today_w_name, mode='w', encoding='utf-8')
f2 = open('all_fligth_today.json', mode='r', encoding='utf-8')
day_j_data = json.load(f2)

i = 0
while i < len(day_j_data):
    file_fligth_today_w.write(day_j_data[i] + '\n')
    # print(day_j_data[i])
    i += 1
file_fligth_today_w.close()

#link = "https://ru.flightaware.com/live/flight/"
#file_fligth_links_today_w_name = "../phaetonalfa/fligth_links_today.txt"
#file_fligth_links_today_w = open(file_fligth_links_today_w_name, mode='a', encoding='utf-8')
#file_fligth_today_w = open(file_fligth_today_w_name, mode='r', encoding='utf-8')
#line = file_fligth_today_w.readline()
#for line in file_fligth_today_w:
#    z = link + line
#    file_fligth_links_today_w.write(z)
#    # print(z)
#file_fligth_links_today_w.close()
#file_fligth_today_w.close()
f1.close()
f2.close()

file_debug = open("Spisok_debug.txt", mode='w', encoding='utf-8')
file_debug.write("Working well")
file_debug.close()

