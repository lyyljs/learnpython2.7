from bs4 import BeautifulSoup

with open ('elice.html','r') as f:
	html_doc = f.read()

soup = BeautifulSoup(html_doc)
#print(soup.prettify())

#print soup.title
#print soup.title.name
#print soup.title.string
#print soup.title.parent.name
#print soup.p
#print soup.p['class']
#print soup.a
#print
#print soup.find_all('a')
#print
#print soup.find(id="link3")

#for link in soup.find_all('a'):
#	print(link.get('href'))

print soup.get_text()
