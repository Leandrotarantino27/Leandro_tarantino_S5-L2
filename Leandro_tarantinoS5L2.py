



Python 3 (ipykernel)
nome_scuola = "Epicode"
nome_scuola = "Epicode"
indice = 0
while indice < len(nome_scuola):
    print(nome_scuola[indice])
    indice += 1
E
p
i
c
o
d
e
indice = 0
while indice <= 20:
    print(indice)
    indice += 1
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
indice = 0
power = 1
while indice <= 10:
    print(power)
    power*=2
    indice += 1
1
2
4
8
16
32
64
128
256
512
1024
N = int(input("Inserisci il valore di N: "))
indice = 0
power = 1
while indice < N:
    print(power)
    power *= 2
    indice += 1
Inserisci il valore di N:  5
1
2
4
8
16
indice = 0
power = 1
while power <= 25000:
    print(power)
    power*=2
1
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]
​
studenti_corsi = {"Emma": "Data Analyst", "Faith": "Backend", "Grace": "Frontend", "Henry": "Cybersecurity"}
​
for studente, corso in zip(studenti, corsi):
    if studente not in studenti_corsi:
        studenti_corsi[studente] = corso
​
dati_ordinati = sorted(studenti_corsi.items(), key=lambda x: x[0])
​
for studente, corso in dati_ordinati:
    print(studente, corso)
    
Alex Cybersecurity
Bob Data Analyst
Cindy Backend
Dan Frontend
Emma Data Analyst
Faith Backend
Grace Frontend
Henry Cybersecurity
stringa = input("inserisci stringa,min 6 caratteri:")
lunghezza = len(stringa)
if lunghezza<6:
    print("mi spiace,inserisci più di 6 caratteri,ripova:")
else:
    print(stringa[:3] + "..." +stringa[-3:])
inserisci stringa,min 6 caratteri: sadness
sad...ess
numero = int(input("inserisci un numero: "))
divisori=[]
for indice in range(1, numero+1):
    if numero% indice==0:
        divisori.append(indice)
        print (divisori)
        
inserisci un numero:  345768
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 6]
[1, 2, 3, 4, 6, 8]
[1, 2, 3, 4, 6, 8, 12]
[1, 2, 3, 4, 6, 8, 12, 24]
[1, 2, 3, 4, 6, 8, 12, 24, 14407]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221, 57628]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221, 57628, 86442]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221, 57628, 86442, 115256]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221, 57628, 86442, 115256, 172884]
[1, 2, 3, 4, 6, 8, 12, 24, 14407, 28814, 43221, 57628, 86442, 115256, 172884, 345768]
numero = int(input("Inserisci un numero: "))
n = int(input("Inserisci il numero di potenze da calcolare: "))
potenze = []
for i in range(1, n + 1):
    potenze.append(numero ** i)
print(potenze)

numero = int(input("Inserisci un numero: "))
n = int(input("Inserisci il numero di potenze da calcolare: "))
potenze = []
for i in range(1, n + 1):
    potenze.append(numero ** i)
print(potenze)
​
Inserisci un numero:  2
Inserisci il numero di potenze da calcolare:  30
[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
somma = 0
indice = 0
while indice < len(guadagni):
    somma += guadagni[indice]
    indice += 1
media = somma / len(guadagni)
print("La media guadagno annuale", media, "euro.")
​
La media guadagno annuale 70.0 euro.
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E",
            "XYZABC01D05A789F", "DEFGHI95J06A987G"]

cf_contenenti_95 = [cf for cf in lista_cf if "95" in cf]
print("I seguenti codici fiscali contengono '95':")
print(cf_contenenti_95)
for cf in cf_contenenti_95:
    nome = cf[0:6]
    cognome = cf[6:9]
    print("Nome:", nome)
    print("Cognome:", cognome)
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E",
            "XYZABC01D05A789F", "DEFGHI95J06A987G"]
​
cf_contenenti_95 = [cf for cf in lista_cf if "95" in cf]
print("I seguenti codici fiscali contengono '95':")
print(cf_contenenti_95)
for cf in cf_contenenti_95:
    nome = cf[0:6]
    cognome = cf[6:9]
    print("Nome:", nome)
    print("Cognome:", cognome)
I seguenti codici fiscali contengono '95':
['ABCDEF95G01A123B', 'STUVWX95Z04A654E', 'DEFGHI95J06A987G']
Nome: ABCDEF
Cognome: 95G
Nome: STUVWX
Cognome: 95Z
Nome: DEFGHI
Cognome: 95J
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for i in range(len(studenti)):
    if edizioni[i] == 1:
        print(studenti[i])
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
​
for i in range(len(studenti)):
    if edizioni[i] == 1:
        print(studenti[i])
Alex
Faith
prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]
prezzi_dollari = []
for prezzo in prezzi:
    prezzo_dollari = prezzo.replace("€", "$")
    prezzi_dollari.append(prezzo_dollari)
print(prezzi_dollari)
['100 $', '200 $', '500 $', '10 $', '50 $', '70 $']
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
squadra_pari = studenti[::2]
squadra_dispari = studenti[1::2]
print("Squadra Pari:", squadra_pari)
print("Squadra Dispari:", squadra_dispari)
Squadra Pari: ['Alex', 'Cindy', 'Emma', 'Grace', 'Isabelle']
Squadra Dispari: ['Bob', 'Dan', 'Faith', 'Henry', 'John']