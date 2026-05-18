import time
import random

cnt = 0       # correct answer count
total_q = 0   # total questions asked (for endless mode)
life = 3 #lives
res = 0 #total tim
var = 0 #time for score
scr = 0 # score

def ask_quest(n1, n2, n3):
    global cnt, life, scr, var, total_q

    correct = n1 * n2 * n3

    start = time.perf_counter()

    while True:
        if b == 3 or (b == 4 and n3 > 1):
            a = str(input(f"{n1} x {n2} x {n3} = "))
        else:
            a = str(input(f"{n1} x {n2} = "))

        if not a.isdigit():
            print("숫자를 입력해주세요.")
            continue

        a = int(a)
        break

    end = time.perf_counter()
    var = round(end - start, 2)

    total_q += 1  # total count

    if a == correct:
        print("정답입니다.")
        cnt += 1
        if b == 4:
            if cnt < 10:  # Easy: generous time limits
                perfect, good = 3, 6
            elif cnt < 30:  # Normal: moderate time limits
                perfect, good = 5, 9
            else:  # Hard: tight time limits
                perfect, good = 8, 13

            if var < perfect:
                print("Perfect score!")
                scr += 10
            elif var < good:
                print("Good score!")
                scr += 5
            else:
                print("Bad Score!")
                scr += 1
    else:
        print("틀렸습니다.")
        if b == 4:
            life -= 1
            print(f"Correct answer was {correct}")
            print(f"You lost one life! Remaining lives: {life}")


def func_for_diff():
    global res
    start = time.perf_counter()
    for _ in range(5):
        n1 = random.randint(low, high)
        n2 = random.randint(low, high)
        n3 = random.randint(low, high) if b == 3 else 1
        ask_quest(n1, n2, n3)
    end = time.perf_counter()

    if cnt == 5:
        print("축하합니다. 면접입니다!")
    elif 0 < cnt < 5:
        print(f"5문제에서 {cnt}개 맞췄습니다.")
    else:
        print("모두 틀렸습니다!")

    print(f"(총 소요시간 {round(end - start, 2)} 초)")


def endless_mode():
    global res, scr, life

    print("=========== ENDLESS MODE ============")
    print("You have 3 lives")

    while life > 0:
        if cnt < 10:
            low, high = 1, 10      # Easy: 1–10
            n3 = 1                 # 2-number multiplication
        elif cnt < 30:
            low, high = 1, 20     # Normal: 1–20
            n3 = 1                 # 2-number multiplication
        else:
            low, high = 1, 20     # Hard: 1–20
            n3 = random.randint(low, high)  # 3-number multiplication

        n1 = random.randint(low, high)
        n2 = random.randint(low, high)

        ask_quest(n1, n2, n3)
        res += var

    print("\n게임오버!")
    print(f"You answered {total_q} questions.")
    print(f"Correct answers: {cnt}")
    print(f"Total score: {scr}")
    print(f"(총 소요시간 {round(res, 2)} 초)")


# --- Main ---
while True:
    b = input("Choose difficulty (1=easy, 2=normal, 3=hard, 4=endless): ")

    if not b.isdigit():
        print("숫자를 입력해 주세요.")
        continue

    b = int(b)

    if b not in [1, 2, 3, 4]:
        print("1,2,3,4 중에서 선택해 주세요.")
        continue
    break

if b == 1:
    low, high = 1, 10
    func_for_diff()
elif b == 2:
    low, high = 1, 20
    func_for_diff()
elif b == 3:
    low, high = 1, 20
    func_for_diff()
elif b == 4:
    endless_mode()