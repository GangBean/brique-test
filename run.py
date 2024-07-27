from problems import *;

OPTIONS = {
    '1': problem_1,
    '2': problem_2,
    '3': problem_3,
    '4': problem_4,
    '5': problem_5,
    '6': problem_6,
    '7': problem_7,
    '8': problem_8,
}

def retry(option: str):
    print(f"유효하지 않은 명령어 입니다. 다시 입력하세요: {option}")
    pass

def run():
    while True:
        print(f"""
# 원하는 명령어를 입력하세요.
[1] 문제 1
[2] 문제 2
[3] 문제 3
[4] 문제 4
[5] 문제 5
[6] 문제 6
[7] 문제 7
[8] 문제 8
[e] 종료""")
        option: str = input()
        if option in OPTIONS:
            OPTIONS[option]()
        elif option == 'e':
            print("종료합니다.")
            break
        else:
            retry(option)
    
if __name__ == '__main__':
    run()
