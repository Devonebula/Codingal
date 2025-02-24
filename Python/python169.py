def duplicates(item):
    seen=set()
    for i in item:
        if i in seen:
            return True
        seen.add(i)
    return False

def like_hate(a):
    if duplicates(a):
        print('I lake', a)
    else:
        print('I hate', a)

like_hate('Keshav')