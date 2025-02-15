import turtle, pandas
from write_state import WriteState

# create a screen
screen = turtle.Screen()
screen.title("U.S. States Game")
usa_image = r"./data/blank_states_img.gif"
print(usa_image)
screen.addshape(usa_image)
screen.setup(735, 495)
turtle.shape(usa_image)

# read data from file and save to a list
data = pandas.read_csv("./data/50_states.csv")
state_list = data["state"].to_list()
ycor_list = data["y"].to_list()
xcor_list = data["x"].to_list()

guessed_list = []

score = 0
while score != 50:
    answer = screen.textinput(prompt="What's another state name?", title=f"{score}/50 States Correct").title()

    for index in range(len(state_list)):

        if answer == state_list[index]:
            score += 1
            guessed_list.append(state_list[index])
            write_state = WriteState(state_list[index], xcor_list[index], ycor_list[index])

screen.exitonclick()

# Get Coordinates first
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
