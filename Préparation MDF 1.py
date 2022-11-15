print("question 1")
Fa=input("Entrez la valeur de la force Fa au point a: ")
D1=input("Entrez la valeur du diametre du piston 1: ")
try:
    Fa=float(Fa)
    PI=3.14
    D1=float(D1)
    PA= (4 * Fa) / (PI * (D1*D1))
    print("la pression PA est : " ,PA, "Pascal")
except:
    print("la valeur de la pression que vous avez donné pas correcte")
print("question 2")
try:
    PA=1910828.0254777067
    PB=PA
    print("la pression PB est : ", PB, "Pascal")
except:
    print("la valeur de la pression que vous avez donné pas correcte")
print("question 3")
D2=input("Entrez la valeur du diametre du piston 2: ")
try:
    D2 = float(D2)
    Fb= (PB*PI*(D2*D2))/4
    print("la force Fb est : ", Fb, "N")
except:
    print("la valeur de la force que vous avez donné pas correcte")


















