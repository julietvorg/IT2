# Algoritme 1: Høyeste tall i en liste

def høyeste(liste: list[int]):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest

min_liste = [2, 6, -10, 100, 95]
print(høyeste(min_liste))


# Algoritme 4

def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(n):
        høyest = høyeste(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n
print(n_høyeste([1,2,3,-5,5,-4,3]), 3)

def n_høyeste_alt(liste: list[int], n: int):
    sortert = sorted(liste, reverse=True)
    return sorted[:n]
print(n_høyeste_alt([1,2,3,-5,5,-4,3]), 3)
