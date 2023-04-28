'''cat parade'''
def main():
    '''cat parade'''
    count_ = []
    cat = []
    while True:
        string = input().split(", ")
        if string == ["IT\'S A DOG"]:
            count_.pop()
            continue
        if string == ['END']:
            break
        count_ += string
    for i in range(len(count_)):
        if count_[i] not in cat:
            cat.append(count_[i])
    cat.sort()
    for i in range(len(cat)):
        print("%s %d %d"%(cat[i], (count_.index(cat[i])+1),\
            count_.count(cat[i])))
main()
