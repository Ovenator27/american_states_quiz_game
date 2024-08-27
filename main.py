import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

state_data = pandas.read_csv("50_states.csv")
correct_guesses = []

game_over = False

while not game_over and len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name another state")
    if answer_state == None:
        game_over = True
    elif answer_state.title() in state_data.state.values and answer_state not in correct_guesses:
        state = state_data[state_data.state == answer_state.title()]
        x_cor = int(state.x.iloc[0])
        y_cor = int(state.y.iloc[0])
        pen.goto(x_cor, y_cor)
        pen.write(state.state.item())
        correct_guesses.append(state.state.item())
    
remaining_states = {
    "State": []
    }

for state in state_data.state.values:
    if state not in correct_guesses:
        remaining_states["State"].append(state)

df = pandas.DataFrame(remaining_states)
df.to_csv("remaining_states.csv")
screen.exitonclick()