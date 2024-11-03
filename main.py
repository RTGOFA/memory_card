from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep        
app = QApplication([])
from main_window import *

from card_window import *
#імпортуємо усі об'єкти з інших файлів
card_win.setWindowTitle("Memory Card")

#клас для збереження одного питання
#містить в собі питання,правильну відповідь
class Question():
    def __init__(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.is_asking = True
        self.count_ask = 0
        self.count_right = 0

count_ask = 0
count_right = 0


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]#масив з кнопками
questions = [q1, q2, q3, q4]#масив з запитаннями


def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_correct.setText(cur_quest.answer)

    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.answer)
    radio_buttons[1].setText(cur_quest.wrong1)
    radio_buttons[2].setText(cur_quest.wrong2)
    radio_buttons[3].setText(cur_quest.wrong3)

new_question()
#перевірка на правильність відповіді
def check():
    global count_ask, count_right
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer in radio_buttons:
            if answer.text()== lbl_correct.text():
                count_ask += 1
                count_right += 1
                lbl_result.setText("Правильно!")
                answer.setChecked(False)
                break
            else:
                lbl_result.setText("Не правильно")
                count_ask += 1
    RadioGroup.setExclusive(True)

#перемикання від питання до відповіді
def switch_screen():
    if btn_ok.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()


        btn_ok.setText("Наступне запитання")
   
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()


        btn_ok.setText("Відповісти")
#приховування програми на заданий час
def rest():
    card_win.hide()
    n = box_min.value()
    sleep(n * 60)
    card_win.show()
#зміна вікна з карток на меню
def to_card():
    main_win.hide()
    card_win.show()

def back_menu():
    if count_ask == 0:
        c = 0
    else:
        c = (count_right / count_ask) * 100

    text = f"Всього відповідей: {count_ask}\n" \
            f"Правильних відповідей: {count_right}\n" \
            f"Успішність: {round(c, 2)}%"
    lbl_stat.setText(text)


    card_win.hide()
    main_win.show()
#очищення полей з 
def clear():
    le_quest.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
#додавання нового вікна
def add_question():
    new_q = Question(le_quest.text(),  le_right_ans.text(), le_wrong_ans1.text(),
                     le_wrong_ans2.text(), le_wrong_ans3.text())
    
    questions.append(new_q)
    clear()

btn_add_quest.clicked.connect(add_question)
#підключення подій до кнопки
btn_clear.clicked.connect(clear)
btn_ok.clicked.connect(switch_screen)
btn_back.clicked.connect(to_card)
btn_menu.clicked.connect(back_menu)
btn_sleep.clicked.connect(rest)

card_win.show() #показ вікна
app.exec_()     #запуск програми