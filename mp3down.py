import os


def make_mp3(urls):
    for url in urls:
        try:
            myurl = '"' + url + '"'
            command = "youtube-dl --extract-audio --audio-format mp3 %s" % myurl
            os.chdir('/Users/zigje9/Desktop/mp3_down/mp3/')
            os.system(command)
        except:
            print("에러 발생 주소를 다시확인하세요")

#https://www.youtube.com/watch?v=0Okrc8l1yYI
#https://www.youtube.com/watch?v=d3JPp_5kgO4
#https://www.youtube.com/watch?v=uFAKthN6BfQ