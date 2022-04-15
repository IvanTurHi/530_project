import json
import psycopg2
import requests
from bs4 import BeautifulSoup


def connection(dict_of_conc):
    conn = psycopg2.connect(database="IATA_to_ICAO", user='postgres',
                            password='YUV45G', host='localhost', port=5432)

    cur = conn.cursor()

    cur.execute("create table if not exists air_to_iata"
                "("
                "airport varchar(30) primary key,"
                "iata varchar(20),"
                "country varchar(30)"
                ")")
    conn.commit()

    for i in dict_of_conc:
        try:
            cur.execute("INSERT INTO air_to_iata VALUES (%s, %s, %s)", (i, dict_of_conc[i][0], dict_of_conc[i][1]))
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            cur.execute("ROLLBACK")

    conn.close()


def parse():
    url = "https://aviateka.su/kody-aeroportov-iata-icao-rf/"
    response = requests.get(url)
    return response.text

def parsing(text):
    soup = BeautifulSoup(text, "lxml")
    tr_list = soup.findAll("tr")

    print("===================================")
    dict_of_conc = {}
    for i in range(1, len(tr_list)):
        i_obj = list(tr_list[i])
        airport = str(i_obj[1])
        k = airport.find("</a>")
        if k == -1:
            airport = airport[:airport.rfind("</td")]
            airport = airport[airport.rfind(">") + 1:]
        else:
            airport = airport[:airport.rfind("</td")]
            airport = airport[:airport.rfind("</a")]
            airport = airport[airport.rfind(">") + 1:]

        code = str(i_obj[3])
        code = code[code.find(">") + 1:code.rfind("</td")]
        if code == "" or airport == "Красноярск (Северный)":
            code = "No data"

        #print(airport)
        if airport == "Красноярск (Северный)": # в табличке пропуск одной ячейки, поэтому меняем код ячейки
            country = str(i_obj[7])
            country = country[country.find(">") + 1:country.rfind("</td")]
        else:
            country = str(i_obj[9])
            country = country[country.find(">") + 1:country.rfind("</td")]
        dict_of_conc[airport] = (code, country)
    return dict_of_conc

def write_to_js(dict_of_conc):
    f = open("iata_to_air.json", "w", encoding='utf-8')
    json.dump(dict_of_conc, f)
    f.close()

text = parse()
dict_of_conc = parsing(text)
connection(dict_of_conc)
write_to_js(dict_of_conc)

