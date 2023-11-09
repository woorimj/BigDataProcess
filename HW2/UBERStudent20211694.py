#!/usr/bin/python3
import datetime
import sys

result = []
weekDay = "MON/TUE/WED/THU/FRI/SAT/SUN"
with open(sys.argv[1], "r") as input:
    for line in input:
        splits = line.split(",")

        baseNumber = splits[0]
        date = splits[1].split("/")  # [month, day, year] 리스트 분할
        vehicles = splits[2]
        trips = splits[3]

        week = weekDay.split("/")
        day = int(date[1])  # 해당 day

        day = week[datetime.date(int(date[2]), int(date[0]), int(date[1])).weekday()]

        # # input 파일에 1~15까지 있음
        # if 1 <= day <= 15:
        #     week = weekDay.split("/")  # 해당 요일 문자열로 줌
        #     day = week[(day - 1) % 7]

        output = f"{baseNumber},{day}", f"{vehicles},{trips}"
        result.append(output)

with open(sys.argv[2], "w") as output:
    for r in result:
        output.write(" ".join(r))
