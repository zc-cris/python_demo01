# zc-cris


class QuestionHandler():
    '''一个用于匿名问题处理的类'''

    def __init__(self, question):
        self.question = question
        self.response_list = []

    def show_question(self):
        print(self.question)

    def store_single_response(self, response):
        self.response_list.append(response)

    def show_responses(self):
        for i in self.response_list:
            print(i)
