# Python Grammer

## Basic

- basic.py
- list.py
- tuple.py
- dict.py
- set.py
- comment.py

## Flow

- if.py
- none.py
- while.py
- for.py

## Func

- func.py
- docstring.py
- generator.py
- lambda.py
- namespace.py
- 표기.py
- error_handleing.py

## Modules

- pyhton내에서 import, export 표준

## import 할때 주의 할 점

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
