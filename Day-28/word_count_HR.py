# constraints:
# word length < 10^6
# word is lowercase char
n = int(input())
word_count={}
order_of_appearance=[]
for i in range(n):
    word = input()
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
        order_of_appearance.append(word)

print(len(order_of_appearance))
print(' '.join(str(word_count[word])for word in word_count))