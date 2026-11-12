# Nama: Adib Ridho Putra
# NIM: 2611532018
# Question 6

full_name = "Adib Ridho Putra"
nim = "2611532018"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]
print(username)