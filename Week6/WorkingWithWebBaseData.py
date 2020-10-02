import urllib.request
url = "http://cims.nyu.edu/~kapp/python/most_popular_words_in_english.txt"
response = urllib.request.urlopen(url)
alldata = response.read().decode('utf-8')
words = alldata.split("\n")
print(alldata)