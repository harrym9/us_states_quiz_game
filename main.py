import turtle

game_screen = turtle.Screen()
usa_image = r"./data/blank_states_img.gif"
print(usa_image)
game_screen.addshape(usa_image)
game_screen.setup(735,495)
turtle.shape(usa_image)





game_screen.exitonclick()

# Get Coordinates
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
