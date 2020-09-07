# resources
# https://stackabuse.com/using-curl-in-python-with-pycurl/
# https://www.jquery-az.com/python-datetime-to-string/

import pycurl
from io import BytesIO
import certifi
import datetime


baseURL = 'https://www.classicalmpr.org/topic/daily-download'
fullURL = 'http://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/2020/08/13/daily_download_20200813_128.mp3'

destination_filename_base = 'daily_download_'

date = datetime.datetime.now()
date_str = '{:%Y%m%d}'.format(date)

destination_filename = 'scratch_' + destination_filename_base + date_str + '_128.mp3'
path = 'G:\Music\Classical MPR Daily Download\\' + destination_filename

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


