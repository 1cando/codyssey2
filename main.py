
# main.py - 종료 처리 개선 버전
"""
quiz_game: 가져올 기능이 들어 있는 파이썬 파일 이름
QuizGame: 그 파일 안에 정의되어 있는 클래스 이름
"""
from quiz_game import QuizGame


def main():
    game = QuizGame()

    print("Code Quiz에 오신 것을 환영합니다!")
   
    """
    try는 프로그램을 실행하다가 특정 오류가 발생할 가능성이 있는 코드를 감싸는 문법
    오류가 발생하면 아래쪽에 있는 except에서 처리
    while은 조건이 참인 동안 반복하는 반복문

    True는 항상 참이므로, 별도로 반복을 멈추지 않으면 계속 실행 (무한 반복)
    => 사용자가 퀴즈를 한 번 풀고 끝내는 게 아니라, 퀴즈도 풀고 목록도 확인하고 점수도 확인할 수 있도록 메뉴를 계속 보여줘야 하기 때문
    
    if: 첫 번째 조건 확인
    elif: 앞의 조건이 거짓이면 다음 조건 확인
    ==: 왼쪽과 오른쪽의 값이 같은지 비교
    break: 반복문 종료 (사용자가 5번을 누르면 게임 종료)
    """

    try:
        while True:
            game.show_menu()
            choice = game.get_number("메뉴 선택: ", 1, 5)

            if choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                game.show_quizzes()
            elif choice == 4:
                game.show_score()
            elif choice == 5:
                print("게임을 종료합니다.")
                break

    # """
    # ① KeyboardInterrupt
    # 일반적으로 터미널에서 Control + C를 눌렀을 때 발생, 프로그램을 강제로 중단하려는 상황
    
    # ② EOFError
    # 입력받는 도중 더 이상 입력할 수 없는 상황에서 발생, 터미널에서 Control + D를 누르는 경우가 대표적
    # Control + D 는 현재 입력이 끝났다는 신호(EOF, End Of File)를 보내는 단축키
    # """
    except (KeyboardInterrupt, EOFError):
        print("\n종료 요청을 받았습니다.")

    # """
    # finally는 try에서 오류가 발생했는지 여부와 관계없이 예외 처리 흐름이 끝날 때 실행되는 영역
    # 사용자가 어떤 방식으로 프로그램을 종료하더라도 데이터를 저장하도록 하기 위해서 작성
    
    # ① game.save_data()
    # 지금까지 변경된 퀴즈나 최고 점수를 state.json에 저장하는 메서드.
    # 예를 들어 사용자가 새로운 퀴즈를 추가했거나 최고 점수를 갱신했다면 해당 내용을 저장.

    # ② print()
    # 저장 작업을 시도했다는 메시지를 출력.
    # 다만 저장이 실제로 성공했는지는 save_data() 내부의 오류 처리 결과에 달려 있음.
    # 참고로 finally는 정상적으로 5번을 눌러 종료해도 실행되고, KeyboardInterrupt나 EOFError가 발생해도 실행.
    # """
    finally:
        game.save_data()
        print("데이터 저장을 시도했습니다.")


'''
이 파일을 직접 실행했을 때만 main() 함수를 실행
'''
if __name__ == "__main__":
    main()