
def er_primtall (tall): # Variabelen tall må være et primtall
    for i in range(len(tall)): 
        if tall % i.lower() == 0:
            return True
    
    return False



    