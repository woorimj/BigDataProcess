#!/usr/bin/python3

result = []
weekDay = "MON/TUE/WED/THU/FRI/SAT/SUN"
with open("uber_exp.txt", "r") as input:
    for line in input:
        splits = line.split(",")

        baseNumber = splits[0]
        date = splits[1].split("/")  # [month, day, year] 리스트 분할
        vehicles = splits[2]
        trips = splits[3]

        day = int(date[1])  # 해당 day

        # input 파일에 1~15까지 있음
        if 1 <= day <= 15:
            week = weekDay.split("/")  # 해당 요일 문자열로 줌
            day = week[(day - 1) % 7]

        output = f"{baseNumber},{day} {vehicles},{trips}"

        result.append(output)

# 결과를 "uberoutput.txt"에 저장
with open("uberoutput.txt", "w") as output:
    output.writelines(result)
