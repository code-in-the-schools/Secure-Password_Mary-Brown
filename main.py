print("Your password needs one upper case and lower case letter, one  number or special character, and must be 8-16 characters long")
password = str(input)

if password < 8 and > 16:
  print("Password saved!")