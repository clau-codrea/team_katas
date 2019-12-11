def wave(string):
    wave = []
    for index, letter in enumerate(string):
        if not letter.isspace():
          wave.append(string[:index] + letter.upper() + string[index + 1:])

    return wave
