'''FUNCTION bytt_plass(liste, i, j)
  SET midlertidig TO liste[i]
  SET liste[i] TO liste[j]
  set liste[j] TO midlertidig
ENDFUNCTION

SET min_liste TO [8, 5, 2, 6, 12]
SET n TO lengden av min_liste
SET bytta TO TRUE
WHILE bytta
  SET bytta TO FALSE
  SET i TO 0
  FOR hver i LESSER THAN n - 1
    IF min_liste[i] GREATER THAN min_liste[i+1]
      CALL bytt_plass(min_liste, i, i + 1)
      SET bytta TO TRUE
    ENDIF
  ENDFOR
ENDWHILE
'''

def bytt_plass(liste, i, j):
    midlertidig = liste[i]
    liste[i] = liste[j]
    liste[j] = midlertidig

min_liste = [8, 5, 2, 6, 12]
n = len(min_liste)
bytta = True

while bytta:
    bytta = False
    i = 0
    for i in range(n - 1):
        if min_liste[i] > min_liste[i + 1]:
            bytt_plass(min_liste, i, i + 1)
            bytta = True

print(min_liste)