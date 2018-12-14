#Author: Diego Garcia Cordeiro Souza

import random
def generate():
    """
    This is a very basic function to generate random passwords
    combining upper and lowercase letters, numbers and special
    characters.
    """
    S1 = "abcdefghijklmnopqrstuvxyz"
    S2 = "ABDCEFGHIJKLMNOPQRSTUVWXYV"
    S3 = "@#!$%&*-_[]{}?<>:+=/,"
    S4 = "0123456789"
    pass_ = []
    pass_len = input("Enter password's lenght: ")

    for i in range(int(pass_len)):
    S = random.randint(1, 4)
    if S == 1:
      char_i = random.randint(0, (len(S1)-1))
      char_ = S1[char_i]
      pass_.append(str(char_))
    elif S == 2:
      char_i = random.randint(0, (len(S2)-1))
      char_ = S2[char_i]
      pass_.append(str(char_))
    elif S == 3:
      char_i = random.randint(0, (len(S3)-1))
      char_ = S3[char_i]
      pass_.append(str(char_))
    elif S == 4:
      char_i = random.randint(0, (len(S4)-1))
      char_ = S4[char_i]
      pass_.append(str(char_))
    else:
      return "hue i broke"
    pass_str = "".join(pass_)
    return pass_str
