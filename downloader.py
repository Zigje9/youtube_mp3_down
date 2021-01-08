import mp3down
import video_down


def start(cursor):
    if cursor == "1":
        print("한줄로 입력")
        urls = list(input().split(","))
        mp3down.make_mp3(urls)

    if cursor == "2":
        video_down.make_video()


print("mp3 다운로드는 1, video 다운로드는 2를 선택하세요:")
cursor = input()
start(cursor)

# https://www.youtube.com/watch?v=5EC3_-mhHp0
# https://www.youtube.com/watch?v=lOrU0MH0bMk

# 입력형식:
# https://www.youtube.com/watch?v=00VK7fE8pts,https://www.youtube.com/watch?v=qtf4-D6V_2o
# https://www.youtube.com/watch?v=qKkmEscb6rg,https://www.youtube.com/watch?v=jwa3qtEgHME,https://www.youtube.com/watch?v=0VBdoHJe1gc
