# Pseudokode

- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske uttrykk fungerer sammen for å løse et bestemt problem.


## Eksempel: Penger tjent på Spotify
 > En algoritme som regner ut hvor mye penger vi tjener på Spotify
 

### Pseudokode i *naturlig språk*

```pseudo
Hent inn antall streams
Hvis antall streams er større enn 30 000 000:
  Returner antall streams gange 70% (0.7)
Ellers hvis antall streams er større enn 1 400 000:
  Returner antall streams gange 40% (0.4)
Ellers:
  Returner 0
```


### Pseudo-kode som følger *UDIRs standard*

```pseudo
SET antall_streams TO READ "Hvor mange streams?"
IF antall_streams GREATER THAN 30 000 000
   THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streams GREATER THAN 1 400 000
   THEN DISPLAY antall_streams * 0.4
ELSE DISPLAY =
```


### Phyton kode

```python
antall_streams = int(input("Hvor mange streams?"))
if antall_streams > 30_000_000:
    print (antall_streams * 0.7)
elif antall_streams > 1_400_000:
    print (antall_streams * 0.4)
else: 
    print (0)
```
