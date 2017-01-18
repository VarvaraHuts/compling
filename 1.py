import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
req = urllib.request.Request('http://animals.nationalgeographic.com/animals/mammals/sea-otter/', headers)
html = req.read()
print (html)
