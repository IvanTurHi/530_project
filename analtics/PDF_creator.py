from fpdf import FPDF
import datetime
import json


class PDF(FPDF):
    def print_title(self):
        self.add_page()
        self.set_font("Arial", size=20)
        self.cell(200, 10, txt=self.title, ln=1, align="C")

    def print_header(self):
        self.set_font("Arial", size=20)
        self.cell(200, 30, txt="Report for {} {}".format(self.month[datetime.datetime.now().month-1], datetime.datetime.now().year), ln=1, align="C")

    def to_print(self):
        self.output("ry{}m{}.pdf".format(datetime.datetime.now().year, datetime.datetime.now().month-1))

    def get_data(self):
        f = open(self.filename, encoding='utf-8')

        self.data = json.load(f)
        self.emissions = self.data["total emissions"]
        self.kilometers = self.data["total kilometers"]
        self.flights = self.data["total number of flights"]
        self.domestic = self.data["number of domestic flights"]
        self.foreign = self.data["number of foreign flights"]
        self.percentage = self.data["percentage of domestic flights"]
        self.companies = self.data["companies"]
        self.airports = self.data["airports"]
        c = 3
        self.d["total emissions (kg)"] = round(self.emissions, c)
        self.d["total number of kilometers"] = round(self.kilometers, c)
        self.d["total number of flights"] = round(self.flights, c)
        self.d["total number of domestic flights"] = round(self.domestic, c)
        self.d["total number of foreign flights"] = round(self.foreign, c)
        self.d["percentage of domestic flights"] = round(self.percentage, c)

    def print_total_data(self):
        self.set_font("Arial", size=16)
        self.cell(200, 30, txt="General information", ln=1, align="C")
        self.set_font("Arial", size=14)
        for i in self.d:
            self.cell(200, h=10, txt="{} -- {}".format(i, self.d[i]), ln=1, align="C")

    def print_by_companies_by_number_of_flights(self):
        self.set_font("Arial", size=16)
        self.cell(200, 30, txt="Airline stats", ln=1, align="C")
        self.cell(200, 15, txt="Top companies by number of flights", ln=1, align="C")

        self.list_of_comp = []
        for i in self.companies:
            self.list_of_comp.append((i, self.companies[i]["emissions"], self.companies[i]["kilometers"], self.companies[i]["total number of flights"]))

        #Сортировка по количеству рейсов
        for i in range(len(self.list_of_comp)-1):
            for j in range(len(self.list_of_comp)-i-1):
                if self.list_of_comp[j][3] < self.list_of_comp[j+1][3]:
                    self.list_of_comp[j], self.list_of_comp[j + 1] = self.list_of_comp[j + 1], self.list_of_comp[j]

        self.set_font("Arial", size=14)
        for i in range(self.top_for_print):
            self.cell(200, h=10, txt="{} -- {} (percentage of total -- {})".format(self.list_of_comp[i][0], self.list_of_comp[i][3], round(self.list_of_comp[i][3]/self.flights * 100, 2)), ln=1, align="C")

    def print_by_companies_by_emissions(self):
        self.set_font("Arial", size=16)
        self.cell(200, 15, txt="Top companies by emissions", ln=1, align="C")
        self.set_font("Arial", size=14)

        self.list_of_comp = []
        for i in self.companies:
            self.list_of_comp.append((i, self.companies[i]["emissions"], self.companies[i]["kilometers"], self.companies[i]["total number of flights"]))

        #Сортировка по количеству выбросов
        for i in range(len(self.list_of_comp)-1):
            for j in range(len(self.list_of_comp)-i-1):
                if self.list_of_comp[j][1] < self.list_of_comp[j+1][1]:
                    self.list_of_comp[j], self.list_of_comp[j + 1] = self.list_of_comp[j + 1], self.list_of_comp[j]

        for i in range(self.top_for_print):
            self.cell(200, h=10, txt="{} -- {}kg (percentage of total -- {})".format(self.list_of_comp[i][0], round(self.list_of_comp[i][1], 3), round(self.list_of_comp[i][1]/self.emissions * 100, 2)), ln=1, align="C")


    def print_by_companies_by_kilometers(self):
        self.set_font("Arial", size=16)
        self.cell(200, 15, txt="Top companies by kilometers", ln=1, align="C")
        self.set_font("Arial", size=14)

        self.list_of_comp = []
        for i in self.companies:
            self.list_of_comp.append((i, self.companies[i]["emissions"], self.companies[i]["kilometers"], self.companies[i]["total number of flights"]))

        #Сортировка по количеству километров
        for i in range(len(self.list_of_comp)-1):
            for j in range(len(self.list_of_comp)-i-1):
                if self.list_of_comp[j][2] < self.list_of_comp[j+1][2]:
                    self.list_of_comp[j], self.list_of_comp[j + 1] = self.list_of_comp[j + 1], self.list_of_comp[j]

        for i in range(self.top_for_print):
            self.cell(200, h=10, txt="{} -- {}km (percentage of total -- {})".format(self.list_of_comp[i][0], round(self.list_of_comp[i][2], 3), round(self.list_of_comp[i][2]/self.kilometers * 100, 2)), ln=1, align="C")


    def airports_to_print(self):
        self.set_font("Arial", size=16)
        self.cell(200, 15, txt="Busiest airports", ln=1, align="C")
        self.set_font("Arial", size=14)
        pdf.set_font('DejaVu', '', 14)
        self.list_of_airports = []
        for i in self.airports:
            self.list_of_airports.append((i, self.airports[i]["departure"], self.airports[i]["arrival"], self.airports[i]["departure"]+self.airports[i]["arrival"]))

        #Сортировка по общему количеству самолетов
        for i in range(len(self.list_of_airports)-1):
            for j in range(len(self.list_of_airports)-i-1):
                if self.list_of_airports[j][3] < self.list_of_airports[j+1][3]:
                    self.list_of_airports[j], self.list_of_airports[j + 1] = self.list_of_airports[j + 1], self.list_of_airports[j]

        for i in range(self.top_for_print):
            self.cell(200, h=10, txt="{}: deaprture--{}, arrival--{}".format(self.list_of_airports[i][0], self.list_of_airports[i][1], self.list_of_airports[i][2]), ln=1, align="C")

    def set_picture(self):
        self.set_font("Arial", size=16)
        self.cell(200, 110, txt="Distribution of flights by mileage", ln=1, align="C")
        pdf.image("raspredelenie_kilometraja_for_March.png", w=200, h=150, x=1, y=70)
        self.cell(200, 158, txt="Number of planes by day", ln=1, align="C")
        pdf.image("Planes_for_March.png", w=200, h=150, x=1, y=150)

    title = "Project 530"
    month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}
    filename = "statistic.json"
    emissions = 0
    kilometers = 0
    flights = 0
    domestic = 0
    foreign = 0
    percentage = 0
    companies = {}
    airports = {}
    data = {}
    top_for_print = 5
    d = {"total emissions (kg)": emissions, "total number of kilometers": kilometers, "total number of flights": flights,
         "total number of domestic flights": domestic, "total number of foreign flights": foreign,
         "percentage of domestic flights": percentage}


pdf = PDF()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.print_title()
pdf.print_header()
pdf.get_data()
pdf.print_total_data()
pdf.print_by_companies_by_number_of_flights()
pdf.print_by_companies_by_emissions()
pdf.print_by_companies_by_kilometers()
pdf.airports_to_print()
pdf.set_picture()
pdf.to_print()
