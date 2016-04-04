# This python script takes the information from a URL and writes it to a file in /tmp

import urllib


request_headers = {
  'User-Agent': 'nappybrainiac',
  'Authorization': 'token 1ab58e09acd3842b931cdac369651f59fbc83f43'
}

url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"

testfile = urllib.URLopener()
testfile.retrieve(url, "/tmp/30")
testfile.close()

print "The file was saved!"