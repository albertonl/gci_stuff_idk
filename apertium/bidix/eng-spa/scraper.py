import requests
from bs4 import BeautifulSoup

URL = 'https://dictionary.cambridge.org/spellcheck/spanish-english/?q='
url2 = ''
page = requests.get(URL)

unknown = False

soup = BeautifulSoup(page.content, 'html.parser')

with open('drae.eng.txt') as f:
	lines = [line.rstrip() for line in f]

for i in range(len(lines)):
	if lines[i][0]=='*':
		url2  = URL
		for j in range(len(lines[i])):
			if j!=0:
				url2 += lines[i][j]
				page = requests.get(url2)

				soup = BeautifulSoup(page.content, 'html.parser')

				msg = results.find_all('section', class_='lpb-10 lbb')
				for msg_single in msg:
					if msg_single == 'Your search terms did not match any definitions.':
						unknown = True

				if unknown==False:
					with open("unknownlinks.txt", "a") as f2:
						f2.write(url2)