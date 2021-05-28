import sys
import requests
import re
from bs4 import BeautifulSoup

page = requests.get("https://genshin-impact.fandom.com/wiki/Lisa")

src = page.content

soup = BeautifulSoup(src, 'html.parser')

table = soup.select('table.wikitable')[3]
tablerows = table.findAll('tr')

count = len(tablerows) - 1
print('Ascension Level', 'Requried Level', 'Mora', 'Element Material 1 Name', 'Element Material 1 Count', 
'Element Material 2 Name', 'Element Material 2 Count', 'Local Specialty Name', 'Local Specialty Count', 'Common Material Name', 'Common Material Count')

def transformCount(soupText):
    string = str(soupText.string)
    return string.replace('×', '')

for x in range(1, count):
    row = tablerows[x]
    ascLevel = row.select('th')[0].text.strip()
    cell = row.select('td')
    reqLevel = cell[0].text.strip()
    mora = re.sub(',', '', cell[1].text.strip())

    eleMat1Name = cell[2].select('a')[1].text.strip()
    eleMat1Count = transformCount(cell[2].select('a')[1].next_sibling)

    eleMat2Name = cell[3].select('a')[1].text.strip() if cell[3].select('a') else 'None'
    eleMat2Count = transformCount(cell[3].select('a')[1].next_sibling) if cell[3].select('a') else '0'

    localSpecname = cell[4].select('a')[1].text.strip()
    localSpecCount = transformCount(cell[4].select('a')[1].next_sibling)

    commonMatName = cell[5].select('a')[1].text.strip()
    commonMatCount = transformCount(cell[5].select('a')[1].next_sibling)



    print(ascLevel, reqLevel, mora, eleMat1Name, eleMat1Count, eleMat2Name, eleMat2Count, localSpecname, localSpecCount, commonMatName, commonMatCount)
    print('\n')