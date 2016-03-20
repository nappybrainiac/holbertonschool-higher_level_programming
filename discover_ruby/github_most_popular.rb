# The purpose of this program is to get JSON data from
# Github (specifically the most popular Ruby projects)
# save them to a Ruby array and print the results to
# the console.

require 'open-uri'

#Hash to create the call.
extheaders = {
  'User-Agent' => 'Nappybrainiac',
  'Authorization' => 'token 1ab58e09acd3842b931cdac369651f59fbc83f43'
}

#Open the url & save it in a variable
popular = open('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')

#Read the string and save the result in a variable
result = popular.read

#Print the results to the console
puts result

# Written by, Nappybrainiac - ヽ(´∇´)ノ
# Holberton School Project (March 2016)
