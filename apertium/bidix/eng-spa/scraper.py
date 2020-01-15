import requests
import progressbar
import time
from bs4 import BeautifulSoup

URL = "https://dictionary.cambridge.org/spellcheck/spanish-english/?q="
url2 = ""
page = requests.get(URL)

unknown = False

soup = BeautifulSoup(page.content, 'html.parser')

with open("drae.eng.txt") as f:
	lines = [line.rstrip() for line in f]
with progressbar.ProgressBar(max_value=progressbar.UnknownLength) as bar:
	for i in range(len(lines)):
		bar.update(i)
		try:
			if lines[i][0]=='*':
				url2 = URL
				for j in range(len(lines[i])):
					if j!=0:
						url2 += lines[i][j]
				print(url2)
				page = requests.get(url2)

				soup = BeautifulSoup(page.content, "html.parser")

				msg = soup.find_all("section", class_="lpb-10 lbb")
				
				if "Search suggestions for" in str(page.content):
					unknown = True
					print("URL: ", url2, " (STATUS: known)")
					print("Ignoring...")
				elif unknown==False:
						with open("unknownlinks.txt", "a") as f2:
							f2.write(url2 + "\n")
							print("URL: ", url2, " (STATUS: unknown)")
							print("Writing to file...")
				"""
				for msg_single in msg:
					if msg_single == "Your search terms did not match any definitions." or "Search suggestions for" in msg_single:
						unknown = True
						print("URL: ", url2, " (STATUS: known)")
						print("Ignoring...")
					if unknown==False:
						with open("unknownlinks.txt", "a") as f2:
							f2.write(url2, "\n")
							print("URL: ", url2, " (STATUS: unknown)")
							print("Writing to file...")
			"""
		except IndexError:
			continue
