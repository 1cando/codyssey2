
# quiz.py

class Quiz:
    """퀴즈 한 문제의 정보를 관리하는 클래스"""

    """__init__은 클래스로 객체를 만들 때 자동으로 실행되면서 객체의 초기 정보를 설정"""
    def __init__(self, question, choices, answer,
                 category="기타", explanation=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.category = category
        self.explanation = explanation

    def show_question(self):
        """문제와 선택지를 출력한다."""
        print(f"\n[{self.category}]")
        print(self.question)
        # enumerate() 순서와 값을 함께 가져오기
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    # enumerate(iterable, start=0)
    # iterable 반복할 대상 (리스트 등)
    # start 번호의 시작값 (기본값은 0)
    def check_answer(self, user_answer):
        """사용자가 입력한 답이 정답인지 확인한다."""
        return self.answer == user_answer

    def to_dict(self):
        """Quiz 객체를 JSON 저장에 적합한 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "category": self.category,
            "explanation": self.explanation
        }

    # 딕셔너리 데이터를 다시 Quiz 객체로 변환하는 메서드 
    # @classmethod는 클래스 자체를 첫 번째 인자로 전달받는 메서드 (객체를 만들기 전에 클래스 이름으로 호출) 
    # data.get("category", "기타") 카테고리 가져오기, 없으면 기타
    # data.get("explanation", "") 해설 가져오기, 없으면 빈 문자열
    # return cls() 생성한 Quiz 객체 반환
    @classmethod
    def from_dict(cls, data):
        """딕셔너리 데이터를 Quiz 객체로 변환한다."""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            category=data.get("category", "기타"),
            explanation=data.get("explanation", "")
        )
