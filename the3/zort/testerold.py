Pt = (["AXA", "XAY"],
    ["AXA", "XAZ"],
    ["ayz", "cba"],
    ["11111111", "11111111"],
    ["XAX", "XXA"],
    ["XAA", "AXx"],
    ["zya", "cba"],
    ["zya", "abc"],
    ["ayz", "cba"],
    ["abcd", "zya'"],
    ["ariby", "#Axaz"],
    ["123", "111"],
    ["111", "456"],
    ["111", "654"],
    ["151", "161"],
    ["1111", "4321"],
    ["kjih098","gefdcba"])

It = (["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr."],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["AXAXAXAX", "AXAAAXXA", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["111111","123456","131111"],
    ["1234567","abcdfeg","890hijk"])

Rt= ((1, 3, 270),
    False,
    (4,5,180),
    False,
    (0, 5, 0),
    (2, 3, 0),
    False,
    False,
    (4,5,180),
    False,
    (1,5,90),
    (0,0,90),
    (0,3,0),
    (1,3,180),
    (0,4,270),
    False,
    (1,0,180))



def pattern_search(pattern, target):
  # Rotate the pattern matrix 90 degrees clockwise
  def rotate_90(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]

  # Check if the pattern is present at the current location in the target matrix
  def check_pattern(x, y, target, pattern):
    for i in range(len(pattern)):
      for j in range(len(pattern[0])):
        if target[x+i][y+j] != pattern[i][j]:
          return False
    return True

  # Iterate through all possible locations in the target matrix
  for i in range(len(target) - len(pattern) + 1):
    for j in range(len(target[0]) - len(pattern[0]) + 1):
      # Check if the pattern is present at the current location
      if check_pattern(i, j, target, pattern):
        return (i, j, 270)

      # Rotate the pattern 90 degrees and check again
      pattern = rotate_90(pattern)
      if check_pattern(i, j, target, pattern):
        return (i, j, 0)

      # Rotate the pattern 90 degrees and check again
      pattern = rotate_90(pattern)
      if check_pattern(i, j, target, pattern):
        return (i, j, 90)

      # Rotate the pattern 90 degrees and check again
      pattern = rotate_90(pattern)
      if check_pattern(i, j, target, pattern):
        return (i, j, 180)

  # Return None if the pattern was not found
  return False



for x in range(len(Pt)):
    if pattern_search(Pt[x], It[x])==Rt[x]:
        print(x+1,"doğru")
    else:
        print(x+1,"yanlış, senin cevabın:", pattern_search(Pt[x], It[x])," doğru cevap:",Rt[x] )
