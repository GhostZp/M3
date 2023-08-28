kalanpituus = float(input("Kerro kuhan pituus: "))
kuha = 38 - kalanpituus
if kalanpituus <= 37:
    print(f"Laske kuha takaisin järveen. Kuhan pitäisi olla viellä {kuha} senttimetriä pitkä.")


elif kalanpituus > 37:
    print("Voit pitää kalan.")