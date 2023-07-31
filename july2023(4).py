##most frequent letters

input_string = input("Please enter a string: ")

def most_frequent(input_string):
  input_string = input_string.lower()
  letter_freq = {}
  for letter in input_string:
    if letter.isalpha():
      letter_freq[letter] = letter_freq.get(letter, 0) + 1
  sorted_freq = dict(sorted(letter_freq.items(), key=lambda item: item[1], reverse=True))

  for letter, freq in sorted_freq.items():
    print(f"{letter} = {freq:02d}")

most_frequent(input_string)
