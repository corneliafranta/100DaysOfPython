import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

program_in_use = True

def ceasar(text, shift, mode):
  new_text = []
  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      if mode == "encode":
        new_text.append(alphabet[index + shift])
      elif mode == "decode":
        new_text.append(alphabet[index - shift])
    else:
      new_text.append(letter)
    
  print(f"The {direction}d text is '{''.join(new_text)}'.")



while program_in_use:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceasar(text, shift, direction)
  answer = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
  if answer.lower() == "no":
    program_in_use = False


   