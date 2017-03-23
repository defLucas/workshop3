"""The function should not print it; the program should store and print the return value.
Wasn't sure if this is what you were requesting for the practical."""

def main():
  score = getScore()
  if score < 0 or score > 100:
      print("Invalid score")
  elif score > 89:
      print("Excellent")
  elif score > 49:
      print("Passable")
  else:
      print("Bad")


def getScore():
    score = float(input("Enter score: "))
    return score


main()