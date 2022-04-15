from os import listdir
import json
import psycopg2
import re
import matplotlib.pyplot as plt


path = r"C:\Users\gev46\Desktop\Проект\1"

def total_emission():
    k = 0
    pas = r"C:\Users\gev46\PycharmProjects\Gleb_projects\filter_II\Flight_today_new"
    icao_to_comp = get_companies_emissions()
    total_emission_value = 0
    total_kilometers = 0
    list_of_companies = []
    dict_of_companies = {}
    list_ofairports = []
    dict_of_airports = {}
    files = listdir(pas)
    domestic = 0
    forejen = 0
    code_to_country = dom_for_flights()
    total_number_of_flights = 0

    for i in files:
        with open(pas+r"\\"+i, encoding='utf-8') as json_file:
            try:
                js_ob = json.load(json_file)
            except BaseException:
                k += 1
            list_of_rounds = js_ob['Way']['flights']['rounds']
            flight_name = js_ob['Way']['flights']['flightname']
            departure_airport = js_ob['Way']['from']
            arrival_airport = js_ob['Way']['to']

            flight_name = flight_name[0:3]
            while re.search('[0-9]', flight_name):
                flight_name = flight_name[:-1]
            try:
                flight_company = icao_to_comp[flight_name]
            except KeyError:
                print(flight_name)
                flight_company = "unnamed_company"

            if flight_company not in list_of_companies:
                list_of_companies.append(flight_company)
                dict_of_companies[flight_company] = {"emissions": 0, "kilometers": 0, "total number of flights": 0}

            if departure_airport not in list_ofairports:
                list_ofairports.append(departure_airport)
                dict_of_airports[departure_airport] = {"departure": 0, "arrival": 0}
            if arrival_airport not in list_ofairports:
                list_ofairports.append(arrival_airport)
                dict_of_airports[arrival_airport] = {"departure": 0, "arrival": 0}



            for i in list_of_rounds:
                total_emission_value += i['totalemissionsmax']
                total_kilometers += i["km"]
                dict_of_companies[flight_company]["emissions"] += i['totalemissionsmax']
                dict_of_companies[flight_company]["kilometers"] += i["km"]
                dict_of_companies[flight_company]["total number of flights"] += 1
                dict_of_airports[departure_airport]["departure"] += 1
                dict_of_airports[arrival_airport]["arrival"] += 1
                try:
                    if code_to_country[departure_airport] == "Россия" and code_to_country[arrival_airport] == "Россия":
                        domestic += 1
                    else:
                        forejen += 1
                except KeyError:
                    forejen += 1
                total_number_of_flights += 1
                #print(i['totalemissionsmax'])




            json_file.close()
    #print(k)
    return total_emission_value, total_kilometers, dict_of_companies, dict_of_airports, domestic, forejen, total_number_of_flights

def get_companies_emissions():
    conn = psycopg2.connect(database="IATA_to_ICAO", user='postgres',
                            password='YUV45G', host='localhost', port=5432)

    cur = conn.cursor()

    cur.execute("select icao, compname from dictionary1")

    icao_to_comp = {}

    for i in cur:
        icao_to_comp[i[0]] = i[1]

    conn.close()
    return icao_to_comp

    #выгрузка из бд в формате iata-icao-company
    #cur.execute("select * from dictionary1")
    #f = open("sex_with_name.txt", 'w')
    #for i in cur:
    #    f.write(i[0]+" ")
    #    f.write(i[1] + " ")
    #    f.write(i[2] + "\n")
    #f.close()

def translate_iata_ro_air(dict_of_airports):
    conn = psycopg2.connect(database="IATA_to_ICAO", user='postgres',
                            password='YUV45G', host='localhost', port=5432)

    cur = conn.cursor()
    cur.execute("select * from air_to_iata")

    tru_names = {}
    d_air_to_iata = {}
    for i in cur:
        if i[1] != "No data":
            d_air_to_iata[i[1]] = i[0]



    for i in dict_of_airports:
        if i in d_air_to_iata:
            tru_names[d_air_to_iata[i]] = dict_of_airports[i]
        else:
            tru_names[i] = dict_of_airports[i]

    conn.close()
    return tru_names

