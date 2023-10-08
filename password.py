# -*- coding: utf-8 -*-
"""Password.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1traYvQ0vyI_iipc8GzmaEzeZOP4gMxxg
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password(10))