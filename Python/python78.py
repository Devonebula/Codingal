def match_words(words):
    count=0
    for i in words:
        if i[0]==i[-1]:
            count+=1

    return count

list_words=["abc", "xyz", "aba", "1221"]
count=match_words(list_words)

print(count)