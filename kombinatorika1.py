# 3 típus
#• hanyfelekeppen rendezhetok sorba;
sz = int(input("Szamjegyek: ")) # _ _ _
e = int(input("Elemek szama: ")) # e * e * e

print(f"Szamjegyek: {sz}")
print("_ " * sz)
print(f"Elemek szama: {e}")
print((str(e) + " ") * sz)
print((str(e) + " * ") * (sz - 1) + str(e))
lehetseges_kombinaciok = e ** sz
print(f"Lehetseges kombinaciok: {lehetseges_kombinaciok}")


