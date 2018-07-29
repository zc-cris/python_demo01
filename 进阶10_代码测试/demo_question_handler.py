# zc-cris
from question_handler import QuestionHandler


def single_question():
    print("你可以输入q来退出")
    question = '你最爱的开发语言是什么？'
    question_handler = QuestionHandler(question)
    while 1:
        question_handler.show_question()
        response = input("language: ")
        if response.lower() == 'q':
            break
        if response.strip():
            question_handler.store_single_response(response)
        else:
            print('输入有误')
    print()
    question_handler.show_responses()


single_question()
