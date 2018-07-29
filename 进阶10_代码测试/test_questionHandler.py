from unittest import TestCase

from question_handler import QuestionHandler


# zc-cris
class TestQuestionHandler(TestCase):

    # setUp 方法专门用来提前为测试方法做准备，例如提前生成好测试的对象等，方便后续测试使用
    def setUp(self):
        question = "你最喜爱的开发语言是？"
        question_handler = QuestionHandler(question)
        self.question_handler = question_handler
        self.responses = ['java', 'go', 'python']

    def test_store_single_response(self):
        '''测试存储用户的单个答案'''
        self.question_handler.store_single_response(self.responses[0])
        self.assertIn('java', self.question_handler.response_list)

    def test_store_more_response(self):
        '''测试存储用户的多个回答'''
        for i in self.responses:
            self.question_handler.store_single_response(i)

        for i in self.responses:
            self.assertIn(i, self.question_handler.response_list)
