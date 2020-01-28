def toNumber(digitlist):
  return sum(list(map(
            lambda t: (10 ** t[0]) * t[1],
            zip(range(len(digitlist)-1, -1, -1), digitlist)
            )))

def toDigitList(number):
  return list(map(lambda x: number // 10 ** x % 10, range(9, -1, -1)))

def diff(list1, list2):
  return sorted(list(set(list1) - set(list2)))

def get_sequence(offset, size):
  snappedOffset = 1023456789 if offset < 1023456789 else offset
  return [] if offset > 9876543210 else forCascade(snappedOffset, size)

def forCascade(offset, size):
  outputList = []
  digList = toDigitList(offset)

  d0 = 1 if digList[0] == 0 else digList[0]
  for a0 in range(d0,10):
    d1 = digList[1] if a0 == d0 else 0
    for a1 in diff(range(d1,10), [a0]):
      d2 = digList[2] if a1 == d1 else 0
      for a2 in diff(range(d2,10), [a0,a1]):
        d3 = digList[3] if a2 == d2 else 0
        for a3 in diff(range(d3,10), [a0,a1,a2]):
          d4 = digList[4] if a3 == d3 else 0
          for a4 in diff(range(d4,10), [a0,a1,a2,a3]):
            d5 = digList[5] if a4 == d4 else 0
            for a5 in diff(range(d5,10), [a0,a1,a2,a3,a4]):
              d6 = digList[6] if a5 == d5 else 0
              for a6 in diff(range(d6,10), [a0,a1,a2,a3,a4,a5]):
                d7 = digList[7] if a6 == d6 else 0
                for a7 in diff(range(d7,10), [a0,a1,a2,a3,a4,a5,a6]):
                  d8 = digList[8] if a7 == d7 else 0
                  for a8 in diff(range(d8,10), [a0,a1,a2,a3,a4,a5,a6,a7]):
                    d9 = digList[9] if a8 == d8 else 0
                    for a9 in diff(range(d9,10), [a0,a1,a2,a3,a4,a5,a6,a7,a8]):
                      number = toNumber([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9])
                      outputList.append(number)
                      if len(outputList) == size:
                        return outputList
