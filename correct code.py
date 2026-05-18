import random
import time

cnt = 0
life =3
res = 0
var = 0
scr = 0

def ask_quest(n1,n2):
    global cnt
    global life

    while True:
        a = str(input(f"{n1} x {n2} = "))
        correct = n1*n2

        if not a.isdigit():
            print("숫자를 입력해주세요.")
            continue
        a=int(a)
        break
    if a == correct:
        print("정답입니다!")
        cnt += 1
        if b == 4:
            if var < 3:
                print("완벽하다!")
            elif var < 5:
                print("굳!")
            else:
                print("아쉬운게요.")

def func_for_diff():
    start = time.perf_counter()
    for _ in range(5):
        while True:
            n1 = random.randint(low,high)
            n2 = random.randint(low,high)
            break
        ask_quest(n1,n2)
    end = time.perf_counter()

    if cnt == 5:
        print("축하합니다. 면접입니다!")
    elif 0 < cnt < 5:
        print(f"5문제에서 {cnt}개 맞췄습니다.")
    else:
        print("모두 들렸습니다!")

    print(f"(총 소요시간 {round(end - start, 2)} 초)")

while True:
    b = input("Choose difficulty(1(easy),2(normal),3(hard)),4(endless mode)")

    if not b.isdigit():
        print("숫자를 입력해 주세요.")
        continue

    b = int(b)

    if b not in [1,2,3,4]:
        print("1,2,3,4 중에서 선택해 주세요.")
        continue
    break

if b == 1:
    low,high = 1,10
    func_for_diff()
elif b == 2:
    low,high = 1,20
    func_for_diff()
elif b == 3:
    low,high = 10,200
    func_for_diff()
elif b == 4:
    endless_mode()
