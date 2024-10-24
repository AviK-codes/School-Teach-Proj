# first project exercise for the class - cipher decipher
import string, random

used_char=set()
cipher_dict = {}
rnd_char=""

random.seed("akeyforciphering")

for letter in string.ascii_letters:
          while True:
              rnd_char = chr(random.randint(32, 126))
              if rnd_char not in used_char:
                 cipher_dict[letter]=rnd_char
                 used_char.add(rnd_char)
                 break

rnd_space=chr(random.randint(32, 126))
cipher_dict[" "]=rnd_space

print(cipher_dict)

decipher_dict = {cipher_dict[le]:le for le in cipher_dict}

print(decipher_dict)

txt = "A message from Mars is arriving"

cp=""
for l in txt:
   cp+=(cipher_dict[l])
print(cp)

dcp=""
for l in cp:
   dcp+=(decipher_dict[l])
print(dcp)