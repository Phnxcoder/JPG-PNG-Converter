import sys
import os
from PIL import Image

first_path = sys.argv[1]
second_path = sys.argv[2]

if not os.path.exists(second_path):
    os.makedirs(second_path)

for file_name in os.listdir(first_path):
    img = Image.open(f'{first_path}{file_name}')
    clean_name = os.path.splitext(file_name)[0]
    img.save(f'{second_path}/{clean_name}.png','png')

print(first_path,second_path)