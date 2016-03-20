# The purpose of this program is to get JSON data from
# Github (specifically the most popular Ruby projects)
# and print the full name of the projects in a list
# on the console.

require 'open-uri'
require 'json'

#Hash to create the call.
extheaders = {
  'User-Agent' => 'Nappybrainiac',
  'Authorization' => 'token 1ab58e09acd3842b931cdac369651f59fbc83f43'
}

#Open the url & save it in a variable
popular = open('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')

#Read the string and save the result in a variable
result = popular.read

#Parse the JSON string for the items array (which you can find
#by going to the  URL specified).
string = JSON.parse(result)['items']

#Save the hashes "full_name" in a variable using the #map
#method.
names = string.map {|full| full["full_name"]}

#Print the result to the console, and join the individual items
#using '\n' for a new line.
puts names.join("\n")

# Written by, Nappybrainiac - ヽ(´∇´)ノ
# Holberton School Project (March 2016)
