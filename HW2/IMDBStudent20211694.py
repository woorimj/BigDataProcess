#!/usr/bin/python3
import sys

counts = {}
with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.strip()
        splits = line.split("::")  # '::'으로 세부분으로 나누기 (id, 영화제목, 장르)
        genre_list = splits[2].split("|")  # 영화장르 여러개인 경우 '|'로 나누기
        # # 해당 line의 장르만 추출되어서 저장되어있음(공백, 줄바꿈이 있었음)
        # print(genre_list)
        # for genre in genre_list:
        #     # genre = genre.strip()
        #     print(genre)
        for genre in genre_list:
            # genre = genre.strip()
            if genre in counts:
                counts[genre] += 1
            else:
                counts[genre] = 1

# 결과저장
with open(sys.argv[2], "w") as output:
    for genre, count in counts.items():
        output.write(f"{genre} {count}\n")
