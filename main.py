dict_meme = {"КРИНЖ": "Что-то очень странное или стыдное",
             "ЛОЛ": "Что-то очень смешное",
             "РОФЛ": "шутка",
             "ЩИЩ": "одобрение или восторг",
             "КРИПОВЫЙ": "страшный, пугающий",
             "АГРИТЬСЯ": "злиться"}

for i in range(5):
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in dict_meme.keys():
        print('Это слово означает:', dict_meme[word])
    else:
        print("Такого слова нет в нашем словаре, спросите у ребенка, что это за слово")
        