import json
import psycopg2
import db_work

conn = psycopg2.connect(database="IATA_to_ICAO", user='postgres',
                        password='YUV45G', host='localhost', port=5432)

cur = conn.cursor()

if db_work.chek_table(cur) == False:
    db_work.initialization_protocol(cur, conn)

def create_list_of_miss_names():
    f1_name = '../filter_I/fligth_today.txt'
    f1 = open(f1_name, 'r', encoding='utf-8')
    f2_name = "IATA_and_RF_to_ICAO.json"
    f2 = open(f2_name, mode='r', encoding='utf-8')
    Translate = json.load(f2)

    for user in Translate:
        Translate_name = user['IATA_and_RF_to_ICAO']

    Result_for_new_flights = []
    for line in f1:
       Result_for_new_flights.append(line[:2])
    print(Result_for_new_flights)

    list_of_unnamed = []
    for i in Result_for_new_flights:
        if i not in Translate_name:
            list_of_unnamed.append(i)
    list_of_unnamed = set(list_of_unnamed)
    f3 = open("file_of_untranslateble_names.txt", 'w')
    for i in list_of_unnamed:
        f3.write(i + '\n')

    f1.close()
    f2.close()
    f3.close()

create_list_of_miss_names()

f1_name = '../filter_I/fligth_today.txt'
f1 = open(f1_name, 'r', encoding='utf-8')
f2_name = "IATA_and_RF_to_ICAO.json"
f2 = open(f2_name, mode='r', encoding='utf-8')

Result_for_new_flights = []
for line in f1:
    Result_for_new_flights.append(line[:-1])
print(Result_for_new_flights)
print(len(Result_for_new_flights))
Flights_Line_z = len(Result_for_new_flights)

#Result_for_new_flights = json.load(f1)
Translate = json.load(f2)

# IATA to ICAO
# RF to ICAO
for user in Translate:
    Translate_name = user['IATA_and_RF_to_ICAO']
    # print(Translate_name)
    Line_z = len(Translate_name)
    # print(Line_z)

#for user in Result_for_new_flights:
#    Result_for_new_flights = user['flight']
#    print(Result_for_new_flights)
#    Flights_Line_z = len(Result_for_new_flights)
#    print(Flights_Line_z)

# print(Result_for_new_flights[3])
# O = Result_for_new_flights[3]
# x = O[0:2:1]
# print("смотри:", x)
# print(len(Result_for_new_flights[3]))

f1.close()
f2.close()

End_of_list = []
i0 = 0
while i0 < Flights_Line_z:
    O = Result_for_new_flights[i0]
    IATA_code = O[0:2:1]
    numeric_code = O[2:len(O):1]
    # print(y)
    # Поиск в словаре
    i = 0
    LO = Line_z
    ICAO_code = db_work.get_ICAO_system(cur, IATA_code)

    #while i < LO:
    #    if x == Translate_name[i]:
    #        # print(i)
    #        # print("смотри:", Translate_name[i+1])
    #        Dima = Translate_name[i+1]
    #        i = LO + 1
    #    else:
    #        i += 2
    End_of_list.append(ICAO_code + numeric_code)
    i0 += 1
print(End_of_list)
print(len(End_of_list))

f3_name = "../phaetonalfa/fligth_links_today.txt"
f3 = open(f3_name, mode='w', encoding='utf-8')
link = "https://ru.flightaware.com/live/flight/"
i1 = 0
while i1 < len(End_of_list):
    f3.write(link + End_of_list[i1] + '\n')
    i1 += 1
f3.close()

conn.close()

# scrapy crawl phaeton
# scrapy crawl phaetonalfa