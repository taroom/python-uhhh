print("Welcome To My Labyrint")

playing = input("Mau Main? ")

if playing != "ya":
    quit()

questionList = ["Apa kepanjangan dari RI? ", "Apa kepanjangan dari TAPERA? ", "Apa kepanjangan IKN? "]
answerList = ["republik indonesia", "tabungan perumahan rakyat", "ibu kota negara"]

print("Anda ternyata main! ")

score = 0

for i, v in enumerate(questionList):
    answer = input(v)
    if answer.lower() == answerList[i]:
        print("Anda benar")
        score += 1
    else:
        print("Anda salah")

print("score Anda : "+ str(score) +" Jawaban Benar")