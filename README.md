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
pip3.11 install poetry
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

Especially in option #2, two prompts are needed. One for client and the other for server. Please make sure select correct command options for each prompts.
After select option, follow the instructions follow.

# How to confirm Dependencies
All dependencies required for this project are listed in the **poetry.lock** file. You can also view them via the command line using the following command:
(Run this command in the project's root directory)
```
poetry show (--tree)
```
__--tree__ is option for visualizing dependencies via tree form.