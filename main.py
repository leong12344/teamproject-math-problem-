import random
import time

cnt = 0

start = time.perf_counter()

#Creating 2 random numbers and checking the answer
for _ in range(5):
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    if n1 * n2 <10:
        a = str(input(f"{n1} x {n2} =  "))
    else:
        a = str(input(f"{n1} x {n2} = "))
    if a.isdigit() == 0:
        print("숫자를 입력하십시오.")
    else:
        a = int(a)
    if a == n1 * n2:
        print("정답입니다!")
        cnt += 1
    else:
        print("틀렸습니다.")

end = time.perf_counter()

if cnt == 5:
    print("축하합니다. 면접입니다!")
elif 0 < cnt < 5:
    print(f"5문제에서 {cnt}개 맞췄습니다.")
else:
    print("모두 들렸습니다!")

print(f"(총 소요시간 {round(end-start,2)} 초)")