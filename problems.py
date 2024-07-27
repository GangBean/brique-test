import requests
import gdown
import os
import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import Error

def problem_1(file_url='https://drive.google.com/uc?id=1Ah0gkauGCIqJHpFGhTgsEZCjYFRscjTh', filename='sample.csv'):
    print("# problem 1")
    if not os.path.exists(filename):
        print("Downloading sample.csv through gdown...")
        gdown.download(file_url, filename, quiet=False)
    file = open(filename)

    total_number_of_lines: int = 0
    calculated_lines: int = 0
    error_values: list[str] = []
    def calculate(line: str, error_values) -> int:
        try:
            items: list[str] = line.split(',')
            numbers: list[int] = [int(item.strip()) for item in items]
            print(f"{min(numbers)} {max(numbers)} {sum(numbers)} {np.mean(numbers)} {np.std(numbers)} {np.median(numbers)}")
            return 1
        except ValueError:
            error_values.append(line)
            return 0
        
    for line in file.readlines():
        calculated_lines += calculate(line, error_values)
        total_number_of_lines += 1
        
    print(f"""---------------------------------------------
The total number of lines: {total_number_of_lines}
The calculated lines: {calculated_lines}
The error values: {error_values} / {len(error_values)} 개
""")

def problem_2():
    print("# problem 2")
    pass

def problem_3():
    print("# problem 3")
    try:
        connection = mysql.connector.connect(
            host= 'codingtest.brique.kr',
            user= 'codingtest',
            password= '12brique!@',
            database= 'employees',
        )

        if connection.is_connected():
            print("Successfully connected to MariaDB")

            # 커서를 생성하고 SQL 쿼리를 실행할 수 있습니다.
            cursor = connection.cursor()
            sql: str = """
               SELECT e.emp_no
                    , e.first_name
                    , e.last_name
                    , e.gender
                    , e.hire_date
                    , d.dept_name
                    , t.title
                    , ms.max_salary
                    # , s.from_date
                    # , s.to_date
                    # , t.from_date
                    # , t.to_date
                FROM employees e
                JOIN salaries s ON s.emp_no = e.emp_no
                JOIN (SELECT emp_no
                        , MAX(salary) AS max_salary 
                        FROM salaries 
                       GROUP BY emp_no) ms 
                  ON s.emp_no = ms.emp_no 
                 AND s.salary = ms.max_salary
                JOIN dept_emp de ON de.emp_no = e.emp_no
                JOIN departments d ON d.dept_no = de.dept_no
                JOIN titles t ON t.emp_no = e.emp_no
                 AND t.from_date <= s.from_date
                 AND t.to_date >= s.to_date
               WHERE DATE_FORMAT(e.hire_date, '%Y') >= '2000'
               ORDER BY e.emp_no
            ;
            """
            cursor.execute(sql)
            results = cursor.fetchall()

            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(results, columns=columns)
            print(df.to_string(index=False))

    except Error as e:
        print(f"데이터 베이스 처리 중 오류가 발생했습니다: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

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
