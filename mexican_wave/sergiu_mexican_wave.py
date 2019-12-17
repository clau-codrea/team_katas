def get_wave_at(string, i):
    return string[:i] + string[i].upper() + string[i + 1:]


def wave(str):
    return [get_wave_at(str, i) for i in range(len(str)) if not str[i].isspace()]
