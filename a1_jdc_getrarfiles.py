# brew install unrar
import requests, os, bs4
import urllib.request
import patoolib
from pyunpack import Archive
from os.path import expanduser
home = expanduser("~")

url = 'http://data.judicial.gov.tw/'              # starting url
targetDir = home + '/' + 'JDCYuan'
os.makedirs(targetDir, exist_ok=True)   # store opendata rar files in ~/JDCYuan

i = 0

# TODO: Download the page.
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))

soup = bs4.BeautifulSoup(res.text, 'lxml')  # create bs4 object.

# TODO: Find the URL of the rar files.
hrefs = soup.select('td > a')

i = 0
for href in hrefs:
    i += 1
    path = href.get('href')  # <a href="rar/199601--(20190220Update).rar">
    s = path.split("/")
    filename = s[1]
    urlpath = url + path
    print('Downloading file {}. {}...'.format(i, urlpath))
    urllib.request.urlretrieve(urlpath, targetDir + '/' + filename)

print('There are {} Files have been downloaded.'.format(i))

