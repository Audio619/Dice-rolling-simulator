# -*- coding: utf-8 -*-
"""Dice rolling simulator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L8__FpLcBiq5UjZ5GnsV4ibawV3iStn_
"""

import random


def roll_dice():
  return random.randit(1,6)

def main():
  while true:
    input ("press enter to roll dice...")
    result= roll_dice ()
    print(f"you rolled a {result}!")

    roll_again= input("Do you want to roll agin?(y/n):").lower()
    if roll_again  !="y"
        break

        if__name__=="__main__"
            main()