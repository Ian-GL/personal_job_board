import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ableton.com/en/jobs/")
soup = BeautifulSoup(response.text, 'html.parser')
positions = soup.find_all("li", attrs={"class": "page-jobs__department__listing__item"})
for pos in positions:
  role_div = pos.find_all("span", attrs={"class": "has-arrow"})[0]
  role = role_div.text

  link_div = pos.find_all("a")[0]
  link = "https://www.ableton.com" + link_div.attrs["href"]
  
  position = {"title": role, "link": link, "company": "Ableton"}

  print(position)