

##TD 1 

## Exercice 1

x = 4
y = 8
z = 10

print ( x + y - z )
print ( x * y / z )
print ( x ** y - z )

## Exercice 2
a = "Ingrid"
b = "Est-ce que"
c = "Tu chantes ? ?"

print (a, b, c )

#Exercice 3
print ( 2 > 3 )
print ( 2 >= 2 )
print ( 2 < 3 )
print ( 5 == 5 ) 
print ( 2 < 3 ) or ( 2 > 3 )

## Exercice 4
Prenom = 'Guilhem'
Nom = 'Chaminade'
i = 0

nom_complet =  Prenom + Nom

print (nom_complet)

##Exercice 5

while i != 100:
    print ( "G " + "C" )
    i = i +1
a = input("C'est quoi ton petit nom ? ")
b = int (input("C'est quoi ton âge ? "))

##Exercice 6 
Celsius = int (input("Entrez la température : "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print ("Temperature:", Celsius, "Celsius = ", Fahrenheit, "Fahrenheit")

Fahrenheit = ( Celsius - 32) * 5.0/9.0

print ("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " Celsius")


## Exercice 7


#TD2 

#Exercice 1

#
c = "X44bf38j23jdjgfjh737nei47"


#
c_alpha, c_num = "", ""
for x in c:
	if x.isalpha():
		c_alpha = c_alpha + x
	else:
		c_num = c_num + x

print(c_alpha)
print(c_num)


#
if c.find("j23") != 1:
	c = c.replace("j23","j24")


#
i1 = c.find("f")
i2 = c.find("3")
i3 = c.find("7")
#print(i1, i2, i3)

if (i1 < i2) and (i2 < i3):
	print("Le pattern f37 existe dans la chaine de caractère")
else:
	print("Le pattern f37 n'existe pas dans la chaine de caractère")

#Exercice 2

#

texte = "We introduce here the Python language"

counter = 0
for c in texte:
	counter += 1
print(counter)
print(len(texte))

counter = 0
for c in texte:
	if  c != " ":
		counter += 1
print(counter)

# Faire attention à  l'indentation dans ce point

counter = 0
for c in texte:
	if  c == " ":
		counter += 1
counter += 1
print(counter)


#


texte2 = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."
print(texte2)

counter = 0
for c in texte2:
	if  (c == " "):
		counter += 1
counter += 1
print(counter)

#Exercice 3

#
liste_mots = []
m1 = input("Entrer un mot: ")
liste_mots.append(m1)
m2 = input("Entrer un mot: ")
liste_mots.append(m2)
m3 = input("Entrer un mot: ")
liste_mots.append(m3)

liste_mots.sort()

for m in liste_mots:
	print(m)


#
liste_mots2 = []
mot = input("Entrer un mot et taper FIN pour terminer la saisie: ")
while (mot != "FIN") and (mot != "fin"):
	liste_mots2.append(mot)
	mot = input("Entrer un mot et taper FIN pour terminer la saisie: ")

liste_mots2.sort()

for m in liste_mots2:
	print(m)


#
liste_mots2 = []
while True:
	mot = input("Entrer un mot et taper FIN pour terminer la saisie: ")
	if (mot != "FIN") and (mot != "fin"):
		liste_mots2.append(mot)
	else:
		break

liste_mots2.sort()

for m in liste_mots2:
	print(m)

#Exercice 4

#
couleurs = ['Pique', 'Trefle', 'Carreau', 'Coeur']
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']

#liste des 52 cartes
cartes = []
for coul in couleurs:
	for val in valeurs:
		cartes.append(str(val) + " de " + coul)		
print(cartes)

#
from random import shuffle

shuffle(cartes)
print(cartes)

#
joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []

compteur = 0
for c in cartes:
	if compteur == 0:
		joueur1.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 1:
		joueur2.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 2:
		joueur3.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 3:
		joueur4.append(c)
		compteur = (compteur + 1) % 4 

print(joueur1)
print(joueur2)
print(joueur3)
print(joueur4)

#Exercice 6

#
prenom = input("Entrer le prenom de l'etudiant: ")
nom = input("Entrer le nom de l'etudiant: ")
matricule = input("Entrer le matricule de l'etudiant: ")
etudiant = (prenom, nom, matricule)
print(etudiant)


#
liste_etudiants = []
while True:
	prenom = input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		etudiant = (prenom, nom, matricule)
		liste_etudiants.append(etudiant)

#
for e in liste_etudiants:
	print("Prenom:", e[0] + ".", "Nom:", e[1]  + ".", "Matricule:", e[2] + ".")

#Exercice 7

#
dico_fr_ang = {"bonjour" : "Hello", "au revoir" : "bye"}
print(dico_fr_ang)

#
dico_fr_ang["cerveau"] = "brain"
print(dico_fr_ang)

#
for x in dico_fr_ang.keys():
	if x == "cerveau":
		print("la traduction anglaise de", x, "est", dico_fr_ang[x])

#
dico_ang_fr = {}
for k, v in dico_fr_ang.items():
	dico_ang_fr[v] = k
print(dico_ang_fr)

# 
for x in dico_ang_fr.keys():
	if x == "brain":
		print("la traduction francaise de", x, "est", dico_ang_fr[x])

#
for k, v in dico_ang_fr.items():
	if v == "cerveau":
		print(k)

#
dico_fr_ang = {"bonjour" : ["Hello", "Hi"], "au revoir" : ["bye", "bye bye"]}
dico_fr_ang["chemin"] = ["path", "way"]
print(dico_fr_ang)

#
print(dico_fr_ang["chemin"][1])

#Exercice 8

#
print('----1----')
dico_etudiants = {}
prenom = input("Entrer le prenom de l'etudiant: ")
nom = input("Entrer le nom de l'etudiant: ")
matricule = input("Entrer le matricule de l'etudiant: ")
dico_etudiants[nom] = (prenom, nom, matricule)
print(dico_etudiants)

#
print('----2----')
dico_etudiants = {}
while True:
	prenom = input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		dico_etudiants[nom] = (prenom, nom, matricule)

#
print('----3----')
for nom_etud in dico_etudiants:
	print("Prenom:", dico_etudiants[nom_etud][0] + ".", "Nom:", dico_etudiants[nom_etud][1]  + ".", "Matricule:", str(dico_etudiants[nom_etud][2]) + ".")

#
print('----4----')
if "Obama" in dico_etudiants.keys():
	print("Prenom:", dico_etudiants["Obama"][0] + ".", "Nom:", dico_etudiants["Obama"][1]  + ".", "Matricule:", str(dico_etudiants["Obama"][2]) + ".")

#
print('----5----')
for k, v in dico_etudiants.items():
	if v[2] == 12345678:
		print("Prenom:", dico_etudiants[k][0] + ".", "Nom:", dico_etudiants[k][1]  + ".", "Matricule:", str(dico_etudiants[k][2]) + ".")

#
print('----6----')
dico_etudiants = {}
while True:
  prenom = input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		#ici, les clÃ©s deviennent des strings nom + matricule
		dico_etudiants[nom + str(matricule)] = (prenom, nom, matricule)

for nom_matricule in dico_etudiants:
	print("Prenom:", dico_etudiants[nom_matricule][0] + ".", "Nom:", dico_etudiants[nom_matricule][1]  + ".", "Matricule:", str(dico_etudiants[nom_matricule][2]) + ".")
