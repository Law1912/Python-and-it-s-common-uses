import requests
from bs4 import BeautifulSoup
from prof.models import Professors

r=requests.get('https://www.iitk.ac.in/new/iitk-faculty')
soup=BeautifulSoup(r.content, 'html.parser')
name=[]
email=[]
ri=[]
phone=[]
degree=[]
department=[]
title = soup.find_all("span", {"class": "jwts_toggleControlTitle"})
for i in range(len(title)):
    table=title[i].findNext("table")
    div=table.find_all("div", {"class": "frcard"})
    for j in range(len(div)):
        department.append(title[i].text)
        para = div[j].findNext("p")
        k=para.get_text()
        if(k.find("Research Interests:") == -1):
            ri.append(" ")
        else:
            k=k.split("Research Interests:")
            ri.append(k[1])
            k=k[0]
        if(k.find("Phone:")==-1 and k.find("Phonel:")==-1):
            phone.append(" ")
        elif(k.find("Phonel:")!=-1):
            k=k.split("Phonel:")
            phone.append(k[1])
            k=k[0]
        else:
            k=k.split("Phone:")
            phone.append(k[1])
            k=k[0]
        if(k.find("iitk.ac.in")==-1):
            email.append(" ")
            if(k.find("(")==-1):
                continue
            else:
                k=k.split("(", 1)
                name.append(k[0])
                degree.append("PhD ()")

        else:
            k=k.split("(", 1)
            name.append(k[0])
            k=k[1].split(")",1)
            email.append(k[0])
            degree.append(k[1])

from prof.models import Professors
Professors.objects.all().delete()
for i in range(len(name)):
    prof=Professors.create(name=name, email=email, degree=degree, research_interests=ri, phone=phone, department=department)
    prof.save()
