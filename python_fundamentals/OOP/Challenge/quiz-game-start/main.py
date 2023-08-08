from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain


# Create Question Object for each data in question_data and append to question_bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text,question_answer)
    question_bank.append(new_question)
    # print(f'text = {question_data[item]["text"]} \n answer = {question_data[item]["answer"]}')

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the  quiz !")
print(f'Your final socre is: {quiz.user_score}/{quiz.question_number}')