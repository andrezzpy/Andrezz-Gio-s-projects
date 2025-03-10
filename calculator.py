print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")
operazione = input("Inserisci il numero per scegliere l'operazione: ")

if (operazione == "1"):
    num1 = input("Inserisci il primo numero: ")
    num2 = input("Inserisci il secondo numero: ")
    somma = int(num1)+int(num2)
    print("Il risultato è: %d" %(somma))
elif (operazione == "2"):
    num1 = input("Inserisci il primo numero: ")
    num2 = input("Inserisci il secondo numero: ")
    diff = int(num1)-int(num2)
    print("Il risultato è: %d" %(diff))
elif (operazione == "3"):
    num1 = input("Inserisci il primo numero: ")
    num2 = input("Inserisci il secondo numero: ")
    molt = int(num1)*int(num2)
    print("Il risultato è: %d" %(molt))
elif (operazione == "4"):
    num1 = input("Inserisci il primo numero: ")
    num2 = input("Inserisci il secondo numero: ")
    div = int(num1)/int(num2)
    print("Il risultato è: %d" %(div))
else:
    print("Numero non valido")



