import os

print("유튜브 주소 검색")

url = input()
url = '"' + url + '"'
command = "youtube-dl --extract-audio --audio-format mp3 %s" % url

os.chdir('/Users/zigje9/Desktop/mp3_down/download/')

os.system(command)

# https://www.youtube.com/watch?v=5EC3_-mhHp0
