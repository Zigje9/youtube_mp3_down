import os


def make_video():
    try:
        print("유튜브 주소 검색(비디오)")
        url = input()
        myurl = '"' + url + '"'
        command = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' %s" % myurl
        os.chdir('/Users/zigje9/Desktop/mp3_down/video/')
        os.system(command)
    except:
        print("에러 발생 주소를 다시확인하세요")



# https://www.youtube.com/watch?v=5EC3_-mhHp0
# https://www.youtube.com/watch?v=lOrU0MH0bMk