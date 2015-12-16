# Download-Lynda-Videos

Works for ubuntu 14.04 and Python 2.7.6.

## Install beautifulsoup:

    sudo apt-get install python-bs4

## Install youtube-dl:

Install youtube-dl via pip (not apt) to have the "good" version:  

    sudo apt-get install python-setuptools  
    sudo easy_install pip
    sudo pip install --upgrade youtube-dl

## HOW TO:
1. Select your course on **http://www.lynda.com/** and replace the link on **line 8** by your link.
2. Replace the key URL on **line 12** by your key URL.  
3. Replace yourLogin and yourPassword **on line 15** by your login and your password to access the site.  
4. Run script:
       python lynda.py
5. The downloaded videos are in the current folder.  
