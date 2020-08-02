import mp3down
import video_down


def start(cursor):
    if cursor == "1":
        mp3down.make_mp3()

    if cursor == "2":
        video_down.make_video()


print("mp3 다운로드는 1, video 다운로드는 2를 선택하세요:")
cursor = input()
start(cursor)

# https://www.youtube.com/watch?v=5EC3_-mhHp0
# https://www.youtube.com/watch?v=lOrU0MH0bMk