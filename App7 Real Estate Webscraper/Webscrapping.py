import requests
from bs4 import BeautifulSoup
import pandas

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/80.0.3987.132 Safari/537.36'}


r = requests.get(
    "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers)
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "propertyRow"})
all[0].find("h4", {"class": "propPrice"}).text.replace(
    "\n", "").replace(" ", "")
page_nr = soup.find_all("a", {"class": "Page"})[-1].text

l = []

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="


for page in range(0, int(page_nr)*10, 10):
    print(base_url+str(page)+".html")
    r = requests.get(base_url+str(page)+".html", headers=headers)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "propertyRow"})

    for item in all:
        d = {}

        d["Address"] = item.find_all(
            "span", {"class", "propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all(
                "span", {"class", "propAddressCollapse"})[1].text
        except:
            d["Locality"] = None
        d["Price"] = item.find("h4", {"class", "propPrice"}
                               ).text.replace("\n", "").replace(" ", "")
        try:
            d["Beds"] = item.find("span", {"class", "infoBed"}).find("b").text
        except:
            d["Beds"] = None

        try:
            d["Area"] = item.find("span", {"class", "infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = item.find(
                "span", {"class", "infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find(
                "span", {"class", "infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        for column_group in item.find_all("div", {"class": "columnGroup"}):
            # print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                #print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)

df = pandas.DataFrame(l)
df.to_csv("Estate_data.csv")
