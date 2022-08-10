from microbit import *

# display.show(Image.HAPPY)

my_image01 = Image("09090:"
                   "09090:"
                   "00000:"
                   "09990:"
                   "90009")

my_image02 = Image("00000:"
                   "09090:"
                   "00000:"
                   "09990:"
                   "90009")

display.show(my_image01)
sleep(1000)
display.show(my_image02)