
# quiz_game.py

import json
import random
# shutil은 파일을 복사하거나 이동할 때 사용하는 Python 모듈
import shutil
from pathlib import Path

from quiz import Quiz

# game = QuizGame() 객체를 생성할 때 QuizGame 코드 실행
class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""
    # __init__ 변수 초기화
    # """
    # Path() 파일이나 폴더 경로를 다루는 객체를 만듦
    # __file__ 현재 실행 중인 Python 파일의 경로
    # .resolve() 경로를 절대 경로로 변환
    # .parent 현재 파일이 들어 있는 폴더
    # / "state.json" 해당 폴더 안의 state.json 경로를 만듦
    # self.data_file = /Users/사용자/codyssey2/state.json
    # """
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.data_file = Path(__file__).resolve().parent / "state.json"
        self.backup_file = Path(__file__).resolve().parent / "state.json.bak"
        self.load_data()

    def create_default_quizzes(self):
        """처음 실행하거나 저장 데이터를 읽을 수 없을 때 사용할 기본 문제."""

        return [
            Quiz(
                "Python에서 변수의 역할은?",
                ["데이터를 저장하고 참조한다", "반복문을 실행한다",
                 "파일을 삭제한다", "프로그램을 종료한다"],
                1, "Python 기초",
                "변수는 값을 저장하고 이름으로 참조할 수 있게 해줍니다."
            ),
            Quiz(
                "다음 코드의 출력 결과는?\na = 10\nprint(type(a))",
                ["<class 'str'>", "<class 'int'>",
                 "<class 'float'>", "<class 'list'>"],
                2, "Python 기초",
                "10은 정수이므로 자료형은 int입니다."
            ),
            Quiz(
                "Python에서 여러 데이터를 순서대로 저장하고 수정할 수 있는 자료형은?",
                ["tuple", "str", "list", "bool"],
                3, "자료형",
                "list는 순서가 있고 값을 수정할 수 있는 자료형입니다."
            ),
            Quiz(
                "다음 코드의 출력 결과는?\nfor i in range(1, 4):\n    print(i)",
                ["0, 1, 2", "1, 2, 3", "1, 2, 3, 4", "2, 3, 4"],
                2, "반복문",
                "range(1, 4)는 1부터 3까지의 숫자를 생성합니다."
            ),
            Quiz(
                "while문에 대한 설명으로 올바른 것은?",
                ["조건이 참인 동안 반복한다", "반드시 1번만 실행된다",
                 "클래스를 생성한다", "파일을 저장한다"],
                1, "반복문",
                "while문은 조건식이 참인 동안 코드를 반복 실행합니다."
            ),
            Quiz(
                "다음 코드의 출력 결과는?\ndef add(a, b):\n    return a + b\nprint(add(3, 5))",
                ["35", "15", "8", "3"],
                3, "함수",
                "add 함수는 두 숫자의 합인 8을 반환합니다."
            ),
            Quiz(
                "Python 클래스에서 __init__ 메서드의 역할은?",
                ["반복문 실행", "객체 초기화", "파일 삭제", "정렬"],
                2, "클래스",
                "__init__은 객체가 생성될 때 초기화 작업을 수행합니다."
            ),
            Quiz(
                "클래스 메서드 안에서 self가 가리키는 것은?",
                ["부모 클래스", "현재 인스턴스", "모듈", "함수의 반환값"],
                2, "클래스",
                "self는 메서드를 호출한 현재 인스턴스를 가리킵니다."
            ),
            Quiz(
                "객체(Object)에 대한 설명으로 올바른 것은?",
                ["클래스로부터 생성된 실제 대상",
                 "반드시 숫자만 저장하는 변수",
                 "반복문을 의미하는 문법",
                 "파일 확장자"],
                1, "객체지향",
                "객체는 클래스라는 설계도를 바탕으로 생성됩니다."
            ),
            Quiz(
                "json.dump()의 역할은?",
                ["JSON 파일 읽기", "JSON 데이터 쓰기",
                 "파일 삭제", "화면 출력"],
                2, "파일 입출력",
                "json.dump()는 Python 데이터를 JSON 형식으로 파일에 씁니다."
            ),
            Quiz(
                "git add 명령어의 역할은?",
                ["원격 저장소 삭제", "커밋 기록 삭제",
                 "변경 파일을 스테이징 영역에 추가",
                 "브랜치 병합"],
                3, "Git",
                "git add는 커밋할 변경사항을 스테이징 영역에 올립니다."
            ),
            Quiz(
                "git clone과 git pull의 차이로 올바른 것은?",
                ["둘 다 파일을 삭제한다",
                 "clone은 저장소를 복제하고 pull은 기존 저장소에 변경사항을 가져온다",
                 "pull은 새 저장소를 만든다",
                 "clone은 커밋만 실행한다"],
                2, "Git",
                "clone은 원격 저장소를 처음 복제하고, pull은 기존 저장소를 업데이트합니다."
            )
        ]

