import requests
from bs4 import BeautifulSoup

response = requests.get("https://runwayml.com/careers/#open-positions")
soup = BeautifulSoup(response.text, 'html.parser')
positions = soup.find_all("div", attrs={"class": "lg:w-11/12 lg:mx-auto flex justify-around w-full"})
for pos in positions:
  role_div = pos.find_all("div", attrs={"class": "md:w-1/2 font-display text-3xl leading-tight"})[0]
  role = role_div.text

  link_div = pos.find_all("a", attrs={"class": "rw-btn border border-black text-base hover:bg-black hover:text-white transition-colors duration-150"})[0]
  link = link_div.attrs["href"]
  
  position = {"title": role, "link": link, "company": "RunwayML"}

  print(position)