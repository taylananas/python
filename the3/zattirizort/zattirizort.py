def matrix_exists(target, pattern):
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
        return (i, j, 180)

      # Rotate the pattern 90 degrees and check again
      pattern = rotate_90(pattern)
      if check_pattern(i, j, target, pattern):
        return (i, j, 90)

      # Rotate the pattern 90 degrees and check again
      pattern = rotate_90(pattern)
      if check_pattern(i, j, target, pattern):
        return (i, j, 0)

  # Return None if the pattern was not found
  return None

# Example usage
target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
pattern = [[5, 6], [9, 10]]
print(matrix_exists(target, pattern))  # Output: (1, 0, 0)



# Test the function
matrix = ["tuz<abcd", ">#sAY#at", "uzyXAAr.", "r,lAXxio", "z#a!yabc", "yazy?zya"]
sub_matrix = ["AXA", "XAY"]
print(matrix_exists(matrix, sub_matrix))  # True


