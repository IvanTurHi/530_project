import os
import time
import datetime
from os import listdir
import sys

print(sys.version)
#print("SSSSSSSSSSSEEEEEEEEEEEEEEEEEEEEEEEEEXXXXXXXXXXXXXXXX")
#print(os.getcwd())
#os.chdir("../home/Ivan/Gleb_projects")
#print(os.getcwd())

#----------- Время сегодня в данный момент сейчас ----------
Time_start = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
file_All_Debug = open("./All_Debug.txt", "a+", encoding='utf-8')
file_All_Debug.write(Time_start + " --- START ---" + "\n")
file_All_Debug.close()

#----------- phaeton phaeton phaeton phaeton phaeton ----------
#----------- Таймер время работы phaeton ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_phaeton = datetime.time(3, 0, 0).strftime("%H:%M:%S") # ---------- Установка на 03:00:00 минут
print(Time_right_now)

#----------- Таймер на запуск phaeton ----------
while Time_right_now < Time_for_phaeton:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск phaeton ----------
path = './phaeton/'
os.chdir(path)
cmd = 'scrapy crawl phaeton' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 90 секунд

#----------- Проверка phaeton (today.json) ----------
Time_right_now_phaeton = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = './phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
x = f1.read()
f1.close()

if len(x) != 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_phaeton + " - phaeton - work" + "\n")
    file_All_Debug.close()
    print("phaeton - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_phaeton + " - phaeton - not work" + "\n")
    file_All_Debug.close()
    print("phaeton - not work")

#----------- pashkovskey pashkovskey pashkovskey pashkovskey pashkovskey ----------
#----------- Таймер время работы pashkovskey ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_pashkovskey= datetime.time(4, 0, 0).strftime("%H:%M:%S") # ---------- Установка на 4:00:00 минут
print(Time_right_now)

#----------- Таймер на запуск Koltsovo ----------
while Time_right_now < Time_for_pashkovskey:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск pashkovskey ----------
path = '../pashkovskey/'
os.chdir(path)
#cmd = 'scrapy crawl pashka' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка pashka (today.json) ----------
Time_right_now_pashka = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
pashka_x = f1.read()
f1.close()

if len(pashka_x) != len(x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_pashka + " - pashka - work" + "\n")
    file_All_Debug.close()
    print("pashka - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_pashka+ " - pashka - not work" + "\n")
    file_All_Debug.close()
    print("pashka - not work")


#----------- tolmachevo tolmachevo tolmachevo tolmachevo tolmachevo ----------
#----------- Таймер время работы tolmachevo ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_tolmachevo = datetime.time(19, 28, 0).strftime("%H:%M:%S") # ---------- Установка на 19:58:00 минут
print(Time_right_now)

#----------- Таймер на запуск tolmachevo ----------
while Time_right_now < Time_for_tolmachevo:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск tolmachevo ----------
path = '../Tolmachovo/'
os.chdir(path)
cmd = 'scrapy crawl Tolmach' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка Tolmach (today.json) ----------
Time_right_now_Tolmach = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
print(os.getcwd())
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
Tolmach_x = f1.read()
f1.close()

if len(Tolmach_x) != len(pashka_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Tolmach + " - Tolmach - work" + "\n")
    file_All_Debug.close()
    print("Tolmach - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Tolmach + " - Tolmach - not work" + "\n")
    file_All_Debug.close()
    print("Tolmach - not work")


#----------- Koltsovo Koltsovo Koltsovo Koltsovo Koltsovo ----------
#----------- Таймер время работы Koltsovo ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_Koltsovo= datetime.time(21, 55, 0).strftime("%H:%M:%S") # ---------- Установка на 21:55:00 минут
print(Time_right_now)

#----------- Таймер на запуск Koltsovo ----------
while Time_right_now < Time_for_Koltsovo:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск tolmachevo ----------
path = '../scrapyKolcovo/'
os.chdir(path)
cmd = 'scrapy crawl Kol' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка Kol (today.json) ----------
Time_right_now_Kol = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
Kol_x = f1.read()
f1.close()

if len(Tolmach_x) != len(Kol_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Kol + " - Kol - work" + "\n")
    file_All_Debug.close()
    print("Kol - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Tolmach + " - Kol - not work" + "\n")
    file_All_Debug.close()
    print("Kol - not work")





#----------- sharik sharik sharik sharik sharik ----------
#----------- Таймер время работы sharik ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_sharik = datetime.time(23, 50, 0).strftime("%H:%M:%S") # ---------- Установка на 23:50:00 минут
print(Time_right_now)

#----------- Таймер на запуск sharik ----------
while Time_right_now < Time_for_sharik :
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск sheremet ----------
path = '../sharik/'
os.chdir(path)
cmd = 'scrapy crawl sheremet' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка sharik (today.json) ----------
Time_right_now_psharik = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
sh_x = f1.read()
f1.close()

if len(sh_x) != len(Kol_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_psharik + " - sharik - work" + "\n")
    file_All_Debug.close()
    print("sharik - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_phaeton + " - sharik - not work" + "\n")
    file_All_Debug.close()
    print("sharik - not work")


#----------- vnukovo vnukovo vnukovo vnukovo vnukovo ----------
#----------- Таймер время работы vnukovo ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_vnukovo = datetime.time(23, 51, 0).strftime("%H:%M:%S") # ---------- Установка на 23:51:00 минут
print(Time_right_now)

#----------- Таймер на запуск vnukovo ----------
while Time_right_now < Time_for_vnukovo:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск vnuk ----------
path = '../vnukovo/'
os.chdir(path)
cmd = 'scrapy crawl vnuk' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка vnukovo (today.json) ----------
Time_right_now_vnukovo = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
vnuk_x = f1.read()
f1.close()

if len(vnuk_x) != len(sh_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_vnukovo + " - vnuk - work" + "\n")
    file_All_Debug.close()
    print("vnuk - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_vnukovo + " - vnuk - not work" + "\n")
    file_All_Debug.close()
    print("vnuk - not work")

#----------- pulkovo pulkovo pulkovo pulkovo pulkovo ----------
#----------- Таймер время работы pulkovo ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_pulkovo = datetime.time(23, 52, 0).strftime("%H:%M:%S") # ---------- Установка на 23:52:00 минут
print(Time_right_now)

#----------- Таймер на запуск pulkovo ----------
while Time_right_now < Time_for_pulkovo:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск pulkovo ----------
path = '../pulkovo/'
os.chdir(path)
cmd = 'scrapy crawl spbpul' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка spbpul (today.json) ----------
Time_right_now_pulkovo = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
spbp_x = f1.read()
f1.close()

if len(spbp_x) != len(vnuk_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_pulkovo + " - spbpul - work" + "\n")
    file_All_Debug.close()
    print("spbpul - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_pulkovo + " - spbpul - not work" + "\n")
    file_All_Debug.close()
    print("spbpul - not work")
time.sleep(600)

# -----------------------------------------------
#----------- domodevo domodevo domodevo domodevo domodevo ----------
#----------- Таймер время работы domodevo ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_domodevo = datetime.time(0, 30, 0).strftime("%H:%M:%S") # ---------- Установка на 0:30:00 минут
print(Time_right_now)

#----------- Таймер на запуск domodevo ----------
while Time_right_now < Time_for_domodevo:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
    # print("Сейчас :", Time_right_now)

#----------- Запуск domodevo ----------
path = '../Domodedovo/'
os.chdir(path)
cmd = 'scrapy crawl Dom' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
#os.startfile('../Domodedovo/F1.py')
os.system('python3 ../Domodedovo/F1.py')
time.sleep(20) # ---------- Задержка на 20 секунд

#----------- Проверка Dom (today.json) ----------
Time_right_now_domodevo = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaeton = '../phaeton/phaeton_data_today/today.json'
f0 = open(file_phaeton, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaeton, mode='r', encoding='utf-8')
DOM_x = f1.read()
f1.close()

if len(DOM_x) != len(spbp_x):
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_domodevo + " - DOM - work" + "\n")
    file_All_Debug.close()
    print("DOM - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_domodevo + " - DOM - not work" + "\n")
    file_All_Debug.close()
    print("DOM - not work")




# -----------------------------------------------


#----------- Spisok_test.py Spisok_test.py Spisok_test.py Spisok_test.py Spisok_test.py ----------
#----------- Таймер время работы Spisok_test.py ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_Spisok_test = datetime.time(0, 31, 0).strftime("%H:%M:%S") # ---------- Установка на 0:31:00 минут
print(Time_right_now)

#----------- Таймер на запуск Spisok_test.py ----------
while Time_right_now < Time_for_Spisok_test:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

#----------- Запуск Spisok_test.py ----------
path = '../filter_I/'
os.chdir(path)
#os.startfile('Spisok_test.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system('python3 Spisok_test.py')
time.sleep(30) # ---------- Задержка на 30 секунд

#----------- Проверка Spisok_test.py (Spisok_debug.txt) ----------
Time_right_now_Spisok_test = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_Spisok_test = './Spisok_debug.txt'
f0 = open(file_Spisok_test, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_Spisok_test, mode='r', encoding='utf-8')
x = f1.read()
f1.close()

if len(x) != 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Spisok_test + " - Spisok_test - work" + "\n")
    file_All_Debug.close()
    print("Spisok_test - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Spisok_test + " - Spisok_test - not work" + "\n")
    file_All_Debug.close()
    print("Spisok_test - not work")

#----------- Flights_new Flights_new Flights_new Flights_new Flights_new----------
#----------- Таймер время работы flights_new ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_flights_new = datetime.time(0, 32, 0).strftime("%H:%M:%S") # ---------- Установка на 0:32:00 минут
print(Time_right_now)

#----------- Таймер на запуск Flights_new ----------
while Time_right_now < Time_for_flights_new:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

path = '../translating/'
os.chdir(path)
#os.startfile('Flights_new.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system('python3 Flights_new.py')
time.sleep(10) # ---------- Задержка на 10 секунд


#----------- phaetonalfa phaetonalfa phaetonalfa phaetonalfa phaetonalfa ----------
#----------- Таймер время работы phaetonalfa ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_phaetonalfa = datetime.time(0, 33, 0).strftime("%H:%M:%S") # ---------- Установка на 0:33:00 минут
print(Time_right_now)

#----------- Таймер на запуск phaetonalfa ----------
while Time_right_now < Time_for_phaetonalfa:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

#----------- Запуск phaetonalfa ----------
path = '../phaetonalfa/'
os.chdir(path)
cmd = 'scrapy crawl phaetonalfa' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system(cmd)
time.sleep(30) # ---------- Задержка на 30 секунд

#----------- Проверка phaetonalfa (today.json) ----------
Time_right_now_phaetonalfa = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaetonalfa = './phaetonalfa_data_today/flights_data.json'
f0 = open(file_phaetonalfa, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaetonalfa, mode='r', encoding='utf-8')
x = f1.read()
f1.close()

if len(x) != 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_phaetonalfa + " - phaetonalfa - work" + "\n")
    file_All_Debug.close()
    print("phaetonalfa - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_phaetonalfa + " - phaetonalfa - not work" + "\n")
    file_All_Debug.close()
    print("phaetonalfa - not work")

#----------- test_crawling_with_requests test_crawling_with_requests test_crawling_with_requests ----------
#----------- Таймер время работы test_crawling_with_requests ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_test_crawling_with_requests = datetime.time(0, 40, 0).strftime("%H:%M:%S") # ---------- Установка на 00:40:00 минут
print(Time_right_now)

while Time_right_now < Time_for_test_crawling_with_requests:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

path = '../phaetonalfa/'
os.chdir(path)
#os.startfile('test_crawling_with_requests.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
os.system('python3 test_crawling_with_requests.py')
time.sleep(30)

#----------- Проверка test_crawling_with_requests (today.json) ----------
Time_right_now_test_crawling_with_requests = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_phaetonalfa = './Stats/today.json'
f0 = open(file_phaetonalfa, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_phaetonalfa, mode='r', encoding='utf-8')
x = f1.read()
f1.close()

if len(x) != 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_test_crawling_with_requests + " - test_crawling_with_requests - work" + "\n")
    file_All_Debug.close()
    print("test_crawling_with_requests - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_test_crawling_with_requests + " - test_crawling_with_requests - not work" + "\n")
    file_All_Debug.close()
    print("test_crawling_with_requests - not work")


#----------- filter_new_v5.py filter_new_v5.py filter_new_v5.py filter_new_v5.py filter_new_v5.py ----------
#----------- Таймер время работы filter_new_v5.py ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_filter_new_v5 = datetime.time(2, 45, 0).strftime("%H:%M:%S") # ---------- Установка на 02:45:00 минут
print(Time_right_now)

#----------- Таймер на запуск filter_new_v5.py ----------
while Time_right_now < Time_for_filter_new_v5:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

#----------- Проверка filter_new_v5.py (Error_debug) ----------
path = '../filter_II/Error_debug/'
os.chdir(path)
k1 = listdir(".")
k = len(k1)
path = '..'
os.chdir(path)
time.sleep(5)

#----------- Запуск filter_new_v5.py ----------
os.startfile('filter_II_new_v5.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
time.sleep(30) # ---------- Задержка на 30 минут

#----------- Проверка filter_new_v5.py (Filter_II_debug) ----------
Time_right_now_filter_new_v5 = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

path = './Error_debug/'
os.chdir(path)
y = listdir(".")
path = '..'
os.chdir(path)
# print(y)

file_filter_new = './Filter_II_debug.txt'
f0 = open(file_filter_new, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_filter_new, mode='r', encoding='utf-8')
z = f1.read()
f1.close()

if len(y) > k:
    k +=1
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_filter_new_v5 + " - filter_new_v5 - error_in_debug" + "\n")
    file_All_Debug.close()
    print("filter_new_v5 - error_in_debug")
elif len(z) == 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_filter_new_v5 + " - filter_new_v5 - not work" + "\n")
    file_All_Debug.close()
    print("filter_new_v5 - not work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_filter_new_v5 + " - filter_new_v5 - work" + "\n")
    file_All_Debug.close()
    print("filter_new_v5 - work")


#----------- Push_II.py Push_II.py Push_II.py Push_II.py Push_II.py ----------
#----------- Таймер время работы Push_II.py ----------
Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
Time_for_Push_II = datetime.time(2, 50, 0).strftime("%H:%M:%S") # ---------- Установка на 02:50:00 минут

#----------- Таймер на запуск Push_II.py ----------
while Time_right_now < Time_for_Push_II:
    time.sleep(20)
    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")

#----------- Запуск Push_II.py ----------
path = '../filter_II/Flight_today_new'
os.chdir(path)
os.startfile('Push_II.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
time.sleep(300) # ---------- Задержка на 5 минут

#----------- Проверка Push_II.py (Push_II_debug.txt) ----------
Time_right_now_Push_II = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

file_Push = './Push_II_debug.txt'
f0 = open(file_Push, mode='a+', encoding='utf-8')
f0.close()
f1 = open(file_Push, mode='r', encoding='utf-8')
x = f1.read()
f1.close()

path = '..'
os.chdir(path)

if len(x) != 0:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Push_II + " - Push_II - work" + "\n")
    file_All_Debug.close()
    print("Push_II - work")
else:
    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
    file_All_Debug.write(Time_right_now_Push_II + " - Push_II - not work" + "\n")
    file_All_Debug.close()
    print("Push_II - not work")
#
##----------- phaetonbravo phaetonbravo phaetonbravo phaetonbravo phaetonbravo ----------
##----------- Таймер время работы phaetonbravo ----------
#Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
#Time_for_phaetonbravo = datetime.time(1, 30, 0).strftime("%H:%M:%S") # ---------- Установка на 01:30:00 минут
## print(Time_right_now)
#
## ----------- Дата запуска phaetonbravo ----------
#Time_right_now = datetime.datetime.now().strftime('%d')
## ----------- День запуска phaetonbravo ----------
#if Time_right_now == "1" :
#    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
#    Time_for_phaetonbravo_print = datetime.datetime.now().strftime("%H:%M:%S")
#    # ----------- Таймер на запуск phaetonbravo ----------
#    while Time_right_now < Time_for_phaetonbravo:
#        time.sleep(20)
#        Time_right_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
#        path = '../phaetonbravo/'
#        os.chdir(path)
#        cmd = 'scrapy crawl phaetonbravo' #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
#        os.system(cmd)
#        file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
#        file_All_Debug.write(Time_for_phaetonbravo_print + " - phaetonbravo - work" + "\n")
#        file_All_Debug.close()
#        print("phaetonbravo - work")
#else:
#    Time_for_phaetonbravo_print = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
#    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
#    file_All_Debug.write(Time_for_phaetonbravo_print + " - phaetonbravo - not work" + "\n")
#    file_All_Debug.close()
#    print("phaetonbravo - not work")
#time.sleep(1800)  # ---------- Задержка на 30 минут
#
##----------- filter.py filter.py filter.py filter.py filter.py ----------
##----------- Таймер время работы filter.py ----------
#Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
#Time_for_filter = datetime.time(2, 0, 0).strftime("%H:%M:%S") # ---------- Установка на 02:00:00 минут
#print(Time_right_now)
#
## ----------- Дата запуска filter ----------
#Time_right_now = datetime.datetime.now().strftime('%d')
#
#path = '../filter_III/'
#os.chdir(path)
#file_filter = './Filter_debug.txt'
#f0 = open(file_filter, mode='w', encoding='utf-8')
#f0.close()
#
## ----------- Таймер на запуск phaetonbravo ----------
#if Time_right_now == "1" :
#    #----------- Таймер на запуск filter.py ----------
#    Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
#    while Time_right_now < Time_for_filter:
#        time.sleep(20)
#        Time_right_now = datetime.datetime.now().strftime("%H:%M:%S")
#        path = '../filter_III/'
#        os.chdir(path)
#        os.startfile('filter.py') #ОООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО
#    else:
#        print()
#
##----------- Проверка filter.py (Filter_debug.txt) ----------
#Time_right_now_filter = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
#
#path = '../filter_III/'
#os.chdir(path)
#file_filter = './Filter_debug.txt'
#f0 = open(file_filter, mode='a+', encoding='utf-8')
#f0.close()
#f1 = open(file_filter, mode='r', encoding='utf-8')
#x = f1.read()
#f1.close()
#
#if len(x) != 0:
#    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
#    file_All_Debug.write(Time_right_now_Spisok_test + " - filter - work" + "\n")
#    file_All_Debug.close()
#    print("filter - work")
#else:
#    file_All_Debug = open("../All_Debug.txt", "a+", encoding='utf-8')
#    file_All_Debug.write(Time_right_now_Spisok_test + " - filter - not work" + "\n")
#    file_All_Debug.close()
#    print("filter - not work")
#time.sleep(1800)  # ---------- Задержка на 30 минут
#
