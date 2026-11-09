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

### 1) 저장소 복제

```bash
% git clone https://github.com/1cando/codyssey2.git
Cloning into 'codyssey2'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.

```

### 2) 프로젝트 폴더 이동

```bash
cd codyssey2
```

### 3) 프로그램 실행

```bash
python3 main.py
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

## 7. 클래스 구성

### Quiz 클래스

퀴즈 한 문제의 정보를 관리합니다.

- 문제 내용
- 선택지
- 정답
- 카테고리
- 해설

문제 출력과 정답 확인 등의 기능을 담당합니다.

### QuizGame 클래스

퀴즈 게임 전체를 관리합니다.

- 메뉴 출력 및 선택
- 퀴즈 진행
- 신규 퀴즈 등록
- 퀴즈 목록 출력
- 점수 계산 및 최고 점수 관리
- JSON 파일 저장 및 불러오기

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