# https://stackabuse.com/using-curl-in-python-with-pycurl/

import pycurl
from io import BytesIO
import certifi


baseURL = 'https://www.classicalmpr.org/topic/daily-download'
fullURL = 'http://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/2020/09/07/daily_download_20200907_128.mp3'
destinationFile = "robot-music.mp3", "wb"
file = open('pycurl.md', 'wb')

b_obj = BytesIO()
crl = pycurl.Curl()

crl.setopt(crl.CAINFO, certifi.where())


# url
crl.setopt(crl.URL, fullURL)
crl.setopt(crl.WRITEDATA, file)
crl.perform()
crl.close()


get_body = b_obj.getvalue()

print('Output of GET request:\n%s' % get_body.decode('utf8')) 
