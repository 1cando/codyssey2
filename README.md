# codyssey2
# Code Quiz — Python & Git Challenge

## 1. 프로젝트 소개

**Code Quiz**는 Python과 Git의 기본 개념을 학습하고 복습할 수 있도록 제작한 콘솔 기반 퀴즈 게임입니다.

사용자는 객관식 퀴즈를 풀고 점수를 확인할 수 있으며, 새로운 문제를 직접 추가할 수도 있습니다. 퀴즈와 최고 점수는 JSON 파일에 저장되어 프로그램을 종료한 후 다시 실행해도 유지됩니다.

## 2. 주제 선정 이유

이번 프로젝트에서는 Python과 Git을 주제로 퀴즈 게임을 제작했습니다.

프로젝트 과제를 수행하면서 학습한 Python 문법, 클래스와 객체, 파일 입출력, 예외 처리 및 Git 명령어를 다시 복습하고 싶었습니다.

또한 과제 이후 예정된 시험에 대비하여 학습 내용을 단순히 읽는 것에서 그치지 않고, 직접 문제를 풀면서 이해도를 확인할 수 있도록 기획했습니다.

## 3. 개발 환경

| 항목 | 사용 환경 |
|---|---|
| OS | macOS |
| Language | Python 3.10 이상 |
| IDE | Visual Studio Code |
| Version Control | Git / GitHub |
| Data Storage | JSON |
| Library | Python Standard Library |

## 4. 실행 방법

### 1) git 저장소 생성

```bash
# 깃 저장소 초기화
% git init

# 로컬 Git 저장소와 GitHub 원격 저장소를 연결
% git remote add origin https://github.com/[깃주소].git

# 깃 파일 생성
% touch main.py quiz.py quiz_game.py state.json .gitignore README.md

# 변경 파일 스테이징
% git add .

# 변경 사항 기록
% git commit -m "Initial commit"

# 현재 브랜치 이름을 main으로 변경
% git branch -M main

# 이후 push/pull의 기본 원격 브랜치 지정하여 GitHub에 업로드
% git push -u origin main
```

### 2) git 브랜치 생성 및 이동

```bash
# 브랜치 전환 및 생성
% git checkout -b feature/quiz-game
Switched to a new branch 'feature/quiz-game'

% git branch
* feature/quiz-game
  main
```

### 3) git 병합

```bash
% git checkout main
M       .gitignore
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

% git merge feature/quiz-game 
Updating e9486b0..f99370a
Fast-forward
 README.md    | 165 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------
 main.py      |  38 +++++++++++++++
 quiz.py      |  46 ++++++++++++++++++
 quiz_game.py | 284 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 510 insertions(+), 23 deletions(-)

 % git push origin main
Enumerating objects: 17, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 15 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 8.82 KiB | 8.82 MiB/s, done.
Total 12 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/[깃주소].git
   e9486b0..f99370a  main -> main
```

### 1) git 저장소 복제

```bash
# 원격 저장소 복제
# GitHub에 있는 codyssey2 저장소를 codyssey2-copy라는 새 폴더에 복제
% git clone https://github.com/[깃주소].git codyssey2-copy
Cloning into 'codyssey2'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
```

### 5) git 변경사항 가져오기

```bash
# GitHub 변경 사항 가져와 통합
% git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 1), reused 4 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 1.59 KiB | 543.00 KiB/s, done.
From https://github.com/1cando/codyssey2
   f99370a..00f9646  main       -> origin/main
Updating f99370a..00f9646
Fast-forward
 .gitignore |  8 ++++++++
 README.md  | 95 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-------------
```

### 5) git 기타 명령어

```bash
# 파일 변경상태 확인 
% git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

## 5. 주요 기능

### 필수 기능

- **퀴즈 풀기**: 등록된 객관식 문제를 풀고 정답 여부 확인
- **퀴즈 추가**: 새로운 문제와 선택지, 정답 등록
- **퀴즈 목록**: 등록된 문제 확인
- **최고 점수 확인**: 지금까지 기록된 최고 점수 확인
- **데이터 저장 및 불러오기**: JSON 파일을 이용한 데이터 영구 저장

### 추가 기능

- 문제별 카테고리 구분
- 정답 및 오답에 대한 해설 제공
- 랜덤 문제 출제
- 오답 복습 기능

※ 추가 기능은 실제 구현된 항목에 맞춰 유지합니다.

## 6. 파일 구조

```text
code-quiz/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
        ├── menu.png
        ├── play.png
        ├── add_quiz.png
        └── score.png
