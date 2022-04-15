import psycopg2
import json

def initialization_protocol(cur, conn):

    def create_table(cur, conn):
        try:
            cur.execute("CREATE TABLE dictionary1"
                        "("
                        "IATA varchar(5) primary key, "
                        "ICAO varchar(5) not null"
                        ")")
            conn.commit()
        except psycopg2.errors.DuplicateTable:
            cur.execute("ROLLBACK")


    def filling(cur, conn):

        f_name = "IATA_and_RF_to_ICAO.json"
        f = open(f_name, mode='r', encoding='utf-8')
        Translate = json.load(f)
        for user in Translate:
            data = user['IATA_and_RF_to_ICAO']

        for i in range(0, len(data), 2):
            try:
                cur.execute("INSERT INTO dictionary1 VALUES (%s, %s)", (data[i], data[i + 1]))
                conn.commit()
            except psycopg2.errors.UniqueViolation:
                cur.execute("ROLLBACK")



    create_table(cur, conn)
    filling(cur, conn)

def chek_table(cur):
    cur.execute("SELECT EXISTS (SELECT * "
                "FROM information_schema.tables "
                "WHERE table_name = 'dictionary1' "
                "AND table_schema = 'public') AS table_exists;")
    for i in cur:
        return i[0]

def get_ICAO_system(cur, key):
    re = 0
    cur.execute("SELECT ICAO FROM dictionary1 WHERE IATA='{}'".format(key))
    for i in cur:
        re = i[0]
    if re == 0:
        return key
    else:
        return re



