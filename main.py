from pathlib import Path
import os
import random
from PIL import Image

# mood_input = input("What сolor do you want to wear today? ")
# answer = ["I don't know", "don't know", "idk", "dont know"]
# if mood_input in answer:
#     print("I will help you")
# color_input = input("Are you ready for random color? ").lower()
# if color_input == "yes":
#     print("random")
#
#


def get_random_image(folder_path):
    folder_path = Path(folder_path)
    for item in folder_path.iterdir():
        Image.open(item).show()
        break


get_random_image("C:\Фото\Ногти\WORK")
