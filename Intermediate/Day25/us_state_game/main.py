import turtle
from time import sleep

import pandas
screen = turtle.Screen()
screen.title('U.S State Game')
screen_writer = turtle.Turtle()
screen_writer.hideturtle()
screen_writer.penup()

FONT = ('Arial', 10, 'normal')

def update_coodinates():
    data = pandas.read_csv('50_states.csv')
    countries = data['countries'].to_list()
    for country in countries:
        print(country)
        print('Move your mouse on the right place.')
        sleep(3)
        x = screen.cv.winfo_pointerx()
        y = screen.cv.winfo_pointery()
        print(x,y)

def show_state_name(name, x, y):
    screen_writer.goto(x, y)
    screen_writer.write(name, font=FONT, align='center')

states_guessed = []
image = 'blank_states_img.gif'
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
screen.addshape(image)
turtle.shape(image)
while len(states_guessed) < 52:
    answer_state = screen.textinput('Guess the country', 'Whats another countries name?').title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in states_guessed]

        data_dict = {'This states you did not guess': missing_states}
        data_1 = pandas.DataFrame(data_dict)
        data_1.to_csv('missed_states.csv')
        break

    if answer_state in data.state.to_list():
        row = data[data.state == answer_state]
        x_cor = row.x.item()
        y_cor = row.y.item()
        show_state_name(answer_state,x_cor, y_cor )
        states_guessed.append(answer_state)

states_not_guessed = data[data.state not in states_guessed]
print(states_not_guessed.to_list)











turtle.mainloop()

def get_mouse_position(x, y):
    print(x, y)

