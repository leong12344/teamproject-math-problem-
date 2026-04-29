import random
import time

cnt = 0

#function for operations
def ask_quest(n1,n2,op):
    global cnt

    if op == "+":
        correct = n1 + n2
    elif op == "-":
        if n1 < n2:
            return
        correct = n1 - n2
    elif op == "x":
        correct = n1 * n2
    elif op == "/":
        if n1 % n2 != 0:
            return
        correct = n1 // n2
#checking if input is digit
#if not it would return previous operation
    while True:
        a = str(input(f"{n1} {op} {n2} ="))

        if not a.isdigit():
            print("숫자를 입력하십시오!")
            continue

        a = int(a)
        break

    if a == correct:
        print("정답입니다!")
        cnt += 1
    else:
        print("틀렸습니다.")

while True:
    b = input("Choose difficulty(1(easy),2(normal),3(hard))")

    if not b.isdigit():
        print("숫자를 입력해 주세요.")
        continue

    b = int(b)

    if b not in [1,2,3]:
        print("1,2,3 중에서 선택해 주세요.")
        continue
    break

if b == 1:
    low,high = 1,10
elif b == 2:
    low,high = 1,100
elif b == 3:
    low,high = 10,200
start = time.perf_counter()

for _ in range(5):
    while True:
        operation = random.choice(["+","-","x","/"])
        if b == 2:
            if operation in ["+","-"]:
                n1 = random.randint(low,high)
                n2 = random.randint(low,high)
            else:
                n1 = random.randint(2,9)
                n2 = random.randint(2,9)
        else:
            n1 = random.randint(low,high)
            n2 = random.randint(low,high)
        if operation == '-' and n1 < n2:
            continue
        if operation == '/' and n1 % n2 !=0:
            continue

        break
    ask_quest(n1, n2, operation)

end = time.perf_counter()

if cnt == 5:
    print("축하합니다. 면접입니다!")
elif 0 < cnt < 5:
    print(f"5문제에서 {cnt}개 맞췄습니다.")
else:
    print("모두 들렸습니다!")

print(f"(총 소요시간 {round(end-start,2)} 초)")