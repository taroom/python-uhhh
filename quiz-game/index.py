print("Welcome To My Labyrint")

playing = input("Mau Main? ")

if playing != "ya":
    quit()

print("Anda ternyata main! ")

answer = input("Apa singkatan dari VS? ")
if answer == "versus":
    print("Anda benar")
else:
    print("Anda salah")

# Ulangi Lagi
answer = input("Apa singkatan dari tapera? ")
if answer == "tabungan perumahan rakyat":
    print("Anda benar")
else:
    print("Anda salah")