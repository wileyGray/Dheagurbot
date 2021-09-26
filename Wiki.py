import requests
from bs4 import BeautifulSoup

class Wiki:
	def __init__(self, url):
		self.page = requests.get(url)

		self.soup = BeautifulSoup(self.page.content, "html.parser")

		self.mainContent = self.soup.find(id="mw-content-text")

		self.allPTags = self.mainContent.find_all("p")

		self.pTagsToText = [text.text for text in self.allPTags]

		#for text in self.pTagsToText:
			#print(text)


#def main():
	#url = "https://en.wikipedia.org/wiki/The_Move_(XM)"
	#url = "https://en.wikipedia.org/wiki/Czech_Christmas_Mass"
	#print(url)
	#test = Wiki(url)


#main()