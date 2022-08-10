from microbit import *

# display.show(Image.HAPPY)

# create first image, LED 0 off, 9 on full
# and any values inbetween
# name the image depending on the subject
# one word with _ between words if necessary
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

# create third image to loop animation
my_image03 = Image("00000:"
                   "00000:"
                   "00000:"
                   "60006:"
                   "07970")

# create a forever loop
while True:
    display.show(my_image01)
    # vary timing depending on the subject
    sleep(1000)
    display.show(my_image02)
    sleep(150)
    display.show(my_image03)
    sleep(300)