vuosiluku = int(input("Kerro vuosiluku: "))

if vuosiluku % 4 == 0 or (vuosiluku % 100 == 0 and vuosiluku % 400 == 0):
    print("Vuosi on karkausvuosi.")
