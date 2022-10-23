import math
#oppgave a og b
def Strom(retning1, retning2):
    return math.sqrt(retning1**2 + retning2**2)

def Areal(r):
    return math.pi*(r**2)

#oppgave f (øving 4)
def Turbin(strom, tetthet=1000, turbin_effekt=0.3, diameter=1):
    areal = Areal(diameter/2)
    return 0.5*turbin_effekt*tetthet*areal*(strom**3)


#oppgave g (øving 4)
strom_bruker = Strom(retning1 = int(input('Retning 1: ')), retning2 = int(input('Retning 2: ')))
strom_verdi = Turbin(strom_bruker)
print(f'Energiproduksjonen til turbinen er: {strom_verdi}')

#oppgave c
with open('tidevannsdata_csv.txt', 'r') as f:
    tidspunkt = []
    strom_r1 = []
    strom_r2 = []

    for linje in f:
        try:
            strippet = linje.strip()
            splittet = strippet.split(';')
            tidspunkt.append(float(splittet[0]))
            strom_r1.append(float(splittet[1]))
            strom_r2.append(float(splittet[2]))
        except ValueError:
            pass
    print(f'Tidspunkt: {tidspunkt}\n\nStrøm retning 1:{strom_r1}\n\nStrøm retning 2:{strom_r2}')
