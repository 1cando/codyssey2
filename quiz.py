
# quiz.py

class Quiz:
    """퀴즈 한 문제의 정보를 관리하는 클래스"""

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

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

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
