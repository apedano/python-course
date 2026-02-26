import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()        # Hide the turtle icon
pen.penup()             # Prevent drawing lines
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()


FONT = ("Courier", 10, "normal")

def get_mouse_click_point(x, y):
    print(x,y)


def load_states_data():
    return pd.read_csv("50_states.csv")


def print_state_on_map(answer, x, y):
    print(f"Printing {answer} in position {x},{y}")
    pen.goto(x, y)
    pen.write(answer.title(), align="center", font=FONT)



def update_score(score):
    score_pen.goto(0, 250)
    score_pen.clear()  # Remove old text
    score_pen.write(f"Score: {score} /50", align="center", font=FONT)



def handle_answer(answer, states_df):
    state_series = states_df[states_df["state"] == answer.title()]
    if state_series.empty:
        return False
    else:
        print_state_on_map(answer, state_series["x"].to_list()[0], state_series["y"].to_list()[0])
        return True



def play_game():
    score = 0
    guesses_states = []
    states_df = load_states_data()
    continue_game = True
    while continue_game:
        #turtle.onscreenclick(get_mouse_click_point)
        answer_state = screen.textinput(title="Guess the State", prompt="What is the State's name?")
        continue_game = handle_answer(answer_state, states_df)
        if continue_game and (not answer_state in guesses_states):
            score += 1
            guesses_states.append(answer_state)
        update_score(score)
    else:
        print("Game Over")

play_game()
turtle.mainloop() #keeps the window open
#screen.exitonclick()