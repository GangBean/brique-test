import requests

def problem_1():
    print("# problem 1")
    pass

def problem_2():
    print("# problem 2")
    pass

def problem_3():
    print("# problem 3")
    pass

def problem_4():
    print("# problem 4")
    pass

def problem_5(num=100, url='http://codingtest.brique.kr:8080/random'):
    print("# problem 5: please wait for output...")
    map = {}
    for _ in range(num):
        response =requests.get(url)
        map.update({response.text:(map[response.text] if response.text in map else 0) + 1})
    sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
    total_count = 0
    for text, count in sorted_map.items():
            print(f"count: {count} {text}")
            total_count += count
    assert(total_count == num)
    print(f"\nTotal count: {total_count}")

def problem_6():
    print("# problem 6: please input tops heights...")
    tops = input().split(' ')
    tops = [int(top) for top in tops]
    answer = []
    for i in range(len(tops)):
            l = [left+1 for left in range(i) if tops[left] > tops[i]]
            answer.append(str(max(l)) if len(l) > 0 else '0')
    print(' '.join(answer))

def problem_7():
    print("# problem 7")
    pass

def problem_8():
    print("# problem 8")
    pass
