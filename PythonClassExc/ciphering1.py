# first project exercise for the class - cipher decipher with
# 1. function
# 2. add support for hebrew

import string, random, time

cipher_dict = {}
decipher_dict = {}
msg = ""
hebrew_letters = ''.join(chr(i) for i in range(0x05D0,0x05EA+1))

def prepare_code_book(key):
  global decipher_dict
  random.seed(key)
  used_char = set()
  rnd_char = ""

  # do it for english letters
  for letter in string.ascii_letters:
      while True:
         rnd_char = chr(random.randint(32, 126))
         if rnd_char not in used_char:
           cipher_dict[letter]=rnd_char
           used_char.add(rnd_char)
           break

  # do it for hebrew letters
  used_char.clear()
  for letter in hebrew_letters:
      while True:
         rnd_char = chr(random.randint(129, 229))
         if rnd_char not in used_char:
           cipher_dict[letter]=rnd_char
           used_char.add(rnd_char)
           break

  # do it for extra characters
  used_char.clear()
  for letter in ",. /\\-":
      while True:
         rnd_char = chr(random.randint(230, 250))
         if rnd_char not in used_char:
           cipher_dict[letter]=rnd_char
           used_char.add(rnd_char)
           break

  decipher_dict = {cipher_dict[le]:le for le in cipher_dict}

def enter_message(prompt):
    global msg
    msg=input(prompt)

#aa=[chr(random.randint(32, 126)) for i in range(1,20)]
#print(''.join(aa)+time.strftime('%Y%m%d-%H%M%S'))

prepare_code_book("fgrdssdfd")

print(cipher_dict)
print(decipher_dict)

enter_message("Enter your message to be encrypt: ")

cp=""
for l in msg:
   cp+=(cipher_dict[l])
print(cp)

dcp=""
for l in cp:
   dcp+=(decipher_dict[l])
print(dcp)