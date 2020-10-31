#add code for flask app object
from flask import Flask, render_template

app = Flask(__name__)

# Dependencies
from bs4 import BeautifulSoup
import requests
import re
import random

#set route for user navigation
@app.route('/')

#define app function
def index():
    

    picture = ("https://truthignitedministry.files.wordpress.com/2019/01/SunGodWordpress.png?w=920&h=344&crop=1")
    
    ########################################
    #Set up list
    D1 = 'sun god'
    #D2 = 'D2'
    #D3 = 'D3'

    #get number
    number = 30

    #move through list
    search = D1
    article = []
    results = 100 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            article.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

    page = requests.get(f'{article[number]}')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = (soup.text) 

    
    return render_template("index.html", text = text,)


#set route for user navigation
@app.route('/d1')

#define app function
def D1():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://www.thefactsite.com/facts-about-the-sun/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("p", attrs={"class": "list"})

    FACTS = [fact.find(string=re.compile("(S|s)un")) for fact in data]
    FACT = [] 
    for val in FACTS: 
        if val != None : 
            FACT.append(val)
    page2 = requests.get("https://www.wiseoldsayings.com/the-sun-quotes/",headers=headers)
    soup2 = BeautifulSoup(page2.content,'html.parser')

    data2 = soup2.findAll("b")

    FACTS2 = [fact2.find(string=re.compile("(S|s)")) for fact2 in data2]
    FACT2 = [] 
    for val2 in FACTS2: 
        if val2 != None :
            val2.replace('\xa0','') 
            FACT2.append(val2)

    s1 = random.choice(FACT)
    q1 = "\""
    q2 = "\""
    s2 = random.choice(FACT2).replace('\xa0','')
    s2 = q1 + s2 + q2
    text1 = s1
    text2 = s2
    return render_template("d1.html", text1 = text1, text2 = text2)


#set route for user navigation
@app.route('/d2')

#define app function
def D2():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://factpros.com/interesting-facts-about-the-moon-for-kids-and-adults/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("h5")

    FACTS = [fact.find(string=re.compile("(M|m)oon")) for fact in data]
    FACT = [] 
    for val in FACTS: 
        if val != None : 
            FACT.append(val)

    s1 = (random.choice(FACT))
    
    page2 = requests.get("https://www.wiseoldsayings.com/the-moon-quotes/",headers=headers)
    soup2 = BeautifulSoup(page2.content,'html.parser')

    data2 = soup2.findAll("b")

    FACTS2 = [fact2.find(string=re.compile("(S|s)")) for fact2 in data2]
    FACT2 = [] 
    for val2 in FACTS2: 
        if val2 != None :
            val2.replace('\xa0','') 
            FACT2.append(val2)

    s2 = random.choice(FACT2).replace('\xa0','')
    q1 = "\""
    q2 = "\""
    s2 = q1 + s2 + q2

    text1 = s1
    text2 = s2
    return render_template("d2.html", text1 = text1, text2 = text2)



#set route for user navigation
@app.route('/d3')

#define app function
def D3():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://www.factretriever.com/star-facts",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.select("ul.factsList")
    data2 = data[0].findAll("li")

    FACTS = [fact.find(string=re.compile(".")) for fact in data2]
    FACT = [] 
    for val in FACTS: 
        if val != None : 
            FACT.append(val)

    s1 = (random.choice(FACT))
    
    page2 = requests.get("https://www.wiseoldsayings.com/stars-quotes/",headers=headers)
    soup2 = BeautifulSoup(page2.content,'html.parser')

    data2 = soup2.findAll("b")

    FACTS2 = [fact2.find(string=re.compile("(S|s)")) for fact2 in data2]
    FACT2 = [] 
    for val2 in FACTS2: 
        if val2 != None :
            val2.replace('\xa0','') 
            FACT2.append(val2)

    s2 = random.choice(FACT2).replace('\xa0','')
    q1 = "\""
    q2 = "\""
    s2 = q1 + s2 + q2
    
    text1 = s1
    text2 = s2
    return render_template("d3.html", text1 = text1, text2 = text2)


#set route for user navigation
@app.route('/d4')

#define app function
def D4():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://techjury.net/blog/cloud-computing-statistics/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("h4")

    FACTS = [fact.find(string=re.compile(".")) for fact in data]
    FACT = [] 
    for val in FACTS: 
        if val != None : 
            FACT.append(val)

    s1 = (random.choice(FACT))
    
    page2 = requests.get("https://www.wiseoldsayings.com/computer-quotes/",headers=headers)
    soup2 = BeautifulSoup(page2.content,'html.parser')

    data2 = soup2.findAll("b")

    FACTS2 = [fact2.find(string=re.compile("(S|s)")) for fact2 in data2]
    FACT2 = [] 
    for val2 in FACTS2: 
        if val2 != None :
            val2.replace('\xa0','') 
            FACT2.append(val2)

    s2 = random.choice(FACT2).replace('\xa0','')
    q1 = "\""
    q2 = "\""
    s2 = q1 + s2 + q2
    
    text1 = s1
    text2 = s2
    return render_template("d4.html", text1 = text1, text2 = text2)