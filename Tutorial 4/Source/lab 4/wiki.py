import requests
from bs4 import BeautifulSoup
import os

def main():
    u="https://en.wikipedia.org/wiki/India"
    s=requests.get(u)
    sp = BeautifulSoup(s.content, "html.parser")
    r=sp.findAll('div')

    for d in r:
        r1=d.find('h1')
        print(r1)
    div=sp.find('div',{'class':"mw-body"})
    print(div.text)
main()
