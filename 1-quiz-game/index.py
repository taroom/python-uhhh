print("Welcome To My Labyrint")

playing = input("Mau Main? ")

if playing != "ya":
    quit()

questionList = ["Apa kepanjangan dari RI? ", "Apa kepanjangan dari TAPERA? ", "Apa kepanjangan IKN? ", "Apa kepanjangan dari SBY? "]
answerList = ["republik indonesia", "tabungan perumahan rakyat", "ibu kota negara", "surabaya"]

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
print("benar : "+ str((score/len(questionList)) * 100) +"%")