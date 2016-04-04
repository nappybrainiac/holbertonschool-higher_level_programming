# This python script calls GitHub's URL that exposes the most popular Python projects on GitHub.

from urllib2 import Request, urlopen

request_headers = {
  'User-Agent': 'nappybrainiac',
  'Authorization': 'token 1ab58e09acd3842b931cdac369651f59fbc83f43'
}

url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
request = Request(url, headers=request_headers)

print urlopen(request).read()
