import random

num_top = input("Ketikkan Angka: ")
trying_guess = 0

if num_top.isdigit():
    num_top = int(num_top)
    if num_top <= 0:
        print("Tolong masukkan angka lebih dari 0 lain kali yaaa :)")
        quit()
else:
    print("Kami tidak mengerti apa yang anda masukkan. Tolong masukkan angka saja")
    quit()

random_number = random.randint(0, num_top)

while True:
    trying_guess += 1
    guess_num = input("Masukkan tebakan Anda ..")

    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("Masukkan angka saja bro")
        continue

    if guess_num == random_number:
        print("Anda benar! permainan berakhir")
        break
    elif guess_num > random_number:
        print("Tebakan Anda terlalu keatas")
    else:
            print("Tebakan Anda Terlalu Kebawah")


print("Anda berhasil menebak dengan", trying_guess, "Percobaan")






