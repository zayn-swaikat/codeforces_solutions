one = input()
two = input()
shuffled = input()
combined = one + two

if (len(combined) != len(shuffled)):
    print("NO")
else:
    if set(combined) != set(shuffled):
        print("NO")
    else:
        for letter in combined:
            if combined.count(letter) != shuffled.count(letter):
                result = "NO"
                break
            else:
                result = "YES"
        print(result)