red = int(input("Red: "))
green = int(input("Green: "))
blue = int(input("Blue: "))
if not(red >= 0 and red <= 255):
    print("Red number is not correct")
if not(green >= 0 and green <= 255):
    print("Green number is not correct")
if not(blue >= 0 and blue <= 255):
    print("Blue number is not correct")
if(red >= 0 and red <= 255 and green >= 0 and green <= 255 and blue >= 0 and blue <= 255):
    print("No problems found!")
