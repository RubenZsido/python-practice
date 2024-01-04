import math
#• hanyfelekeppen keszıthetunk beloluk egy k hosszu sorozatot;
def sorbarendezhetoseg():        
    k = int(input("Sor hossza(k): "))
    elemek = [1, 2, 3]

    if  len(elemek) < k:
        print(f"lehetetlen mert elemek szama: {len(elemek)}, k(sor hossza): {k}")
        return

    
    lehetseges_kombinaciok = math.factorial(k) / math.factorial(len(elemek) - k)
    print(f"Lehetseges kombinaciok: {int(lehetseges_kombinaciok)}")
sorbarendezhetoseg()
#• hanyfelekeppen valaszthatunk ki beloluk k darabot?

