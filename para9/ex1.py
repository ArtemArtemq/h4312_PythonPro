import urllib.request

opener = urllib.request.build_opener()
response = opener.open("http://httpbin.org/get")
print(response.read())