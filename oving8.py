#oppgave a)

class Land:
    def __init__(self, navn, befolkning='Ikke satt', areal=None):
        self.navn = navn
        self.befolkning = befolkning
        self.areal = areal

    #oppgave b)
    def __str__(self):
        return f'Navn: {self.navn} (Befolkning: {self.befolkning}, Areal til landet: {self.areal})'
        
    #oppgave c)
    def befolkningstetthet(self):
        return self.befolkning / self.areal

#oppgave d)
def befolkning(land1=Land, land2=Land):
    if land1.befolkning > land2.befolkning:
        return land1
    else: 
        return land2

#oppgave e)
land = {}
with open('befolkning_tabell_csv.txt', 'r') as f:
    for linje in f:
        try:
            strippet = linje.strip()
            splittet = linje.split(';')
            land_navn = splittet[0]
            land_befolkning = int(splittet[1])

            land_objekt = Land(land_navn, land_befolkning)
            land[land_navn] = land_objekt
        except: 
            pass

#oppgave f
with open('areal_tabell_csv.txt', 'r') as f:
    for linje in f:
        try:
            strippet = linje.strip()
            splittet = strippet.split(';')

            if splittet[0] in land:
                land[splittet[0]].areal = float(splittet[1])
            else:
                print(f'Fannt ikke landet {splittet[0]}.')
        except:
            print(f'Finner ikke {splittet}')

#oppgave g og h
foreloping_hoyest = Land('minst', -1, 1)
for l in land:
    if land[l].areal:
        if type(land[l].befolkning) != str:
            print(f'{land[l]}, {land[l].befolkningstetthet()}')
            if land[l].befolkningstetthet() > foreloping_hoyest.befolkningstetthet():
                foreloping_hoyest = land[l]
print(foreloping_hoyest)