def write_data(total_emission_value, total_kilometrs, dict_of_companies, dict_of_airports, domestic, forejen, total_number_of_flights):
    f = open("statistic.json", mode='w', encoding='utf-8')
    data_for_writing = {
        "total emissions": total_emission_value,
        "total kilometers": total_kilometrs,
        "total number of flights": total_number_of_flights,
        "number of domestic flights": domestic,
        "number of foreign flights": forejen,
        "percentage of domestic flights": domestic/total_number_of_flights * 100,
        "companies": dict_of_companies,
        "airports": dict_of_airports
    }
    json.dump(data_for_writing,  f)
    f.close()


def get_number_of_planes():
    files = listdir(path)
    list_of_dates = []
    list_of_count = []
    for i in files:
        if "2022" in i:
            if "02.2022" not in i:
                with open(path + r"\\" + i, encoding='utf-8') as json_file:
                    # with open('../phaetonalfa/phaetonalfa_data_today/flights_data.json', encoding='utf-8') as json_file:
                    print(i)
                    list_of_dates.append(int(i[0:2]))
                    all_air = json.load(json_file)
                    list_of_count.append(len(all_air))
    #files.sort()
    #print(files)
    print(list_of_dates)
    print(list_of_count)
    return list_of_dates, list_of_count

def draw(list_of_dates, list_of_count):
    fig = plt.figure()
    plt.plot(list_of_dates, list_of_count)
    plt.show()

def raspredelenie_kilometraja():
    files = listdir(path)
    dict_of_kilometers = {}
    for i in files:
        if "2022" in i:
            with open(path + r"\\" + i, encoding='utf-8') as json_file:
                print(i)
                all_air = json.load(json_file)
                for i in all_air:
                    if i["direct_distance"] in dict_of_kilometers:
                        dict_of_kilometers[i["direct_distance"]] += 1
                    else:
                        dict_of_kilometers[i["direct_distance"]] = 1
    return dict_of_kilometers

def draw_kilometers(dict_of_kilometers):
    fig = plt.figure()
    x = []
    y = []
    delta = 150
    d = {}
    min_kilo = 150
    group_dict = {}
    for i in dict_of_kilometers:
        if i[0] >= min_kilo + delta:
            min_kilo += delta
        if "{}-{}".format(min_kilo, min_kilo + delta) in group_dict:
            group_dict["{}-{}".format(min_kilo, min_kilo + delta)] += i[1]
        else:
            group_dict["{}-{}".format(min_kilo, min_kilo + delta)] = i[1]
    a = list(group_dict.keys())
    b = list(group_dict.values())
    plt.barh(a, b)
    plt.show()

def dom_for_flights():
    conn = psycopg2.connect(database="IATA_to_ICAO", user='postgres',
                            password='YUV45G', host='localhost', port=5432)

    cur = conn.cursor()
    cur.execute("select iata, country from air_to_iata")

    code_to_country = {}

    for i in cur:
        code_to_country[i[0]] = i[1]

    conn.close()
    return code_to_country

# ======== получение общей статистики, статистики по авиакомпаниям и аэропортам ========
total_emission_value, total_kilometrs, dict_of_companies, dict_of_airports, domestic, forejen, total_number_of_flights = total_emission()
tru_names = translate_iata_ro_air(dict_of_airports)
write_data(total_emission_value, total_kilometrs, dict_of_companies, tru_names, domestic, forejen, total_number_of_flights)


# ======= получение количества рейсов в месяц ==========
#list_of_dates, list_of_count = get_number_of_planes()
#draw(list_of_dates, list_of_count)


# ========= получение среднего километража ==========
#dict_of_kilometers = raspredelenie_kilometraja()
#dict_of_kilometers = sorted(dict_of_kilometers.items(), key=lambda x: x[0])
#draw_kilometers(dict_of_ilometers)
