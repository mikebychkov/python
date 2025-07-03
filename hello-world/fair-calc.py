part = {}

while True:
    name = input("Name of the partisipant: ")
    if name == "calc":
        break
    money = input("Money amount: ")
    try:
        part[name] = int(money)
    except:
        print("Invalid amount, try again")

totalAmount = 0
for name in part:
    totalAmount += part[name]

print(f"Total amount: {totalAmount}")

equalAmount = totalAmount / len(part)

givers = {}
takers = {}

for name, amount in part.items():
    if amount > equalAmount:
        takers[name] = abs(equalAmount - amount)
    else:
        givers[name] = abs(equalAmount - amount)

print(f"Takers: {takers}")
print(f"Givers: {givers}")

debt = 0
for g in givers:
    debt += givers[g]

while debt > 0:
    for g in givers:
        for t in takers:
            sum = min(takers[t], givers[g])
            if sum == 0:
                continue
            print(f"{g} gives {t}: {sum}")
            takers[t] -= sum
            givers[g] -= sum  
            debt -= sum
