sukupuoli = str(input("Kerro biologinen sukupuoli: "))

if sukupuoli == "Nainen":
    hemoglobiini = float(input("Kerro hemogloobiiniarvo: "))
    if hemoglobiini >= 117 and hemoglobiini <=175:
        print("Hemoglobiini on normaali.")
    elif hemoglobiini <= 116:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini >=176:
        print("Hemoglobiinin on korkea.")

if sukupuoli == "Mies":
    hemoglobiini = float(input("Kerro hemogloobiiniarvo: "))
    if hemoglobiini >= 134 and hemoglobiini <=195:
        print("Hemoglobiini on normaali.")
    elif hemoglobiini <= 133:
        print("Hemoglobiini on alhainen.")
    elif hemoglobiini >=196:
        print("Hemoglobiinin on korkea.")