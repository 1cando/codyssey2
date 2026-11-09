
# main.py - 종료 처리 개선 버전

from quiz_game import QuizGame


def main():
    game = QuizGame()

    print("Code Quiz에 오신 것을 환영합니다!")

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

    except (KeyboardInterrupt, EOFError):
        print("\n종료 요청을 받았습니다.")

    finally:
        game.save_data()
        print("데이터 저장을 시도했습니다.")


if __name__ == "__main__":
    main()
