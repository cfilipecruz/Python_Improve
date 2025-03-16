import urllib.request

try:
    response = urllib.request.urlopen('https://www.pudim.com.br/', data=None, context=None)
except:
    print('The website is currently unavailable.')
else:
    print('The website is available.')
    print(response.read())