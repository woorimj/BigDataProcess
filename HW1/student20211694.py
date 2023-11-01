#!/usr/bin/python3

from openpyxl import load_workbook

wb = load_workbook(filename="student.xlsx")
sheet = wb.active

students = sheet.max_row - 1  # header값 빼고 총 학생 수 구하기
aStu = int(students * 0.3)
bStu = int(students * 0.7)
bplusStu = int(bStu * 0.5)
cStu = students - aStu - bStu

for row in range(2, sheet.max_row + 1):
    total = sheet.cell(row=row, column=7).value  # total값 계산한거 가져오기

    # 40점 미만이면 F학점
    if total < 40:
        grade = "F"
    else:
        if aStu > 0:
            grade = "A+"
            aStu -= 1
        elif aStu == 0 and bplusStu > 0:
            grade = "A0" if aStu == 0 else "B+"
            bplusStu -= 1
        elif bStu > 0:
            grade = "B0"
            bStu -= 1
        elif bStu == 0 and bplusStu > 0:
            grade = "B+" if bStu == 0 else "C+"
            bplusStu -= 1
        else:
            grade = "C0" if cStu > 0 else "C"

    sheet.cell(row=row, column=8, value=grade)

wb.save("student.xlsx")
