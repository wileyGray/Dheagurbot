import requests
from bs4 import BeautifulSoup

class Wiki:
	def __init__(self, url):
		self.page = requests.get(url)

		self.soup = BeautifulSoup(self.page.content, "html.parser")

		self.results = self.soup.find(id="mw-content-text")

		#print(self.results.prettify())

		self.results2 = self.results.find_all("p")

		for text in self.results2:
			print(text.text)

	def getText(url: str):
		print(self.page.text)

def main():
	url = "https://en.wikipedia.org/wiki/The_Move_(XM)"
	url = "https://en.wikipedia.org/wiki/Czech_Christmas_Mass"
	print(url)
	test = Wiki(url)


main()