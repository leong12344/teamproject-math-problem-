import time
import random
import csv
import os

cnt = 0       # correct answer count
total_q = 0   # total questions asked (for endless mode)
life = 3 #lives
res = 0 #total tim
var = 0 #time for score
scr = 0 # score

#function for saving score into csv file
def save_score():
    filename = "score.csv"

    if not os.path.exists(filename): #if file does not exist
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Difficulty","Score","Time","Count"])

    rows = []
    score_for_dif_exist = False

    with open(filename, "r") as f: #open file
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)

        #checking if difficulty exists and updating best score, time, and count, instead of adding new rows infinitely
        for row in reader:
            difficulty = row[0]
            best_score = int(row[1])
            best_time = float(row[2])
            best_count = int(row[3])

            if difficulty == str(b):
                score_for_dif_exist = True
                if scr > best_score:
                    best_score = scr
                if cnt >= best_count:
                    best_count = cnt
                    if res < best_time:
                        best_time = res
                row = [difficulty,best_score,best_time,best_count]
            rows.append(row)

    #if difficulty does not exist, add new row
    if not score_for_dif_exist:
        rows.append([str(b),scr,res,cnt])

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

#function for printing best score, time, and count
def print_score():
    filename = "score.csv"
    rows = []

    #if file does not exist, this function will return None
    #without it program will return error
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)

        for row in reader:
            difficulty = row[0]
            best_score = int(row[1])
            best_time = float(row[2])
            best_count = int(row[3])
            if difficulty == []:
                break
            if difficulty == str(b):
                print(f"Your best time: {best_time}")
                if b == 4: #for endless mode
                    print(f"Your best score: {best_score}\n")
                else: #for difficulties
                    print(f"Your best score: {best_count}\n")


def ask_quest(n1, n2, n3):
    global cnt, life, scr, var, total_q

    correct = n1 * n2 * n3 #adding it for 3 difficulty and endless mode

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
        print(f"Correct answer was {correct}")
        if b == 4:
            life -= 1
            print(f"You lost one life! Remaining lives: {life}")

#function for difficulties in game
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

    res = round(end - start, 2)
    print(f"(총 소요시간 {res} 초)")


def endless_mode():
    global res, scr, life,total_q,var

    print("=========== ENDLESS MODE ============")
    print("You have 3 lives")

    while life > 0:
        if total_q < 10:
            low, high = 1, 10      # Easy: 1–10
            n3 = 1                 # 2-number multiplication
        elif total_q < 30:
            low, high = 1, 20     # Normal: 1–20
            n3 = 1                 # 2-number multiplication
        else:
            low, high = 1, 20     # Hard: 1–20
            n3 = random.randint(low, high)  # 3-number multiplication

        n1 = random.randint(low, high)
        n2 = random.randint(low, high)

        ask_quest(n1, n2, n3)
        res += round(var,2)

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
    print_score()
    func_for_diff()
    save_score()
elif b == 2:
    low, high = 1, 20
    print_score()
    func_for_diff()
    save_score()
elif b == 3:
    low, high = 1, 20
    print_score()
    func_for_diff()
    save_score()
elif b == 4:
    print_score()
    endless_mode()
    save_score()