import requests
from bs4 import BeautifulSoup
import re

class WebScraper:

    def getInfo(self):
        source = requests.get( 'https://www.theguardian.com/world/ng-interactive/2020/apr/16/coronavirus-map-of-the-us-latest-cases-state-by-state').text
        soup = BeautifulSoup(source, 'lxml')

        info = soup.find_all('td', class_='co-td-cases')

        soup1 = BeautifulSoup(source, 'lxml')
        info0 = str(soup.find_all('tbody', class_='co-tbody'))

        info1 = info0.replace(',', '')

        temp = re.findall(r'\d+', info1)
        res = list(map(int, temp))

        cases = []

        for i in range(0, 108, 2):
            cases.append(res[i])

        info2 = ''.join([i for i in info1 if not i.isdigit()])
        info3 = info2.replace(
            '<td class="co-td-cases"></td>\n<td class="co-td-deaths"></td>\n<td class="co-td-bars"></td>\n</tr>\n<tr>',
            '')
        info4 = info3.replace('<td>', '')
        info5 = info4.replace('</td>', '')
        info6 = info5.replace('<td class="co-td-cases">\n<td class="co-td-deaths">\n<td class="co-td-bars">', '')
        info7 = info6.replace('<tbody class="co-tbody">\n<tr>', '')
        info8 = info7.replace('</tr>\n</tbody>', '')
        info9 = info8.replace('\n', ',')
        info10 = info9.replace('[,', '')
        info11 = info10.replace(']', '')

        info12 = info11.split(',,')

        states = []

        for i in range(0, 54):
            states.append(info12[i])

        dict = {}



        for i in range(len(states)):
            dict[states[i].upper()] = cases[i]

        return dict



