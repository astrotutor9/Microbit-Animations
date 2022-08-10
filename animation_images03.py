from microbit import *

# display.show(Image.HAPPY)

# create first image, LED 0 off, 9 on full
# and any values inbetween
my_image01 = Image("00000:"
                   "09090:"
                   "00000:"
                   "60006:"
                   "07970")

# make a small change to the image
my_image02 = Image("00000:"
                   "05050:"
                   "00000:"
                   "60006:"
                   "07970")

display.show(my_image01)
sleep(1000)
display.show(my_image02)