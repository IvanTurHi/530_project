## проверка какие самолеты нашлись а какие нет
import requests
import datetime
import json

def chek_requests():
    f = open("fligth_links_today.txt", 'r')
    list_of_links = []
    for i in f:
        list_of_links.append(i[:-1])
    print(list_of_links)
    print(len(list_of_links))
    kk = 0
    count_of_good_r = 0
    count_of_bad_r = 0
    #bs = 'https://ru.flightaware.com/live/flight/LO4471'
    #gs = 'https://ru.flightaware.com/live/flight/AFL1222'
    #res = requests.get(gs)
    #print(res.text)
    list_of_bad_links = []
    list_of_good_links = []
    for i in list_of_links:
        res = requests.get(i)
        kk += 1
        print(kk)
        #print(res.text)
        #print(res.url)
        #print(res.text)
        #if 'FlightAware не удалось найти данных для отслеживания рейса' in res.text:
        if 'INVALID' in res.url:
            count_of_bad_r += 1
            list_of_bad_links.append(i)
        else:
            count_of_good_r += 1
            list_of_good_links.append(i)

    print('total_count', count_of_good_r+count_of_bad_r)
    print('count_of_good_r',count_of_good_r)
    print('count_of_bad_r',count_of_bad_r)

    good_f = open('good_f_links.txt', 'w')
    for ii in list_of_good_links:
        good_f.write(ii + '\n')
    good_f.close()

    bad_f = open('bad_f_links.txt', 'w')
    for ii in list_of_bad_links:
        bad_f.write(ii + '\n')
    bad_f.close()

    f.close()

    return (count_of_good_r+count_of_bad_r, count_of_good_r, count_of_bad_r)


## поиск левых рабоичх ссылок
def chek_true_but_old():
    #f = open("good_f_links.txt",'r')
    #list_of_links = []
    #for i in f:
    #    list_of_links.append(i[39:-1])
    ##print(list_of_links)
    #for i in range(len(list_of_links)):
    #    list_of_links[i] = list_of_links[i][:3]
    ##print(list_of_links)
    ##print(list(list_of_links[0]))
    #count_of_wrong_flights = 0
    #list_of_numbers = ['0','1','3','4','5','6','7','8','9']
    #for j in range(len(list_of_links)):
    #    for i in list(list_of_links[j]):
    #        if i in list_of_numbers:
    #            count_of_wrong_flights += 1
    #            print(list_of_links[j])
    #print("количество самолетов которые нашлись но нам не подходят по времени", count_of_wrong_flights)
    #return count_of_wrong_flights


    f = open("good_f_links.txt",'r')
    list_of_links = []
    for i in f:
       list_of_links.append(i[39:-1])
    len_good = len(list_of_links)
    f1 = open('./phaetonalfa_data_today/flights_data.json', 'r', encoding='utf-8')
    js_d = json.load(f1)
    js_len = len(js_d)

    #list_of_tru_f = []
    #for i in range(len(js_d)):
    #    list_of_tru_f.append(js_d[i]['url'][39:])
    #left_f = 0
    #for i in list_of_links:
    #    if i not in list_of_tru_f:
    #        left_f += 1
    #        print('https://ru.flightaware.com/live/flight/' + i)
    #print('Левые самолеты', left_f)

    print('Левые самолеты', len_good - js_len)
    return len_good - js_len


## вычленение самолетов которые не перевелись по системам
def chek_wrong_translate():
    f = open("bad_f_links.txt",'r')
    list_of_links = []
    for i in f:
        list_of_links.append(i[39:-1])
    print(list_of_links)
    f1 = open("list_of_bad_flights.txt",'w')
    for ii in list_of_links:
        f1.write(ii + '\n')
    f1.close()
    for i in range(len(list_of_links)):
        list_of_links[i] = list_of_links[i][:2]
    #print(list_of_links)
    #print(len(list_of_links))
    unicum = set(list_of_links)
    print('префиксы самолетов, который не перевелись по системам', unicum)
    #print(len(unicum))
    f.close()
    f2 = open("unicum_cod.txt",'w')
    for ii in unicum:
        f2.write(ii + '\n')
    f2.close()
    return unicum

def get_total_stat(num,wrong,uni):
    items = {}
    t2 = datetime.date.today()
    t3 = datetime.timedelta(days=1)
    time_I = (t2 - t3).strftime('%d.%m.%Y')
    file_new_name_problem = "./Stats/" + time_I + ".json"
    file_new_for_problem = open(file_new_name_problem, mode='w', encoding='utf-8')
    today_file = open('./Stats/today.json', 'w', encoding='utf-8')
    items['total_count'] = num[0]
    items['good_count'] = num[1]
    items['bad_count'] = num[2]
    items['find_but_bad'] = wrong
    items['percentage_of_good'] = (num[1] - wrong) * 100 / num[0]
    items['unfindable_marks'] = list(uni)
    json.dump(items, file_new_for_problem, ensure_ascii=False)
    json.dump(items, today_file, ensure_ascii=False)
    file_new_for_problem.close()
    today_file.close()




num = chek_requests()
wrong = chek_true_but_old()
uni = chek_wrong_translate()
get_total_stat(num, wrong, uni)
