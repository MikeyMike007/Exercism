# convert converts the sound of 'number' of raindrops. The function return the
# sound in a string format
def convert(number):
    sound = ''
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        sound = str(number)
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"

    return sound
