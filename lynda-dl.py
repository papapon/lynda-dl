# adapted from http://fossbytes.com/how-to-download-lynda-com-videos-using-youtube-dl/

import os
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('http://www.lynda.com/Unity-tutorials/Unity-5-2D-Building-Tile-Map-Editor/384876-2.html') # url from the site you'd like to scrape

for link in BeautifulSoup(response).find_all('a', href=True):
    #print link['href']
    if 'http://www.lynda.com/Unity-tutorials/' in link['href']: # parse only the links that contain the key URL to your specific tutorial
        l = link['href']
        #print l
        os.system("youtube-dl --username yourLogin --password yourPassword " + l) # login + password lynda to change. nb : the space after your password is usefull
