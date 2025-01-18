from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
que_list = []
for que in question_data:
    question = que['text']
    ans = que['answer']
    new_que = Question(question, ans)
    que_list.append(new_que)

a = QuizBrain(que_list)
while a.que_continue():
    a.next_que()
    a.check_ans()
print(f"\nCongratulations you have completed the quiz. The final socore is {a.score}/{a.que_num}")



