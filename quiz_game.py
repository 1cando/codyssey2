
# quiz_game.py

import json
from pathlib import Path

from quiz import Quiz


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.data_file = Path(__file__).resolve().parent / "state.json"

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

    def load_data(self):
        """JSON 파일에서 퀴즈와 최고 점수를 불러온다."""

        if not self.data_file.exists():
            self.quizzes = self.create_default_quizzes()
            self.save_data()
            return

        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            loaded_quizzes = [
                Quiz.from_dict(item) for item in data["quizzes"]
            ]
            loaded_best_score = data.get("best_score", 0)

            if not isinstance(loaded_best_score, int) or loaded_best_score < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")

            self.quizzes = loaded_quizzes
            self.best_score = loaded_best_score

        except (OSError, json.JSONDecodeError, KeyError,
                TypeError, ValueError) as error:
            print(f"저장 데이터를 불러오지 못했습니다: {error}")
            print("기본 퀴즈로 시작합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = 0

    def save_data(self):
        """현재 퀴즈와 최고 점수를 JSON 파일에 저장한다."""

        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError as error:
            print(f"데이터 저장에 실패했습니다: {error}")

    def get_input(self, message):
        """사용자 입력의 앞뒤 공백을 제거한다."""
        return input(message).strip()

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

        print(f"\n총 {len(self.quizzes)}문제를 시작합니다!")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{len(self.quizzes)}]")
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
        print(f"점수: {score} / {len(self.quizzes)}")

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
