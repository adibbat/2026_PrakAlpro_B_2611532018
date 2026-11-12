# Nama: Adib Ridho Putra
# NIM: 2611532018
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * len(phone[4:-3]) + phone[-3:]
print(masked)