```

| 파일 | 설명 |
|---|---|
| `main.py` | 프로그램 실행 및 전체 흐름 관리 |
| `quiz.py` | 퀴즈 한 문제를 표현하는 Quiz 클래스 |
| `quiz_game.py` | 퀴즈 진행, 문제 추가, 점수 관리 등을 담당하는 QuizGame 클래스 |
| `state.json` | 퀴즈 데이터와 최고 점수 저장 |
| `README.md` | 프로젝트 설명 |
| `.gitignore` | Git 추적 제외 파일 설정 |
| `docs/screenshots/` | 프로그램 실행 화면 캡처 저장 |


## 7. 클래스 및 프로그램 구조

본 프로젝트는 객체지향 프로그래밍(OOP) 개념을 적용하여
Quiz 클래스와 QuizGame 클래스를 중심으로 구성했습니다.

각 클래스가 담당하는 역할을 분리하여 코드의 가독성과
유지보수성을 높이고, 기능별로 코드를 관리할 수 있도록 설계했습니다.

### 7-1. Quiz 클래스 (`quiz.py`)

Quiz 클래스는 퀴즈 한 문제를 표현하는 클래스입니다.

하나의 문제에 필요한 데이터와 해당 데이터를 처리하는 메서드를
하나의 클래스로 묶어 관리합니다.

**주요 속성(Attribute)**

| 속성 | 자료형 | 설명 |
|---|---|---|
| question | str | 퀴즈 문제 내용 |
| choices | list | 4개의 객관식 선택지 |
| answer | int | 정답 번호 (1~4) |
| category | str | 문제의 학습 카테고리 |
| explanation | str | 정답 및 오답에 대한 해설 |

**주요 메서드(Method)**

| 메서드 | 기능 |
|---|---|
| `__init__()` | 퀴즈 객체 생성 및 속성 초기화 |
| `show_question()` | 문제와 선택지 출력 |
| `check_answer()` | 사용자 답변과 정답 비교 |
| `to_dict()` | Quiz 객체를 딕셔너리로 변환 |
| `from_dict()` | 딕셔너리 데이터를 Quiz 객체로 변환 |

`__init__()`을 통해 문제마다 독립적인 Quiz 객체를 생성합니다.

`check_answer()`는 정답 여부를 Boolean 값(True/False)으로 반환하며,
`to_dict()`와 `from_dict()`는 JSON 파일에 데이터를 저장하고
불러오는 과정에서 사용합니다.

### 7-2. QuizGame 클래스 (`quiz_game.py`)

QuizGame 클래스는 퀴즈 게임의 전체적인 흐름과 데이터를 관리합니다.

여러 개의 Quiz 객체를 리스트 형태로 보관하고,
문제 출제부터 점수 계산, 신규 문제 등록, 데이터 저장까지 담당합니다.

**주요 속성(Attribute)**

| 속성 | 자료형 | 설명 |
|---|---|---|
| quizzes | list | Quiz 객체들을 저장하는 리스트 |
| best_score | int | 지금까지 기록한 최고 점수 |
| data_file | Path | JSON 데이터 파일의 경로 |

**주요 메서드(Method)**

| 메서드 | 기능 |
|---|---|
| `__init__()` | 게임 데이터 초기화 및 저장 데이터 불러오기 |
| `create_default_quizzes()` | 기본 퀴즈 데이터 생성 |
| `load_data()` | JSON 파일에서 퀴즈와 점수 불러오기 |
| `save_data()` | 퀴즈와 최고 점수를 JSON 파일에 저장 |
| `get_input()` | 사용자 입력값의 앞뒤 공백 제거 |
| `get_number()` | 숫자 입력 및 유효 범위 검증 |
| `show_menu()` | 메인 메뉴 출력 |
| `play_quiz()` | 퀴즈 출제, 정답 확인 및 점수 계산 |
| `add_quiz()` | 새로운 퀴즈 등록 |
| `show_quizzes()` | 등록된 퀴즈 목록 출력 |
| `show_score()` | 최고 점수 출력 |

QuizGame은 Quiz 클래스로 생성한 객체들을 관리합니다.

예를 들어 퀴즈를 추가하면 새로운 Quiz 객체를 생성하고,
이를 quizzes 리스트에 추가합니다.

퀴즈 진행 시에는 리스트에 저장된 Quiz 객체의
show_question()과 check_answer() 메서드를 호출하여
문제 출력과 정답 확인을 수행합니다.

### 7-3. main.py

main.py는 프로그램의 실행 진입점(Entry Point)입니다.

QuizGame 객체를 생성하고 메뉴를 반복해서 출력하며,
사용자가 선택한 메뉴에 따라 해당 기능을 호출합니다.

게임의 세부 기능은 QuizGame 클래스에 위임하여
main.py가 프로그램의 전체 실행 흐름에 집중하도록 구성했습니다.

주요 구성:
- `main()` 함수: 프로그램 실행 및 메뉴 반복 처리
- `QuizGame()` 객체 생성
- 조건문(if/elif)을 이용한 메뉴 분기
- 예외 처리(try/except/finally)를 통한 종료 및 데이터 저장

### 7-4. 객체지향 프로그래밍 적용

본 프로젝트에서는 다음과 같은 객체지향 프로그래밍 개념을 적용했습니다.

**1. 클래스와 객체**
- Quiz와 QuizGame 클래스를 정의했습니다.
- 클래스를 이용해 각각의 퀴즈 객체와 게임 객체를 생성합니다.

**2. 캡슐화**
- 퀴즈 데이터와 관련 기능을 Quiz 클래스 안에 모았습니다.
- 게임 진행과 데이터 관리 기능을 QuizGame 클래스 안에 모았습니다.
- 관련 데이터와 기능을 하나의 단위로 관리하도록 구성했습니다.

**3. 객체 간 협력**
- QuizGame 객체가 여러 Quiz 객체를 관리합니다.
- QuizGame은 Quiz 객체의 메서드를 호출하여 문제 출력과 정답 확인을 수행합니다.

**4. 책임 분리**
- Quiz는 개별 문제 관리에 집중합니다.
- QuizGame은 게임 전체 관리에 집중합니다.
- main.py는 프로그램 실행 흐름을 담당합니다.

### 7-5. 프로그램 실행 흐름

1. main.py 실행
2. QuizGame 객체 생성
3. state.json 파일 확인 및 데이터 불러오기
4. 메인 메뉴 출력
5. 사용자 메뉴 선택
6. 선택한 기능 실행
7. 퀴즈 진행 및 점수 계산
8. 데이터 변경 시 JSON 파일에 저장
9. 종료 시 데이터 저장 후 프로그램 종료


## 8. 데이터 저장 방식

퀴즈 데이터와 최고 점수는 프로젝트 루트 디렉터리의 `state.json` 파일에 JSON 형식으로 저장합니다.

예시:

```json
{
    "quizzes": [
        {
            "question": "Python에서 리스트의 자료형은?",
            "choices": ["int", "str", "list", "bool"],
            "answer": 3,
            "category": "Python 기초",
            "explanation": "list는 여러 데이터를 순서대로 저장하는 자료형입니다."
        }
    ],
    "best_score": 3
}
```

- `quizzes`: 등록된 퀴즈 목록
- `question`: 문제 내용
- `choices`: 객관식 선택지
- `answer`: 정답 번호
- `category`: 문제 카테고리
- `explanation`: 정답에 대한 해설
- `best_score`: 최고 점수

프로그램 실행 시 JSON 파일을 불러오고, 데이터가 변경되면 파일에 저장합니다. 파일이 없거나 데이터 형식이 올바르지 않은 경우에도 프로그램이 중단되지 않도록 예외 처리를 적용합니다.

## 9. 실행 화면

### 메인 메뉴
![메인 메뉴](docs/screenshots/menu.png)

### 퀴즈 진행
![퀴즈 진행](docs/screenshots/play.png)

### 퀴즈 추가
![퀴즈 추가](docs/screenshots/add_quiz.png)

### 최고 점수 확인
![최고 점수](docs/screenshots/score.png)

---

**Code Quiz — Learn, Practice, and Challenge Yourself!**