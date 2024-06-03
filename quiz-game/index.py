print("Welcome To My Labyrint")

playing = input("Mau Main? ")

if playing != "ya":
    quit()

questionList = ["Apa kepanjangan dari RI? ", "Apa kepanjangan dari TAPERA? ", "Apa kepanjangan IKN? "]
answerList = ["republik indonesia", "tabungan perumahan rakyat", "ibu kota negara"]

print("Anda ternyata main! ")

for i, v in enumerate(questionList):
    answer = input(v)
    if answer == answerList[i]:
        print("Anda benar")
    else:
        print("Anda salah")