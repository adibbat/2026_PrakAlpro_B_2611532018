# Nama: Adib Ridho Putra
# NIM: 2611532018
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Adib Ridho Putra"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)