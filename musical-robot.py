import pycurl
from io import BytesIO

baseURL = "https://www.classicalmpr.org/topic/daily-download"
fullURL = "http://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/2020/09/03/daily_download_20200903_128.mp3"

# https://stackabuse.com/using-curl-in-python-with-pycurl/



b_obj = BytesIO()
crl = pycurl.Curl()

# url
crl.setopt(crl.URL, 'http://download.publicradio.org/podcast/minnesota/classical/programs/free-downloads/2020/09/03/daily_download_20200903_128.mp3')

crl.setopt(crl.WRITEDATA, b_obj)

crl.perform()

crl.close()

get_body = b_obj.getvalue()


