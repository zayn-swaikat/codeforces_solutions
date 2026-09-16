line = input()
if len(line) < 7:
    print("NO")

else:
    yes = False
    for i in range(len(line) - 6):
        if line[i]==line[i+1]==line[i+2]==line[i+3]==line[i+4]==line[i+5]==line[i+6]:
            yes = True
            break
    if yes:
        print("YES")
    else:
        print("NO")