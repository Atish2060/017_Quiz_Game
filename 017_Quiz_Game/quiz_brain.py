class QuizBrain():
    def __init__(self, q_list):
        self.que_num = 0
        self.que_list = q_list
        self.score = 0
        self.user_ans = ' '

    def next_que(self):
        self.user_ans = input(f" Q.no {self.que_num+1}: {self.que_list[self.que_num].que} (true/False): ")
        self.que_num += 1

    def que_continue(self):
        return self.que_num < len(self.que_list)

    def check_ans(self):
        answer = self.que_list[self.score].ans
        if self.user_ans.lower() != answer.lower():
            print(f"Your answer is incorrect. The correct ans is {answer}. Your score is: {self.score} / {self.que_num}")
        else:
            self.score += 1
            print(f"Your answer is correct. The correct ans is {answer}. Your score is: {self.score} / {self.que_num}")



