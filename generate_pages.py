# generate_pages.py

import random

first_names = ["ali","reza","mohammad","amir","sina","mehdi","maryam","zahra","fateme","narges","sara","shima","elham","parsa","armin","navid","hamed","vahid","pouya","zahra"]
suffixes = ["","123","_2024","_official",".ir","_tv","_fan","_page","_club","_iran","_music","_team","_group"]

with open("pages.txt", "w") as f:
    count = 0
    while count < 100000:
        name = random.choice(first_names)
        suf = random.choice(suffixes)
        user = f"{name}{suf}{random.randint(1,99999)}"
        f.write(user + "\n")
        count += 1

print("✅ Generated 100,000 usernames in pages.txt")
