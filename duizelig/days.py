day = ["ma", "di", "wo", "do", "vr", "za", "zo"]
choice = input("vul een dag in ")
i = 0

while i <= day.index(choice):
    print(day[i])
    i += 1