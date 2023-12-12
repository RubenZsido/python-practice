csoki = int(input("Hany csokit vasarol? "))

gumi = int(input("Hany gumicukrot vasarol? "))

keksz = int(input("Hany kekszet vasarol? "))

suti = int(input("Hany doboz sutemenyt vasarol? "))

borravalo = int(input("Mennyi borravalot ad? "))

koltes = csoki * 600 + gumi * 400 + keksz * 550 + suti * 1200 + borravalo

megmaradt = 10000-koltes

if megmaradt >= 0:
    print(f"Megmarad: {megmaradt} Ft ")
else:
    print(f"Hitelre vasarolt: {megmaradt * -1} Ft ertekben")




kamion = int(input())
auto = int(input())
egyeb = 250 - kamion - auto
print(f"{kamion} kamion/{auto} szemelyauto/{egyeb} egyeb jarmu")





szam = input()
if not len(szam) == 11:
    print("A megadott azonosito nem 11 szamjegybol all.")
else:
    eleventh_digit = int(szam[10])
    sum = 0
    for i, curr_digit in enumerate(szam[:-1]):
        sum += int(curr_digit) * (i + 1)
    if eleventh_digit == sum % 11:
        print("A szemelyi azonosito valodi.")
    else:
        print("A szemelyi azonosito nem valodi.")



szo = input()
szo = szo.replace("a", "4")
szo = szo.replace("e", "3")
szo = szo.replace("o", "0")
print(szo)


pi = 3.14159
r = int(input())
print(2 * r * pi)
print(r **2 * pi)



def van_e_a():
    szo = input()
    if not "a" in szo:
        print("Sajnos az 'a' karakter nem szerepelt a szovegben.")
        return
    
    elso = ""
    masodik = ""
    hossz = len(szo)
    if hossz % 2 == 0:
        elso = szo[:int(hossz / 2)]
        masodik = szo[int(hossz / 2):]
    else:
        elso = szo[:int(hossz / 2)+1]
        masodik = szo[int(hossz / 2+1):]
    if "a" in elso:
        print("Az 'a' karakter szerepel, es eloszor az elso feleben szerepelt.")
    else:
        print("Az 'a' karakter szerepel, de a masodik feleben szerepelt.")
van_e_a()
    



def is_valid_license_plate(lp):
    
    if not len(lp) == 7:
        print("Helytelen rendszam hossz.")
        return
    if not lp[3] == "-":
        print("A negyedik karakternek kotojelnek kell lennie.")
        return
    if not is_number(lp[4:]):
        print("Az utolso harom karakternek szamjegyeknek kell lenniuk.")
        return
    print("A megadott rendszam helyes formatumu.")
    

def is_number(num):
    try:
        a = int(num)
    except:
        return False
    return True
lp = input()
is_valid_license_plate(lp)





a = input()
b = input()
def melyik_hosszabb(a, b):
    if len(a) == len(b):
        print("A ket szo egyforma hosszu.")
        return
    if len(a) < len(b):
        c = a
        a = b
        b = c
    print(f"A ket szo kozul a {a} a hosszabb, {len(a) - len(b)} karakterrel.")
melyik_hosszabb(a,b)




jegyek = []
for i in range(5):
    a = input()
    jegyek.append(int(a))
    
print(sum(jegyek) / len(jegyek))




a = int(input())
b = int(input())
print(float((a+b)*2))
print(float(a*b))



def anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if not len(s1) == len(s2):
        return False
    m1 = {}
    m2 = {}
    for i in s1:
        if i not in m1:
            m1[i] = 1
        else:
            m1[i]+=1
        
    for i in s2:
        if i not in m2:
            m2[i] = 1
        else:
            m2[i]+=1
    return m1 == m2



def shopping(prices):
    min_index = -1
    min_price = 999999
    for index, store in enumerate(prices):
        if "tej" in store and "tojás" in store and "kenyér" in store:
            osszertek = store["tej"] + store["tojás"] + store["kenyér"]
            if osszertek < min_price:
                min_price = osszertek
                min_index = index
    return (min_index, min_price)


def email_checker(email):
    email = email.strip()
    if not '@' in email or not "." in email:
        return False
    #find the index of '@'
    at_index = -1
    for index, letter in enumerate(email):
        if letter == "@":
            if at_index == -1:
                at_index = index
            else:
                return False
                
    username = email[:at_index]
    if not username.isalpha():
        return False
        
    domain = email[at_index+1:]
    dot_i = first_dot_index(domain)
    sd = domain[:dot_i]
    if not sd.isalpha():
        return False
    pd = domain[dot_i+1:]
    if pd.count(".") > 1:
        return False
    if not pd.replace(".", "").isalpha():
        return False
    return True
    
    
def first_dot_index(str):
    for index, char in enumerate(str):
        if char == ".":
            return index
    return -1




def jaccard(A, B):
    a = set(A)
    b = set(B)
    
    intersection = a.intersection(b)
    union = a.union(b)
    if len(union) == 0:
        return float('NaN')
    J_index = len(intersection) / len(union)
    return J_index



import math

def polygon_perimeter(polygon):
    perimeter = 0
    for i, point in enumerate(polygon[1:]):
        perimeter += dist(polygon[i-1], point)
    
    perimeter += dist(polygon[len(polygon)-1], polygon[0])
    return float(perimeter)

def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)