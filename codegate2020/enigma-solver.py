#!/usr/bin/env python3
#code from the OSIRIS Lab
#download the file and unzip in the linux system:
'''
DON'T LET YOUR RIGHT HAND KNOW WHAT YOUR LEFT HAND DID
5+,'( "2( )+-3 r-/:( :*,5 ',+1 1:*( )+3 "26( :*,5 5-d


ONCE A HACKER IS AN ETERNAL HACKER
+,92 * :*9'23 -4 *, 2(23,*" :*9'23


A HACKER WITHOUT PHILOSOPHY IS JUST AN EVIL COMPUTER GENIUS
* :*9'23 1-(:+-( @:-"+4+@:) -4 ;_4( *, 2?-" 9+.@_(23 /2,-_4

flag is :
9+52/*(22020{:*9'234 *32 ,+( !+3, +,") -( -4 .*52}
'''
#each symbol is corresponding to a character 


file = []
enc_flag = None

# Parse file
with open("enigma", 'r') as f:
  lines = []
  for line in f.readlines():
    if line == '\n':
      continue
    lines.append(line.strip())
  #read the file in to an array
  print("lines: "+str(lines))
  print()

  for ln in range(0, len(lines)-2, 2):
    file.append((lines[ln], lines[ln+1]))
  enc_flag = lines[-1]
  #the flag
  print("enc_flag: " + str(enc_flag))
  print()

key_char_map = {'!': 'B'}
for text_line, enc_line in file:
  for char, key in zip(text_line, enc_line):
    key_char_map[key] = char
  print("zip(text_line, enc_line): " + str(set(zip(text_line,enc_line))))
  print()
#the map of corresponding character
print("key_char_map:" + str(key_char_map))
print()

flag = ""
for enc in enc_flag:
  try:
    flag += key_char_map[enc]
  except:
    # print(f"Key not found: {enc}")
    flag += enc

print(flag)
