def deg_profanity(line):
    profane = {"beep": 0, "beep1": 0, "beep2":0, "beep3":0}
    deg = 0
    words = line.strip().split(" ")
    for word in words:
        try:
            profane[word] = profane[word]+1
            deg = deg + 1
        except KeyError:
            pass
    sane = len(words) - deg
    if(deg == 0):
        print(line.strip() + " -> Normal -> Degree: " + str(deg))
    elif(sane > deg):
        print(line.strip() + " -> Mild -> Degree: " + str(deg))
    elif(sane == deg):
        print(line.strip() + " -> High -> Degree: " + str(deg))
    else:
        print(line.strip() + " -> Severe -> Degree: " + str(deg))

def call():
    with open("tweets.txt", "r") as file:
        for f in file:
            deg_profanity(f)
            
call()