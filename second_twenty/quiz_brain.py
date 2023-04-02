class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        my_question = self.question_list[self.question_number]
        self.question_number += 1
        my_answer = input(f'Q.{self.question_number}: {my_question.text} (True/False)?: ')
        self.check_answer(my_answer, my_question.answer)

    def check_answer(self, my_answer, correct_answer):
        if my_answer.lower() == correct_answer.lower():
            self.score += 1
            print('That\'s correct')
        else:
            print('You\'re wrong')
            print(f'The correct answer is {correct_answer}')
        print(f'Your score is {self.score}/{self.question_number}')
        print('\n')