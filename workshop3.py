Boss = int(input("บอสสั่งให้ไปเก็บส่วยกี่ร้าน: "))
num = 0


for i in range(1, Boss+1):

    Cost = float(input(f"เก็บเงินจากร้านที่ {i}: "))
    num += Cost



print(f"จำนวนร้านที่เก็บ: {Boss}")
print(f"จำนวนเงินทั้งหมดที่เก็บได้: {num}")