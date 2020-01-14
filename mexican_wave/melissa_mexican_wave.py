def wave(string):
  wave = []
  
  for i in range(len(string)):
        if string[i].isspace() == False:
            wave.append(string[:i] + string[i].upper() + string[i+1:])
  
  return wave