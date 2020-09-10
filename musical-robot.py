# resources
# https://stackabuse.com/using-curl-in-python-with-pycurl/
# https://www.jquery-az.com/python-datetime-to-string/

import pycurl
from io import BytesIO
import certifi
import datetime

destination_filename_base = 'daily_download_'

date = datetime.datetime.now()
date_str = '{:%Y%m%d}'.format(date)
date_str_url = '{:%Y/%m/%d/}'.format(date)

destination_filename = destination_filename_base + date_str + '_128.mp3'
path = 'G:\Music\Classical MPR Daily Download\\' + destination_filename + '_scratch'

baseURL = 'https://www.classicalmpr.org/topic/daily-download'
fullURL = 'http://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/' + date_str_url + destination_filename

# this url might work better...
# https://feeds.feedburner.com/YourClassicalDailyDownload
feedburnerURL = 'http://feedproxy.google.com/~r/YourClassicalDailyDownload/~5/TycEQoxorbM/daily_download_20200908_128.mp3'

print(fullURL)

print(path)
destination_file = open(path, 'wb')


b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.CAINFO, certifi.where())


# url
crl.setopt(crl.URL, fullURL)
crl.setopt(crl.WRITEDATA, destination_file)
crl.perform()
crl.close()

