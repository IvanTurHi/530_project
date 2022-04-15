import json
import datetime
import re
from os import listdir
from haversine import haversine


#----------- Дебаг ----------
file_debug = open("Filter_II_debug.txt", mode='w', encoding='utf-8')
file_debug.close()

#----------- День сегодня ----------
t2 = datetime.date.today()
t3 = datetime.timedelta(days=1)
time_I = (t2 - t3).strftime('%d.%m.%Y')
#print(time_I)

#----------- Основной файл для читения ----------
pas = r"C:\Users\gev46\Desktop\Проект\1"
files = listdir(pas)
for i in files:
    if "2022" in i:
        with open(pas+r"\\"+i, encoding='utf-8') as json_file:
        #with open('../phaetonalfa/phaetonalfa_data_today/flights_data.json', encoding='utf-8') as json_file:
            print(i)
            data_for_file = i[:10]
            print(data_for_file)
            all_air = json.load(json_file)
            r = json.dumps(all_air).replace('null', '"notgiven"')
            all_airplan = json.loads(r)
            # print(all_airplan)

        #----------- Всего файлов ----------
        total = []
        for user in all_airplan:
            total.append(user['url'])
        combien = len(total) #Загружаем все найденный рейсы с flightware и вычисляем их колчество
        #print(combien)

        #----------- Установка сетов ----------
        url_set = []
        aircraft_set = []
        origin_set = []
        destination_set = []
        direct_distance_set = []
        coordinates_set = []


        # вычисление реального километража
        def work_with_cordinates(coordinates):
            work_with_cor = []
            work_with_cor.append('1')
            for i in coordinates:
               work_with_cor.append(i)
            for i in range(6):
                work_with_cor.pop(0)
            while re.search("[А-я]", work_with_cor[1]):
                work_with_cor.pop(0)
                work_with_cor.pop(0)
                work_with_cor.pop(0)
                if len(work_with_cor) == 0:
                    break
            if len(work_with_cor) != 0:
                i = 0
                only_cor = []
                i = 0
                for i in range(len(work_with_cor)):
                    if  i + 1 == len(work_with_cor):
                        break
                    if "@" in work_with_cor[i+1]:
                        break
                    if re.search("[А-я]", work_with_cor[i]):
                        only_cor.append(work_with_cor[i+1])
                        only_cor.append(work_with_cor[i + 2])
                total_dist = 0
                for i in range(0, len(only_cor)-2, 2):
                    first = (float(only_cor[i]), float(only_cor[i+1]))
                    second = (float(only_cor[i+2]), float(only_cor[i+3]))
                    total_dist += haversine(first, second)
                #print(total_dist)
                return total_dist
            else:
                return -1

        #----------- Заполнение сетов ----------
        for user in all_airplan:
            url = user['url']
            url_set.append(url) #----------Заполнение сета url
            aircraft = user['aircraft']
            aircraft_set.append(aircraft) #----------Заполнение сета aircraft
            origin = user['origin']
            origin_set.append(origin) #----------Заполнение сета origin
            destination = user['destination']
            destination_set.append(destination) #----------Заполнение сета destination
            coordinates = user['coordinates']
            coordinates_set.append(coordinates) #----------Заполнение сета coordinates
            try:
                direct_distance = work_with_cordinates(coordinates)
            except BaseException:
                direct_distance = user['direct_distance']
            if direct_distance == -1:
                direct_distance = user['direct_distance']
            direct_distance_set.append(direct_distance) #----------Заполнение сета direct_distance

        #----------- Фильтр для рейсов ----------
        url_new = []
        g0 = 0
        while g0 < combien:
            url_ne = url_set[g0]
            url_n = url_ne.replace('https://ru.flightaware.com/live/flight/', '')
            url_new.append(url_n)
            g0 += 1
        # print(url_new)

        #----------- Фильтр самолета ----------
        aircraft_new = []
        g = 0
        i = 0
        while g < combien:
            if aircraft_set[g].find('(') != -1:
                jp = aircraft_set[g]
                j = jp.index(' (')
                a_r = jp[i:j:1]
                aircraft_new.append(a_r)
                g += 1
            elif aircraft_set[g] == 'notgiven':
                a_t = aircraft_set[g]
                aircraft_new.append(a_t)
                g += 1
            else:
                g += 1
        # print(aircraft_new)

        #----------- Фильтр координат ----------
        coor = []
        coordinates_new = []
        g2 = 0
        while g2 < combien:
            z = len(coordinates_set[g2])
            if z != 0:
                coor = coordinates_set[g2]
                coordinates_n = []
                coordinates_n.append(coor[1])
                coordinates_n.append(coor[2])
                i = 6
                while i < z:
                    if coor[i].find('.')  != -1:
                        coordinates_n.append(coor[i])
                        i += 1
                    else:
                        i += 1
                coordinates_new.append(coordinates_n)
            else:
                coordinates_new.append(list(''))
                #print(coordinates_new[-1])
            g2 += 1

        coordinates_new_form = []
        g3 = 0
        while g3 < combien:
            xol =  coordinates_new[g3]
            z2 = len(xol)
            allpoints = (int(z2/2) - 2)
            body_in_new = []
            i = 2
            while i < z2:
                i += 1
                x1 = i-1
                x = xol[x1]
                y1 = i
                y = xol[y1]
                i += 1

                body_in = {"longitude": x,"latitude": y}
                body_in_new.append(body_in)
                body_all = {"allpoints": allpoints, "points": body_in_new}
            # print(body_all)
            coordinates_new_form.append(body_all)
            g3 += 1

        #----------- Чтение файла СО2 ----------
        #-----------CO2 JSON include {emissions_less, emissions_max, seats_max, seats_less, max_airplane_weight, commercial_weight}
        with open('CO6.json', mode='r', encoding='utf-8') as file:
            day_json_dataCO2 = json.load(file)
        # print(day_json_dataCO2)

        #----------- Фильтр километража ----------
        direct_distance_new = []
        g4 = 0
        while g4 < combien:
            direct_distance_n = direct_distance_set[g4]
            #direct_distance_ne = 1.60934 * direct_distance_n
            direct_distance_ne = direct_distance_n
            direct_distance_new.append(direct_distance_ne)
            g4 += 1
        # print(direct_distance_new)

        #----------- Кpm коефициент пассажиромест ----------
        Kpm_name = "Kpm.txt"
        Kpm_today = open(Kpm_name, mode='r', encoding='utf-8')
        Kx = Kpm_today.readline()
        Ky = Kx.replace(',', '.')
        Kpm = float(Ky)
        Kpm_today.close()
        # print(Kpm)

        # ----------- Обявление сетов математика ----------
        totalfuelwastedless_new = []
        totalfuelwastedmax_new = []
        totalemissionsless_new = []
        totalemissionsmax_new = []
        emissionsforpointless_new = []
        emissionsforpointmax_new = []
        seats_max_new = []
        seats_less_new = []
        in_data = []
        g5 = 0
        list_not_in_CO6 = []
        while g5 < combien:
            in_dat = aircraft_new[g5]
            in_data.append(in_dat)

        #----------- Математика ----------
            try:
                for user in day_json_dataCO2:
                    emissions_less = user[in_dat][0]
                    emissions_max = user[in_dat][1]
                    seats_max = user[in_dat][2]
                    seats_less = user[in_dat][3]
                    m_airplane_weight = user[in_dat][4]
                    c_weight = user[in_dat][5]
                totalemissionsless100 = float(emissions_less)
                totalemissionsmax100 = float(emissions_max)
                max_airplane_weight = float(m_airplane_weight)
                commercial_weight = float(c_weight)
                km = direct_distance_new[g5]
                empty_airplane_weight = max_airplane_weight - commercial_weight
                real_airplane_weight = (((commercial_weight/100) * Kpm) + empty_airplane_weight)
                Influence_from_passengers = 100 - ((real_airplane_weight/max_airplane_weight)*100)
                Real_totalemissionsless = (totalemissionsless100/100) * (100 - Influence_from_passengers)
                Real_totalemissionsmax = (totalemissionsmax100/100) * (100 - Influence_from_passengers)
                totalemissionsless = km * (Real_totalemissionsless/100)
                totalemissionsmax = km * (Real_totalemissionsmax/100)
                totalfuelwastedless = (totalemissionsless/3.15)
                totalfuelwastedmax = (totalemissionsmax/3.15)
                em = km / 6.15
                try:
                    emissionsforpointless = totalemissionsless / em
                    emissionsforpointmax = totalemissionsmax / em
                except ZeroDivisionError:
                    emissionsforpointless = totalemissionsless / 1
                    emissionsforpointmax = totalemissionsmax / 1
            # ----------- Добавление ----------
                totalfuelwastedless_new.append(totalfuelwastedless)
                totalfuelwastedmax_new.append(totalfuelwastedmax)
                totalemissionsless_new.append(totalemissionsless)
                totalemissionsmax_new.append(totalemissionsmax)
                emissionsforpointless_new.append(emissionsforpointless)
                emissionsforpointmax_new.append(emissionsforpointmax)
                seats_max_new.append(seats_max)
                seats_less_new.append(seats_less)
                g5 += 1
            except KeyError:
                print("Дата в дебаге!")
                list_not_in_CO6.append(in_dat)
                file_new_name_problem = "./Error_debug/" + time_I + ".json"
                file_new_for_problem = open(file_new_name_problem, mode='w', encoding='utf-8')
                #json.dump(all_air, file_new_for_problem, ensure_ascii=False)
                file_new_for_problem.close()
                #raise SystemExit
                g5 += 1

        # ----------- Запись выбросов ----------
        print('не нашлось в файле СО6', set(list_not_in_CO6))
        file_for_unfindable = open("unfindable.txt", 'a+')
        for i in set(list_not_in_CO6):
            file_for_unfindable.write(i + '\n')
        flightname_today = []
        flightname_today_new = []
        flightname_pollution_today_data = []
        flightname_pollution_today = []
        g6 = 0
        k = 0
        while g6 < combien-k:
            #if g6 == combien - 35:
            #    print(1)
            if in_data[g6] not in set(list_not_in_CO6):
                #print(totalfuelwastedless_new[g6])
                flightname_pollution_today_data = [
                    {"data": data_for_file,
                     "airplane": in_data[g6],
                     "km": direct_distance_new[g6],
                     "totalfuelwastedless": totalfuelwastedless_new[g6],
                     "totalfuelwastedmax": totalfuelwastedmax_new[g6],
                     "totalemissionsless": totalemissionsless_new[g6],
                     "totalemissionsmax": totalemissionsmax_new[g6],
                     "emissionsforpointless": emissionsforpointless_new[g6],
                     "emissionsforpointmax": emissionsforpointmax_new[g6],
                     "coefficientoftheseatsmax": seats_max_new[g6],
                     "coefficientoftheseatsless": seats_less_new[g6]
                     }
                ]
                #print(g6)
                if g6 == 1802:
                    print('sex')
                flightname_pollution_today.append(flightname_pollution_today_data)
                flightname_today = {"flightname": url_new[g6],
                                    "rounds": flightname_pollution_today[g6-k]
                                    }
                flightname_today_new.append(flightname_today)
            else:
                k += 1
            g6 += 1

        # print(coordinates_new_form[1])
        # print(flightname_today_new[1])

        # ----------- Дописать в БД или создать весь файл ----------
        last_generator = []
        glob = 0
        i = 0
        denis = 0
        while glob < len(flightname_today_new):
            file_name = url_new[glob] + ".json"
            file_new_name = "./Flight_today_new/" + url_new[glob] + ".json"
            file1 = open(file_new_name, mode='a+', encoding='utf-8')
            file2 = open(file_new_name, mode='r', encoding='utf-8')
            old_data = file2.read()  # Читение файла для проверки: (1) на дозапись (2) записать полностью
            denis = len(old_data)
            if denis != 0:
                j = old_data.index(']}}}')
                a_r = old_data[i:j:1]
                ox1 = json.dumps(flightname_pollution_today[glob])
                ox = ox1[1:-1:1]
                add = a_r + "," + ox + "]}}}"
                file_json = open("./Flight_today_new/"  + url_new[glob] + ".json", "w+", encoding='utf-8')
                file_json.write(add)
                file_json.close()
                file1.close()
                file2.close()
            else:
                last_generator = {
                    "Way": {
                        "from": origin_set[glob],
                        "to": destination_set[glob],
                        "coordinates": coordinates_new_form[glob],
                        "flights": flightname_today_new[glob]
                    }
                }

                file_new_name = "./Flight_today_new/" + url_new[glob] + ".json"
                file_new_for_generator = open(file_new_name, mode='w', encoding='utf-8')
                json.dump(last_generator, file_new_for_generator)
                file_new_for_generator.close()
            glob += 1

        # ----------- Оповещение об окончании программы ----------
        file_debug = open("Filter_II_debug.txt", mode='w', encoding='utf-8')
        file_debug.write("Working well")
        file_debug.close()
