# assert 3 > 2 # sjekk/forsikre at 3 er større enn 2
# assert 2 > 3 # Gir en feilmelding. Koden stopper. 


# Test-drevet utvikling med assert
# Eksempel en funksjon som tester om tall er partall
def partall(tall: int):
    #if tall == 2:
        #return True
    #if tall == 1:
        #return False (samme som under, enklere skrevet)
    if tall % 2 == 0:
        return True
    else: 
        return False
    

assert partall(2) == True, "2 er et partall"
assert partall(1) == False, "1 er IKKE et partall"
assert partall(-2) == True, "-2 er et partall"
assert partall(-1) == False, "-1 er IKKE et partall"

