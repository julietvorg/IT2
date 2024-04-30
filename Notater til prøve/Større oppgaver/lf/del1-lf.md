---
title:  'IT2 - Tentamen H23'
author:
- 12.12.23
---

# Del 1 - uten hjelpemidler

Navn: **FASIT**

## Oppgave 1

### 1.1


```python
tall1 = "22"
tall2 = "55"
tall = tall1 + tall2
print(tall)
```

Hva printes?

Svar: `2255`

### 1.2

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
print(hallo[1][1])
```

Hva printes?

Svar: `hallo`

### 1.3

```python
hallo = [{"b":[4,3,5], "a":[0]}, ["hei", "hallo"]]
print(hallo[1][1][1])
```

Hva printes?

Svar: `a`

### 1.4

```python
a = {"a": [1,2,-1], "b": [9,-9,1]}
print(max(a["b"]))
```

Hva printes?

Svar: `9`

### 1.5

```python
nøkkel = "hei"
if True:
    nøkkel = "ja"
else:
    nøkkel = "yo"

bok = {"ja": "nei", "hei": "Ha det!", "yo": "man"}
print(bok[nøkkel])
```

Hva printes?

Svar: `nei`


### 1.6

```python
def nei(a, b):
    print(b,a)

a = 2
b = 3
nei(b,a)
```

Hva printes?


Svar: `2 3`

### 1.7

```python
def ja(n):
    for i in range(n):
        print("hei " * i)
ja(3)
print("Tull!")
```

Hva printes?


Svar:
```

hei
hei hei
Tull!
```


### 1.8

```python
a = 100
b = 150
b = a
a = b
print(a, b)
```

Hva printes?


Svar: `100 100`


### 1.9

Skriv en kode som bytter plass på verdiene til `a` og `b`

```python
a = 20
b = 10
# Din kode her
c = a
a = b
b = c
# ---
print(a) # -> 10
print(b) # -> 20
```

Bonus:
```python
a = 20
b = 10
# Din kode her
a,b = b,a
# ---
print(a) # -> 10
print(b) # -> 20
```


### 2.1

Hva skrives ut her?

```python
class Buss():
    def __init__(self, maks):
        self.passasjerer = 0
        self.maks = maks

    def ta_på(self, antall):
        if self.passasjerer + antall <= self.maks:
            self.passasjerer += antall

    def sett_av(self, antall):
        self.passasjerer -= antall
        if self.passasjerer < 0:
            self.passasjerer = 0

thors_buss = Buss(5)

thors_buss.ta_på(6)
thors_buss.ta_på(3)
thors_buss.ta_på(3)
thors_buss.ta_på(3)

thors_buss.sett_av(1)

print(thors_buss.passasjerer)
```

Svar: `2`


### 2.2

Hva skrives ut her? (klassen `Buss` er lik som i oppgave 2.1)

```python
thors_buss = Buss(5)
ravis_buss = Buss(40)
ingrids_buss = Buss(30)

thors_buss.ta_på(10)
ravis_buss.ta_på(10)
ingrids_buss.ta_på(10)

thors_buss.sett_av(5)
ravis_buss.sett_av(5)
ingrids_buss.sett_av(5)

print(thors_buss.passasjerer)
print(ravis_buss.passasjerer)
print(ingrids_buss.passasjerer)

```

Svar:

```
0
5
5
```


### 2.3

Hva skrives ut her? (klassen `Buss` er lik som i oppgave 2.1)

```python
class Minibuss(Buss):
    def __init__(self):
        super().__init__(7)

class Megabuss(Buss):
    def __init__(self):
        super().__init__(90)

peders_buss = Minibuss()
fredriks_buss = Megabuss()
peders_buss.ta_på(10)
fredriks_buss.ta_på(10)

peders_buss.sett_av(5)
fredriks_buss.sett_av(5)

print(fredriks_buss.passasjerer)
print(peders_buss.passasjerer)

```

Svar:

```
5
0
```