# self.data_file 파일 경로
# .open() 해당 파일 열기
# "r" 읽기 모드(Read)
# encoding="utf-8" UTF-8 인코딩으로 읽기
# 열린 파일을 file이라는 변수로 사용
# data = json.load(file) => 열린 파일(file)의 JSON 내용을 읽어서 파이썬 자료형(딕셔너리)으로 변환
# with를 사용하면 해당 블록이 끝났을 때 파일을 자동으로 닫아줘서 직접 close()를 호출하지 않아도 된다. (파일을 안전하게 열고 사용하기 위한 문법)


    def load_data(self):
        """JSON 파일에서 퀴즈와 최고 점수를 불러온다."""

        # 저장 파일이 없으면 백업 파일을 먼저 확인한다.
        if not self.data_file.exists():
            if self.backup_file.exists():
                try:
                    self.quizzes, self.best_score = self.read_data(
                        self.backup_file
                    )
                    shutil.copy2(self.backup_file, self.data_file)
                    print("백업 파일을 이용하여 데이터를 복구했습니다.")
                    return

                except (OSError, json.JSONDecodeError,
                        KeyError, TypeError, ValueError) as error:
                    print(f"백업 파일을 불러오지 못했습니다: {error}")

            print("저장 데이터가 없습니다. 기본 퀴즈로 시작합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = 0
            self.save_data()
            return

        try:
            self.quizzes, self.best_score = self.read_data(self.data_file)

        except (OSError, json.JSONDecodeError,
                KeyError, TypeError, ValueError) as error:

            print(f"저장 데이터를 불러오지 못했습니다: {error}")

            # 백업 파일을 이용한 복구 시도
            if self.backup_file.exists():
                try:
                    self.quizzes, self.best_score = self.read_data(
                        self.backup_file
                    )
                    shutil.copy2(self.backup_file, self.data_file)
                    print("백업 파일을 이용하여 데이터를 복구했습니다.")
                    return

            # OSError 파일 관련 입출력 오류, 파일이 없거나 읽기 권한이 없는 경우
            # json.JSONDecodeError JSON 형식 오류, JSON 문법이 잘못된 경우
            # KeyError 딕셔너리에 없는 키를 조회할 때 발생
            # TypeError 자료형이 올바르지 않거나 연산이 불가능할 때 발생, 리스트가 와야 하는 곳에 문자열이 들어오는 경우
            # ValueError 값이 적절하지 않을 때 발생, int("hello")처럼 변환할 수 없는 값을 정수로 바꾸려는 경우
            # as error는 발생한 오류 객체를 error라는 변수에 저장
                except (OSError, json.JSONDecodeError,
                        KeyError, TypeError, ValueError) as backup_error:
                    print(f"백업 파일도 복구할 수 없습니다: {backup_error}")

            # 백업 파일도 사용할 수 없는 경우 기본 데이터로 초기화
            print("기본 퀴즈로 시작합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = 0
            self.save_data()


    def read_data(self, file_path):
        """JSON 파일을 읽고 퀴즈와 최고 점수를 반환한다."""

        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("저장 데이터 형식이 올바르지 않습니다.")

        if not isinstance(data.get("quizzes"), list):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")
        # 리스트 컴프리헨션(List Comprehension)이라는 문법이야. 반복문을 사용해서 리스트를 간결하게 만드는 방법
        # loaded_quizzes = []

        # for item in data["quizzes"]:
        # quiz = Quiz.from_dict(item)
        # loaded_quizzes.append(quiz)
        loaded_quizzes = [
            Quiz.from_dict(item) for item in data["quizzes"]
        ]
        # 딕셔너리.get("찾을 키", 기본값)
        loaded_best_score = data.get("best_score", 0)
        # isinstance()는 특정 변수의 자료형이 무엇인지 확인
        # not isinstance가 참이거나 뒤가 참이거나
        # raise 오류를 발생
        # ValueError 값이 올바르지 않을 때 사용하는 오류 종류
        # 괄호 안의 문장 : 오류가 발생한 이유를 설명하는 메시지
        if not isinstance(loaded_best_score, int) or loaded_best_score < 0:
            raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

        return loaded_quizzes, loaded_best_score

    def save_data(self):
        """현재 퀴즈와 최고 점수를 JSON 파일에 저장한다."""
        """quiz.to_dict() for quiz in self.quizzes를 풀어쓰면,"""
        # quiz_list = []
        # for quiz in self.quizzes:
        # quiz_list.append(quiz.to_dict())
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        # 임시 파일 경로
        temp_file = self.data_file.with_name(
        self.data_file.name + ".tmp"
        )
        # json JSON 기능을 제공하는 모듈
        # dump() 데이터를 JSON 형식으로 파일에 저장하는 함수
        # data 저장할 파이썬 데이터
        # file 데이터를 저장할 파일
        # ensure_ascii=False 한글을 유니코드 코드로 바꾸지 않고 그대로 저장(한글 유지)
        # indent=4 들여쓰기를 4칸으로 설정

        try:
            # 기존 저장 파일이 정상적인 경우 백업 파일 생성
            if self.data_file.exists():
                try:
                    self.read_data(self.data_file)
                    shutil.copy2(self.data_file, self.backup_file)

                except (OSError, json.JSONDecodeError,
                        KeyError, TypeError, ValueError):
                    print("기존 저장 파일이 손상되어 백업하지 않았습니다.")

            # 임시 파일에 새로운 데이터 저장
            with temp_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            # 저장이 완료되면 기존 파일을 새로운 파일로 교체
            temp_file.replace(self.data_file)

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")

            # 저장 실패 시 남아 있는 임시 파일 정리
            if temp_file.exists():
                temp_file.unlink()

    # input() => 입력값 받음, input(mes) => mes는 입력받기 전 출력 문구
    def get_input(self, message):
        """사용자 입력의 앞뒤 공백을 제거한다.(중간 공백은 제거 안됨)"""
        return input(message).strip()

    # continue는 현재 반복을 중단하고 while문의 처음으로 돌아감
    """
    try 일단 실행을 시도할 코드
    except 지정한 오류가 발생했을 때 실행할 코드
    else 오류 없이 try가 끝났을 때 실행할 코드
    finally 오류 발생 여부와 관계없이 마지막에 실행할 코드
    """
    def get_number(self, message, minimum, maximum):
        """범위 안의 숫자가 입력될 때까지 다시 입력받는다."""

        while True:
            value = self.get_input(message)

            if not value:
                print("입력값이 비어 있습니다. 다시 입력해 주세요.")
                continue

            try:
                number = int(value)
            except ValueError:
                print("숫자로 입력해 주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(f"{minimum}부터 {maximum} 사이의 숫자를 입력해 주세요.")

    def show_menu(self):
        """메인 메뉴를 출력한다."""

        print("\n========== CODE QUIZ ==========")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가하기")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("================================")

    def play_quiz(self):
        """등록된 퀴즈를 출제하고 점수를 계산한다."""

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        # 기존 문제를 복사해서 랜덤으로 섞고 보여주기
        # quiz_list = self.quizzes.copy()
        # random.shuffle(quiz_list)

        # 문제수 선택 및 랜덤 모듈 사용
        total_count = len(self.quizzes)

        print(f"\n현재 등록된 퀴즈: {total_count}문제")

        count = self.get_number(
            f"몇 문제를 풀까요? (1~{total_count}): ",
            1,
            total_count
        )

        quiz_list = random.sample(self.quizzes, count)       

        # 총 문제 개수 출력
        # f"..." 괄호 안의 내용을 화면에 출력 (f는 f-string이라는 기능)
        # \n은 줄바꿈
        print(f"\n총 {len(quiz_list)}문제를 시작합니다!") 
        
        for index, quiz in enumerate(quiz_list, start=1):
            print(f"\n[{index}/{len(quiz_list)}]")
            quiz.show_question()

            answer = self.get_number("정답 번호: ", 1, len(quiz.choices))

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

            if quiz.explanation:
                print(f"해설: {quiz.explanation}")

        print("\n========== 결과 ==========")
        print(f"점수: {score} / {len(quiz_list)}")

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

        print(f"최고 점수: {self.best_score}")
        self.save_data()

    def add_quiz(self):
        """새로운 퀴즈를 등록한다."""

        print("\n========== 퀴즈 추가 ==========")

        question = self.get_input("문제 내용: ")

        while not question:
            print("문제 내용을 입력해 주세요.")
            question = self.get_input("문제 내용: ")

        choices = []

        for index in range(1, 5):
            choice = self.get_input(f"{index}번 선택지: ")

            while not choice:
                print("선택지를 입력해 주세요.")
                choice = self.get_input(f"{index}번 선택지: ")

            choices.append(choice)

        answer = self.get_number("정답 번호(1~4): ", 1, 4)

        category = self.get_input("카테고리: ")
        if not category:
            category = "기타"

        explanation = self.get_input("정답 해설: ")

        new_quiz = Quiz(
            question, choices, answer, category, explanation
        )

        self.quizzes.append(new_quiz)
        self.save_data()

        print("새로운 퀴즈가 등록되었습니다!")

    def show_quizzes(self):
        """등록된 퀴즈 목록을 출력한다."""

        print("\n========== 퀴즈 목록 ==========")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. [{quiz.category}] {quiz.question}")

        print(f"\n총 {len(self.quizzes)}문제가 등록되어 있습니다.")

    def show_score(self):
        """최고 점수를 출력한다."""

        print("\n========== 최고 점수 ==========")
        print(f"최고 점수: {self.best_score}")
