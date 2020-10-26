#add code for flask app object
from flask import Flask, render_template

app = Flask(__name__)

# Dependencies
from bs4 import BeautifulSoup
import requests
import re

# generate random integer point values
from random import seed
from random import randint

#set route for user navigation
@app.route('/')

#define app function
def index():
    
    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://www.reddit.com/r/MemeEconomy/", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    imgs = soup.findAll('img', attrs={'alt':'Post image'})

    imglist = []
    for img in imgs :
        link_src = img.get('src')
        imglist.append(link_src)

    #picture = imglist[1]
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

    
    return render_template("index.html", text = text, picture = picture)


#set route for user navigation
@app.route('/d1')

#define app function
def D1():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://www.thefactsite.com/facts-about-the-sun/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("p", attrs={"class": "list"})

    FACTS = [fact.find(string=re.compile("(S|s)un")) for fact in data]
    # list size: 40
    # seed random number generator
    seed(1)
    # generate some integers
    num = randint(0, 39)

    text = (FACTS[num]) 
    
    return render_template("d1.html", text = text)


#set route for user navigation
@app.route('/d2')

#define app function
def D2():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://factpros.com/interesting-facts-about-the-moon-for-kids-and-adults/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("h5")

    FACTS = [fact.find(string=re.compile("(M|m)oon")) for fact in data]
    # list size: 40

    # seed random number generator
    seed(1)
    # generate some integers
    num = randint(0, 39)
    text = (FACTS[num])

    
    return render_template("d2.html", text = text)



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
    # list size: 46

    # seed random number generator
    seed(1)
    # generate some integers
    num = randint(0, 45)
    text = (FACTS[num])
    
    return render_template("d3.html", text = text)


#set route for user navigation
@app.route('/d4')

#define app function
def D4():

    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://techjury.net/blog/cloud-computing-statistics/",headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    data = soup.findAll("h4")

    FACTS = [fact.find(string=re.compile(".")) for fact in data]
    # list size: 33 (skip first index[0])

    # seed random number generator
    seed(1)
    # generate some integers
    num = randint(1, 32)

    text = (FACTS[num])

    return render_template("d3.html", text = text)