import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  for x in range(2):
      rnd = random.randint(0, last)
      print(quotes[rnd], end="")

def add():
  # adding of a new quote to the quote.txt

  quote = input("Enter a new quote: " )
  f = open("quotes.txt", "a")
  f.write(quote)
  f.close()
  print("The quote: \n" + quote+ "\nis added to the File quote.txt.")

if __name__== "__main__":
  primary()
  add()
