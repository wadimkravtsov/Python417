from asyncore import write

import requests
from bs4 import BeautifulSoup

class Parser:
    html = ""
    res = []
    numres = []
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        reg = requests.get(self.url).text
        # print(reg)
        self.html = BeautifulSoup(reg, "lxml")

    def parsing(self):
        greys = self.html.find_all("div", class_="workdesc descpad")
        numbers = self.html.find_all("div", class_="worknumber")
        for numb in numbers:
            number = numb.find("span", class_="basewhite").text
            self.numres.append(number)
            # print(number)
        for item in greys:
            rating = item.find("span", class_="base").text
            result = item.find("div", class_="workdescbar").text.strip()
            self.res.append({
                "rating": rating,
                "result": result,
            })
        # print(self.numres)
        # print(self.res)

    def save(self):
        i = 0
        with open(self.path, "w") as f:
            for item in self.res:
                f.write(f"Сканворд {self.numres[i]}\n\n{item['rating']}\nРезультаты: {item['result']}\n\n{'*' * 50}\n\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()