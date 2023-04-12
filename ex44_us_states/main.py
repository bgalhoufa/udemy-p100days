import turtle
import pandas

full_states = pandas.read_csv('50_states.csv')
data_states = full_states['state'].tolist()
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

score = 0
game_is_on = True
correct_list = []

while game_is_on:
    answer = screen.textinput(title=f'{score}/50', prompt='What\'s another state\'s name?').title()
    if answer == 'Exit':
        break
    if answer in data_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = full_states[full_states.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        score += 1
        data_states.remove(answer)
        if score == 50:
            game_is_on = False


data_to_save = pandas.DataFrame(data_states)
data_to_save.to_csv('states_to_learn.csv')

turtle.mainloop()

