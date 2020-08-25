def emoji(message):
    words = message.split(" ")
    convert = {
        ":)" : "😊",
        ":(" : "😔",
        "<3" : "❤"
    }
    j = ""
    for word in words:
        j = j + convert.get(word, word) + " "
    return j


message=input("Enter your message : ")
print(emoji(message))
