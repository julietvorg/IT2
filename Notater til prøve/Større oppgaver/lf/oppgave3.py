# 3.1

def per_stream(land):
    land = land.lower()
    if land == "norge":
        return 0.55
    if land == "sverige":
        return 0.44
    if land == "finland":
        return 0.44
    if land == "danmark":
        return 0.52
    if land == "island":
        return 0.62
    return 0.24

print(per_stream("Norge"))  # -> 0.55
print(per_stream("Island")) # -> 0.62
print(per_stream("USA"))    # -> 0.24

# 3.2
def andel_til_artist(antall_streams):
    if antall_streams > 29_999_999:
        return 0.7
    if antall_streams > 399_999:
        return 0.4
    return 0
    

print(andel_til_artist(50_000))     # -> 0
print(andel_til_artist(5_000_000))  # -> 0.4
print(andel_til_artist(50_000_000)) # -> 0.7

# 3.3
def penger_tjent(antall_streams, land):
    return antall_streams * per_stream(land) * andel_til_artist(antall_streams)

print(penger_tjent(5_000_000, "Norge"))    # -> 1100000
print(penger_tjent(100_000_000, "Island")) # -> 43_400_000

# 3.4
def populære(artistliste):
    ny_liste = []
    for artist in artistliste:
        if artist[1] >= 100_000_000:
            ny_liste.append(artist)
    return ny_liste

artister = [
    ["Taylor Swift",  109_940_000],
    ["The Weeknd",    105_410_000],
    ["Justin Bieber",  83_820_000],
    ["Drake",          81_980_000],
    ["Ariana Grande",  81_800_000]
]
print(populære(artister)) # -> [["Taylor Swift", 109_940_000], ["The Weeknd", 105_410_000]]


# 3.5
def royalties(artistliste):
    ny_liste = []
    for artist in artistliste:
        penger = penger_tjent(artist[2], artist[1])
        ny_liste.append([artist[0], penger])
    return ny_liste

artister = [
    ["Sígur Ros",        "Island", 1_047_010],
    ["Emma Steinbakken", "Norge",  3_459_239]
]
print(royalties(artister)) # -> [['Sígur Ros', 259658], ['Emma Steinbakken', 761032]]