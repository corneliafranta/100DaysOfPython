from bs4 import BeautifulSoup

with open('website.html', encoding='utf-8') as website_file:
    contents = website_file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)

print(soup.prettify())

all_ancor_tags = soup.find_all(name='a')

for tag in all_ancor_tags:
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id="name")
section_heading = soup.find(name='h3', class_="heading")
print(heading)
print(section_heading.getText())
company_url = soup.select_one(selector='p a')
