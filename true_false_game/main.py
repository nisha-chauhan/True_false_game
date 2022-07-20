from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(q_list=question_bank)
game_on = True
while game_on:
    quiz.still_has_question()
    quiz.next_question()

print(f"your final score is {quiz.score}/{len(question_bank)}")
print("game Ended")
