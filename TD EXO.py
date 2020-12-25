

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

# Exo 1 | 1-2
c = "X44bf38j23jdjgfjh737nei47"  ## déclaration de la variable avec lettre et chiffre au hasard
c_num = ""  ## déclaration de la variable sans valeur dedans    
c_alpha = ""  ## déclaration de la variable sans valeur dedans 
for caracters in c:             ##Boucle FOR  pour tout élément dans C
    if str.isdigit(caracters) == True:  ##Si la chaine de caractère "caracters" contient des chiffres , la variable c_num s'ajoute + ou égale les chiffres dans la variable C
        c_num += caracters
    else:
        c_alpha += caracters    #sinon la variable c_alpha + ou égale le nombre de chiffre dans la variable caracters

print(c_num, c_alpha) ##a afficher la valeur de C_num et c_alpha

# Exo 1 | 3
str_find = "j23"  ## chaine de caractère find qui permet de retrouver les caractères j23
c.find(str_find) ## Renvoie le premier indice d'apparition  de notre chaine de caractère str_find
if c.find(str_find) != -1: ## si c.find n'est pas égale à -1 alors on déclare une nouvelle variable qui remplace notre chaine de caractere J23 par J24
    new_c = c.replace(str_find, "j24")
    print(new_c) ##affiche notre nouvelle variable qui à remplacé l'ancienne
else : 
    print("Il ")
# Exo 1 | 4
list = ["f","3","7"] ## déclaration d'une liste  avec trois valeurs . 
for string in list: ## Boucle for pour tout élément string dans la liste , on déclare la variable first qui est égale au premier indice de notre apparition de chaine 
    first = c.find(string)
    print(first) ##affiche notre premier indice

print("\n")

# Exo 2 | 1
texte = "We introduce here the Python language"
compteur = 0
for lettre in texte:
    compteur += 1
if compteur == len(texte):
    print("good")
else:
    print("not good")

# Sans compter les espaces
compteur_lettre = 0
for lettre in texte:
    if lettre == " ":
        pass
    else:
        compteur_lettre += 1
print(compteur_lettre)

# Compter les mots dans la variable texte
mots = len(texte.split())
print(mots)

# Exo 2 | 2

# Oui tjrs viable puisque j'ai utilisé le module split

texte2 = "We introduce here the Python language. To learn more about the language, \
consider going through the excellent tutorial https://docs.python.org/ \
tutorial. Dedicated books are also available, such as \
http://www.diveintopython.net/."
mots = len(texte2.split())
print(mots)

# Exo 3 | 1-2
n = input("Entrer des mots separes par un espace : ")
user_list = n.split()
list_triee = sorted(user_list)
print(list_triee)


#EXO 4 

for C in Couleurs:n
       for v in valeurs:
       card = str(v) + " " + str(C)
       deck.append(card)
print(deck)

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

#Exo 6

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

#Exo 7

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

#Exo 8

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
