# brique-test
This Repository is for brique coding test project.

Please read and follow below instructions.


# How To Run on macOS
## 1. Install Python Version >= 3.11
Ensure that a package manager like Homebrew is installed on your macOS. To install Python 3.11, run the following command:
```
brew install python@3.11
```
## 2. Install Poetry
Poetry is a tool for managing Python project dependencies and virtual environments. It helps manage library dependencies specified in the **pyproject.toml** file.

To install Poetry, you can use the following command:
```
curl -sSL https://install.python-poetry.org | python3 -
```

## 3. Initiating Poetry Virtual Environment
Once Poetry is installed, navigate to the project directory and initialize a new virtual environment:
```
poetry install
```

This command installs the dependencies listed in the **pyproject.toml** file and sets up a virtual environment.


## 4. Run application via poetry
After install dependencies, run project through given poetry virtual environment:
```
poetry run python3.11 run.py
```

## 5. Input option command
Please input your option command:
```
# 원하는 명령어를 입력하세요.
[1] 문제 1
[2] 문제 2
[3] 문제 3
[4] 문제 4
[5] 문제 5
[6] 문제 6
[7] 문제 7
[8] 문제 8
[e] 종료
```

after select option, follow the instructions follow.