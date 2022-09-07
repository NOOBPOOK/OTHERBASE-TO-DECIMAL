# Convert other number systems into decimal

nr = input("Please Enter The Number to be Converted!:\t")
n = nr.split(".")
m = int(input("Please Enter Your Base of Number:\t"))
tot1 = 0
tot2 = 0
x = 0

if m != 16:
    sentence = ""
    print("\n***STEPS TO BE FOLLOWED:***\n")
    print(f"{n[0]} = ", end="")
    for i in (n[0][::-1]):
        print(f"({i}X{m}**{x})", end=" + ")
        sentence += f"{i}X{m ** x} + "
        tot1 += int(i) * (m ** x)
        x += 1
    print(f"\n{n[0]} =", sentence)
    print(f"For Integer Part:\n{n[0]} = {tot1}")

    if len(n) == 2:
        x = 1
        print("\n******For Decimal Part******\n")
        print(f"{n[1]} = ", end="")
        sen = ""
        for i in (n[1]):
            print(f"({i}X{m}**{-x})", end=" + ")
            sen += f"{i}X{1 / (m ** x)} + "
            tot2 += int(i) * (m ** (-x))
            x += 1
        print(f"\n{n[1]} =", sen)
        print(f"For Decimal Part:\n0.{n[1]} = {tot2}")

    print("\nThe Final Number in Decimal Format:\t", tot1 + tot2)
    for i in range(70):
        print("*", end="")

else:
    con = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    quo = []
    rem = []
    for i in n[0]:
        if i in con.keys():
            quo.append(str(con[i]))
        else:
            quo.append(i)
    if len(n) == 2:
        for i in n[1]:
            if i in con.keys():
                rem.append(str(con[i]))
            else:
                rem.append(i)

    sentence = ""
    print("\n***STEPS TO BE FOLLOWED:***\n")
    print(f"{n[0]} = ", end="")
    for i in (quo[::-1]):
        print(f"({i}X{m}**{x})", end=" + ")
        sentence += f"{i}X{m ** x} + "
        tot1 += int(i) * (m ** x)
        x += 1
    print(f"\n{n[0]} =", sentence)
    print(f"For Integer Part:\n{n[0]} = {tot1}")

    if len(n) == 2:
        x = 1
        print("\n******For Decimal Part******\n")
        print(f"{n[1]} = ", end="")
        sen = ""
        for i in rem:
            print(f"({i}X{m}**{-x})", end=" + ")
            sen += f"{i}X{1 / (m ** x)} + "
            tot2 += int(i) * (m ** (-x))
            x += 1
        print(f"\n{n[1]} =", sen)
        print(f"For Decimal Part:\n0.{n[1]} = {tot2}")

    print("\nThe Final Number in Decimal Format:\t", tot1 + tot2)
    for i in range(70):
        print("*", end="")
