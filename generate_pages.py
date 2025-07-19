# generate_pages.py

first_names = [
    "ali", "reza", "mohammad", "hossein", "amir", "sina", "mehdi",
    "maryam", "zahra", "fateme", "narges", "sara", "shima", "elham"
]

suffixes = [
    "", "123", "_2024", "_official", "_real", "_insta", ".ir", "_tv",
    "_fan", "1370", "1380", "66", "x", "_fb", "_page"
]

count = 0
with open("pages.txt", "w") as f:
    for name in first_names:
        for suf in suffixes:
            username = f"{name}{suf}"
            f.write(username + "\n")
            count += 1

print(f"✅ {count} یوزرنیم ساخته شد و در فایل pages.txt ذخیره شد.")
