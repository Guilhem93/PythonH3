

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







##TD 2

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