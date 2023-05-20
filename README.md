# Python Grammer

## 1. Basic

- basic.py
- list.py
- tuple.py
- dict.py
- set.py
- comment.py

## 2. Flow

- if.py
- none.py
- while.py
- for.py

## 3. Func

- func.py
- docstring.py
- generator.py
- lambda.py
- namespace.py
- 표기.py
- error_handleing.py

## 4. Modules

- pyhton내에서 import, export 표준

### import 할때 주의 할 점

```
    // bad
    import collections, os, sys (x)

    // good
    import collections
    import os
    import sys

    import termcolor // third party library는 한줄띄워서 작성

    import config // 본인이 만든 package도 한줄띄워서 작성

    1. package 기재 순서 (알파벳 순서)
        - 파이썬 표준 라이브버리
        - 서드파티 라이브러리
        - 본인이 만든 라이브러리
        - 로컬 라이브러리
```

## 5. Class

- access.py
- class.py
- extends.py
- method.py

## 6. File

- file.py
- file_operator.py
- csv_parse.py
- tar_file.py
- temp_file.py
- template.py
- subprocess.py

## Roboter (mini project 1)

- 질답형 간단한 cli프로젝트

## Python Best Practice

- python_best_practice.py (파이썬 사용법)
- python_concepts.py (Pythonic 하게 코딩하기)

```
    // python lint tool
    pip install pep8 | pip install flake8 | pip install pylint

    // if install python3
    pip3 install --upgrade pip

    // check pip version
    pip -v

    // register pylint in vscode

    1. install extends pylint
    2. cmd + p
    3. "> python: select linter"
    4. enter > "pylint"
```

## application help

- python 에서 사용되는 외부 라이브러리
- config.py
- config_yml.py
- logger.py

## Email Sender (SMTP)

- 이메일 송신
