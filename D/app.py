#add code for flask app object
from flask import Flask, render_template

app = Flask(__name__)

# Dependencies
from bs4 import BeautifulSoup
import requests
import re


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


   #Set up list
    D1 = 'sun god'
    #D2 = 'D2'
    #D3 = 'D3'


    #get number
    number = 10


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
    text = (soup.p)

    
    return render_template("d1.html", text = text)


#set route for user navigation
@app.route('/d2')

#define app function
def D2():

    #Set up list
    #D1 = 'sun god'
    D2 = 'moon god'
    #D3 = 'D3'


    #get number
    number = 30

    #move through list
    search = D2
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
    text = (soup.p)

    
    return render_template("d2.html", text = text)



#set route for user navigation
@app.route('/d3')

#define app function
def D3():

    #Set up list
    #D1 = 'D1'
    #D2 = 'D2'
    D3 = 'ocean god'


    #get number
    number = 30

    #move through list
    search = D3
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
    text = (soup.p)

    
    return render_template("d3.html", text = text)