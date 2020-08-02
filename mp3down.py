import os


def make_mp3():
    try:
        print("유튜브 주소 검색(mp3)")
        url = input()
        myurl = '"' + url + '"'
        command = "youtube-dl --extract-audio --audio-format mp3 %s" % myurl
        os.chdir('/Users/zigje9/Desktop/mp3_down/mp3/')
        os.system(command)
    except:
        print("에러 발생 주소를 다시확인하세요")

