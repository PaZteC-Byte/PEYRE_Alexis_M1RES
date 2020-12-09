{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TD1 :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 10\n",
    "y = 3\n",
    "z = x - y \n",
    "print (z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 10\n",
    "y = 3\n",
    "z = 1 \n",
    "print (x + y - z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30.0\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 3\n",
    "z = 1 \n",
    "print (x * y / z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000.0\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 3\n",
    "z = 1 \n",
    "print (x ** y / z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "y = 3\n",
    "z = 1 \n",
    "print (x % y ** 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 2 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "peyre alexis peyre alexis \n"
     ]
    }
   ],
   "source": [
    "nom = \"peyre\"\n",
    "prenom = \"alexis\"\n",
    "print(( nom + \" \" + prenom + \" \" ) * 2 )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 3 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "bool1 = 'true'\n",
    "bool2 = 'fasle'\n",
    "boolsome = bool1 <= bool2\n",
    "print(boolsome)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 4 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 5 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 6 : cassé ne pas lancer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#Celsius = float(input(\"Enter a temperature in Celsius: \"))\n",
    "\n",
    "#Fahrenheit = (9.0/5.0) * Celsius + 32\n",
    "\n",
    "#print(\"Temperature:\", Celsius, \"Celsius = \", Fahrenheit, \" F\")\n",
    "#Fahrenheit = float(input(\"Enter a temperature in Fahrenheit: \"))\n",
    "\n",
    "#Celsius = (Fahrenheit - 32) * 5.0/9.0\n",
    "\n",
    "#print(\"Temperature:\", Fahrenheit, \"Fahrenheit = \", Celsius, \" C\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 7 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer une valeur de verite pour A: (entrer False ou True)true\n",
      "Entrer une valeur de verite pour B: (entrer False ou True)true\n",
      "Entrer une valeur de verite pour C: (entrer False ou True)false\n",
      "Entrer une expression Bolenne avec des \"non\", \"ou\", \"et\", et des parentheses:ou\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "A=input('Entrer une valeur de verite pour A: (entrer False ou True)')\n",
    "B=input('Entrer une valeur de verite pour B: (entrer False ou True)')\n",
    "C=input('Entrer une valeur de verite pour C: (entrer False ou True)')\n",
    "\n",
    "expression_bol=input('Entrer une expression Bolenne avec des \"non\", \"ou\", \"et\", et des parentheses:')\n",
    "expression_bol.replace('non', 'not')\n",
    "expression_bol.replace('et', 'and')\n",
    "expression_bol.replace('ou', 'or')\n",
    "print (bool(expression_bol))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# #___________________________________________________________"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TD 2 :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 (1-2) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44382373747 Xbfjjdjgfjhnei\n"
     ]
    }
   ],
   "source": [
    "valeur = \"X44bf38j23jdjgfjh737nei47\"\n",
    "valeur_numero = \"\"\n",
    "valeur_lettre = \"\"\n",
    "for symboles in valeur:\n",
    "    if str.isdigit(symboles) == True:\n",
    "        valeur_numero += symboles\n",
    "    else:\n",
    "        valeur_lettre += symboles\n",
    "\n",
    "print(valeur_numero, valeur_lettre)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 (3) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X44bf38j24jdjgfjh737nei47\n"
     ]
    }
   ],
   "source": [
    "str_find = \"j23\"\n",
    "valeur.find(str_find)\n",
    "if valeur.find(str_find) != -1:\n",
    "    nouvelle_valeur = valeur.replace(str_find, \"j24\")\n",
    "    print(nouvelle_valeur)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 (4) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "5\n",
      "17\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "list = [\"f\",\"3\",\"7\"]\n",
    "for string in list:\n",
    "    premierevaleur = valeur.find(string)\n",
    "    print(premierevaleur)\n",
    "\n",
    "print(\"\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 2 (1) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "good\n",
      "32\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "txt = \"We introduce here the Python language\"\n",
    "compteur = 0\n",
    "for lettres in txt:\n",
    "    compteur += 1\n",
    "if compteur == len(txt):\n",
    "    print(\"good\")\n",
    "else:\n",
    "    print(\"not good\")\n",
    "\n",
    "compteur_lettres = 0\n",
    "for lettres in txt:\n",
    "    if lettres == \" \":\n",
    "        pass #saute les espaces\n",
    "    else:\n",
    "        compteur_lettres += 1\n",
    "print(compteur_lettres) #affiche le nombres de lettres dans le texte\n",
    "\n",
    "mots = len(txt.split())  \n",
    "\n",
    "print(mots) #affiche le nombre de mots "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 2 (2) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "202\n",
      "28\n"
     ]
    }
   ],
   "source": [
    "txt2 = \"We introduce here the Python language. To learn more about the language, \\\n",
    "consider going through the excellent tutorial https://docs.python.org/ \\\n",
    "tutorial. Dedicated books are also available, such as \\\n",
    "http://www.diveintopython.net/.\"\n",
    "\n",
    "compteur_lettres = 0\n",
    "for lettres in txt2:\n",
    "    if lettres == \" \":\n",
    "        pass #saute les espaces\n",
    "    else:\n",
    "        compteur_lettres += 1\n",
    "print(compteur_lettres) #affiche le nombres de lettres dans le texte\n",
    "\n",
    "mots = len(txt2.split())\n",
    "\n",
    "print(mots) #affiche le nombre de mots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 3 (1-2) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tapez une phrase avec espaces entre chaque mots : je test cette phrase\n",
      "['cette', 'je', 'phrase', 'test']\n"
     ]
    }
   ],
   "source": [
    "n = input(\"Tapez une phrase avec espaces entre chaque mots : \")\n",
    "user_list = n.split()\n",
    "list_trie = sorted(user_list) \n",
    "print(list_trie)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 4 (1-3) :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Joueur 1 = ['♦ Carreau 5', '♣ Trefle 6', '♠ Pique As', '♠ Pique 6', '♦ Carreau 8', '♠ Pique Roi', '♥ Coeur 9', '♦ Carreau Valet', '♦ Carreau 3', '♥ Coeur 6', '♣ Trefle 2', '♣ Trefle 10', '♠ Pique 4']\n",
      " Joueur 2 = ['♣ Trefle 4', '♥ Coeur 8', '♠ Pique Valet', '♦ Carreau 7', '♠ Pique 9', '♥ Coeur 7', '♠ Pique 7', '♠ Pique 8', '♥ Coeur 4', '♥ Coeur 5', '♣ Trefle 5', '♦ Carreau As', '♥ Coeur 10']\n",
      " Joueur 3 = ['♣ Trefle 9', '♠ Pique 10', '♥ Coeur As', '♦ Carreau 2', '♦ Carreau 4', '♥ Coeur 3', '♦ Carreau Dame', '♠ Pique 3', '♠ Pique Dame', '♦ Carreau Roi', '♦ Carreau 9', '♥ Coeur Valet', '♣ Trefle 7']\n",
      " Joueur 4 = ['♥ Coeur Dame', '♣ Trefle Valet', '♦ Carreau 10', '♦ Carreau 6', '♣ Trefle Roi', '♣ Trefle 3', '♣ Trefle Dame', '♥ Coeur Roi', '♣ Trefle 8', '♥ Coeur 2', '♠ Pique 5', '♣ Trefle As', '♠ Pique 2']\n"
     ]
    }
   ],
   "source": [
    "from random import *; \n",
    "\n",
    "Couleurs= [\"♠ Pique\",\"♣ Trefle\",\"♦ Carreau\",\"♥ Coeur\"]\n",
    "valeurs= [2,3,4,5,6,7,8,9,10,\"Valet\",\"Dame\",\"Roi\",\"As\"]\n",
    "paquet = []\n",
    "joueur_1 = []\n",
    "joueur_2 = []\n",
    "joueur_3 = []\n",
    "joueur_4 = []\n",
    "\n",
    "for C in Couleurs: #boucle for de navigation pour les couleurs\n",
    "    for v in valeurs: #boucle for de navigation pour les noms de cartes\n",
    "        carte = str(C) + \" \" + str(v) #assemblage des variables listé dans Couleurs et Valeurs\n",
    "        paquet.append(carte)\n",
    "\n",
    "shuffle(paquet) #mélange du paquet\n",
    "\n",
    "for carte_par_joueur in range(13): #boucle de distribution (13) = nb de carte par joueurs\n",
    "    joueur_1.append(paquet[carte_par_joueur]) #13 premiere carte\n",
    "    joueur_2.append(paquet[carte_par_joueur + 13])#décale de 13 cartes dans le paquet\n",
    "    joueur_3.append(paquet[carte_par_joueur + 26])#décale de 26 cartes dans le paquet\n",
    "    joueur_4.append(paquet[carte_par_joueur + 39])#décale de 39 cartes dans le paquet\n",
    "\n",
    "print(\" Joueur 1 = \" + str(joueur_1))\n",
    "print(\" Joueur 2 = \" + str(joueur_2))\n",
    "print(\" Joueur 3 = \" + str(joueur_3))\n",
    "print(\" Joueur 4 = \" + str(joueur_4))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 5 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "53941\n",
      "['\"carat\",\"cut\",\"color\",\"depth\",\"price\",\"x\",\"y\",\"z\"\\n', '\"0.23\",\"Ideal\",\"E\",\"61.5\",\"326\",\"3.95\",\"3.98\",\"2.43\"\\n', '\"0.21\",\"Premium\",\"E\",\"59.8\",\"326\",\"3.89\",\"3.84\",\"2.31\"\\n']\n"
     ]
    }
   ],
   "source": [
    "# (1)\n",
    "with open('diamonds.csv', 'r') as cs: #appel au csv sous le nom de cs\n",
    "    diamants = cs.readlines() \n",
    "    print(len(diamants)) #nb de diamants dans la liste\n",
    "    print(diamants[0:3]) #affiche les trois premieres lignes du csv\n",
    "\n",
    "# (2)\n",
    "num_ligne = 0\n",
    "for lignes in diamants:\n",
    "    num_ligne += 1\n",
    "    final = lignes.split(\",\")\n",
    "    #print(final, num_ligne) #test de visualisation du numéro de ligne\n",
    "cs.close() #fermeture de l'appel cvs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('diamonds.csv', 'r') as cs: #appel au csv sous le nom de cs\n",
    "    diamants_100 = [next(cs) for i in range(100)] #\"\"[next(f) for i in range(100)]\"\" permet de ne selectionner que les 100 premiers diamants de la liste\n",
    "    #print(diamants_100[0:20]) #affiche les 20 premiers diamants\n",
    "cs.close() #fermeture de l'appel cvs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[326.0, 326.0, 327.0, 334.0, 335.0, 336.0, 336.0, 337.0, 337.0, 338.0, 339.0, 340.0, 342.0, 344.0, 345.0, 345.0, 348.0, 351.0, 351.0, 351.0]\n"
     ]
    }
   ],
   "source": [
    "with open('diamonds.csv', 'r') as cs: #appel au csv sous le nom de cs\n",
    "    diamants_prix = [] #futur list des prix des 100 premiers diamants \n",
    "    diamants = cs.readlines() #récupère le nombre de lignes de données dans le csv\n",
    "    for lignes in diamants: \n",
    "        donnees = lignes.split(\",\")\n",
    "        donnees = [i.replace('\"', '').replace(\"\\n\", \"\") for i in donnees]\n",
    "        try:\n",
    "            diamants_prix += [float(donnees[4])]\n",
    "        except ValueError: #si la valeur est null ou non renseigné, la valeur n'est pas pris en compte\n",
    "            pass\n",
    "cs.close() #fermeture e l'appel cvs\n",
    "\n",
    "print(diamants_prix[0:20]) #affichage des 20 premiers prix de diamants"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 6 (1-3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces : test1 test1 10\n",
      "<class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "values = input(\"Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces : \")\n",
    "liste = values.split(\" \")\n",
    "#tuple = tuple(liste)\n",
    "print(tuple)\n",
    "liste_entiere = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces :(Entrer 'FIN' pour finir la saisie)test1 test1 11\n",
      "Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces :(Entrer 'FIN' pour finir la saisie)test2 test2 12\n",
      "Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces :(Entrer 'FIN' pour finir la saisie)test3 test3 13\n",
      "Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces :(Entrer 'FIN' pour finir la saisie)FIN\n"
     ]
    }
   ],
   "source": [
    "#(2)\n",
    "#tuple = tuple(liste)\n",
    "while True: #tant que l'utilisateur ne rentre pas FIN la boucle continue de remplir le Tuple\n",
    "    choix = input(\"Veuillez rentrer votre prénom, nom et matricule d'étudiant séparés par des espaces :(Entrer 'FIN' pour finir la saisie)\")\n",
    "    if choix == \"FIN\":\n",
    "         break\n",
    "    else:\n",
    "        liste = choix.split(\" \")\n",
    "        montuple = tuple(liste)\n",
    "        liste_entiere.append(montuple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "___________________________________________________\n",
      "| Matricule : 11 | Mme/Mr : test1 test1 \n",
      "| Matricule : 12 | Mme/Mr : test2 test2 \n",
      "| Matricule : 13 | Mme/Mr : test3 test3 \n",
      "___________________________________________________\n"
     ]
    }
   ],
   "source": [
    "#(3)\n",
    "print(\"___________________________________________________\")\n",
    "for etudiant in liste_entiere:\n",
    "    print(\"| Matricule : \" + etudiant[2] + \" | Mme/Mr : \" + etudiant[1] + \" \" + etudiant[0] +\" \")\n",
    "print(\"___________________________________________________\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 7 (1-3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "brain\n"
     ]
    }
   ],
   "source": [
    "fr_en = {\n",
    "    \"ordinateur\": \"computer\",\n",
    "    \"clavier\": \"keyboard\",\n",
    "    \"Tasse\": \"mug\",\n",
    "    \"cerveau\": \"brain\"\n",
    "    }\n",
    "for cle, valeur in fr_en.items():\n",
    "    if cle == \"cerveau\": #si la clé est égale à \"mot en français\" il retourne la valeur \n",
    "        print(valeur)\n",
    "    else:\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'computer': 'ordinateur', 'keyboard': 'clavier', 'mug': 'Tasse', 'brain': 'cerveau'}\n"
     ]
    }
   ],
   "source": [
    "en_fr = {}\n",
    "for cle, valeur in fr_en.items():\n",
    "    en_fr[valeur] = cle  # assigne cette cle cette valeur\n",
    "print(en_fr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n'est pas présent dans le dictionnaire\n"
     ]
    }
   ],
   "source": [
    "if \"allo\" in (en_fr): # par défaut dans les clés pour values .values\n",
    "    print(\"est présent dans le dictionnaire\")\n",
    "else :\n",
    "    print(\"n'est pas présent dans le dictionnaire\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anglais = brain | Français = cerveau\n"
     ]
    }
   ],
   "source": [
    "for cle, values in en_fr.items():\n",
    "    if en_fr[cle] == \"cerveau\":\n",
    "        print(\"Anglais = \" + cle, \"| Français = \" + values)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "la deuxième traduction de clavier est : keypad\n",
      "vérification de suppréssion du mot clavier du dictionnaire\n",
      "{'ordinateur': ['computer', 'PC'], 'tasse': ['mug', 'cup'], 'cerveau': ['brain', 'cerebral'], 'chemin': ['path', 'way']}\n"
     ]
    }
   ],
   "source": [
    "new = {\n",
    "    \"ordinateur\": [\"computer\", \"PC\"],\n",
    "    \"clavier\": [\"keyboard\", \"keypad\"],\n",
    "    \"tasse\": [\"mug\", \"cup\"],\n",
    "    \"cerveau\": [\"brain\", \"cerebral\"],\n",
    "    \"chemin\" : [\"path\", \"way\"]\n",
    "    }\n",
    "\n",
    "for cle, values in new.items():\n",
    "    if cle == \"clavier\":\n",
    "        print (\"la deuxième traduction de clavier est : \" + values[1])#Affichage de la deuxieme traduction\n",
    "\n",
    "del new[\"clavier\"] #drop du mot clavier du dictionnaire\n",
    "\n",
    "print (\"vérification de suppréssion du mot clavier du dictionnaire\")\n",
    "print(new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 8 (1-2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) Test1 test1 11\n",
      "Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) Test2 test2 12\n",
      "Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) Test3 test3 13\n",
      "Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) FIN\n",
      "{'test1': ('Test1', 'test1', '11'), 'test2': ('Test2', 'test2', '12'), 'test3': ('Test3', 'test3', '13')}\n"
     ]
    }
   ],
   "source": [
    "etudiant = {}\n",
    "\n",
    "while True:\n",
    "    choix = input(\"Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) \")\n",
    "    if choix == \"FIN\":\n",
    "         break\n",
    "    else:\n",
    "        list = choix.split(\" \")\n",
    "        montuple = tuple(list)\n",
    "        count = 0\n",
    "        for cle in etudiant.keys():\n",
    "            if montuple[1] in cle:\n",
    "                count += 1\n",
    "        if count > 0:\n",
    "            new_key = montuple[1] + str(count)\n",
    "            etudiant[new_key] = montuple\n",
    "        else:\n",
    "            etudiant[montuple[1]] = montuple\n",
    "            \n",
    "print(etudiant)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 8 (3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nom étudiant : test1\n",
      "Nom étudiant : test2\n",
      "Nom étudiant : test3\n"
     ]
    }
   ],
   "source": [
    "for keys in etudiant.keys():\n",
    "    print(\"Nom étudiant : \" + keys)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 8 (4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c'est qui encore celui ci\n"
     ]
    }
   ],
   "source": [
    "if \"Obama\" in (etudiant):\n",
    "    print(etudiant[\"Obama\"])\n",
    "else :\n",
    "    print (\"c'est qui encore celui ci\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 8 (5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "for cle, values in etudiant.items():\n",
    "    if values[2] == \"20\":\n",
    "        print(\"cle \" + str(cle), \"valeur \" + str(values))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# #___________________________________________________________"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TD 3 :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer un nombre à multiplier : 5\n",
      "5\n",
      "10\n",
      "15\n",
      "20\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "user = int(input(\"Entrer un nombre à multiplier : \"))\n",
    "for x in range(1,6):\n",
    "    print(user*x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer un nombre à multiplier : 5\n",
      "5 10 15 20 25 30 35 40 45 50 "
     ]
    }
   ],
   "source": [
    "user = int(input(\"Entrer un nombre à multiplier : \"))\n",
    "for x in range(1, 11):\n",
    "    print(user*x, end=\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez entrer le nombre table que vous souhaitez visualisé : 2\n",
      "Table de 1 :\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "Table de 2 :\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "user = int(input(\"Veuillez entrer le nombre table que vous souhaitez visualisé : \"))\n",
    "for x in range(user):\n",
    "    print(\"Table de\", int(x) + 1, \":\")\n",
    "    for i in range(1, 11):\n",
    "        print((x+1)*i,)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez entrer le nombre d'asterisk à afficher : 5\n",
      " * \n",
      " *  * \n",
      " *  *  * \n",
      " *  *  *  * \n",
      " *  *  *  *  * \n"
     ]
    }
   ],
   "source": [
    "user = int(input(\"Veuillez entrer le nombre d'asterisk à afficher : \"))\n",
    "for x in range(user):\n",
    "    print(\" * \" * (x+1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer un nombre à afficher en asterisk : 5\n",
      "    * \n",
      "   * * \n",
      "  * * * \n",
      " * * * * \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "user = int(input(\"Entrer un nombre à afficher en asterisk : \"))\n",
    "for x in range(user):\n",
    "    print(\" \" * ((user-1)-x) + (\"* \" * (x+1)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 2 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Janvier', 31), ('Février', 28), ('Mars', 31), ('Avril', 30), ('Mai', 31), ('Juin', 30), ('Juillet', 31), ('Août', 31), ('Septembre', 30), ('Octobre', 31), ('Novembre', 30), ('Décembre', 31)]\n"
     ]
    }
   ],
   "source": [
    "jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n",
    "mois = [\"Janvier\", \"Février\", \"Mars\", \"Avril\", \"Mai\", \"Juin\", \"Juillet\", \"Août\", \"Septembre\", \"Octobre\", \"Novembre\", \"Décembre\"]\n",
    "moisjours = []\n",
    "for x in range(len(jours)):\n",
    "    moisjours.append((mois[x], jours[x]))\n",
    "\n",
    "print (moisjours)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "annee = []\n",
    "for month in moisjours:\n",
    "    for x in range(month[1]):\n",
    "        annee.append((str(x+1)) + \" \" + month[0])\n",
    "#print (annee)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "jours_de_la_semaine = [\"Lundi\", \"Mardi\", \"Mercredi\", \"Jeudi\", \"Vendrdi\", \"Samedi\", \"Dimanche\"]\n",
    "for jour in range(365):\n",
    "    annee.append(jours_de_la_semaine[jour%len(jours_de_la_semaine)] + \" \" + annee[jour])\n",
    "#print (annee)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 3 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez entrer la note : 5\n",
      "Veuillez entrer la note : 15\n",
      "Veuillez entrer la note : 20\n",
      "moyenne générale : 13.333333333333334 | minimum : 5.0 | maximum : 20.0\n"
     ]
    }
   ],
   "source": [
    "relevee_notes = []\n",
    "while len(relevee_notes) < 3:\n",
    "    compteur_de_notes = 0\n",
    "    utilisateur = float(input(\"Veuillez entrer la note : \"))\n",
    "    relevee_notes.append(utilisateur)\n",
    "\n",
    "minimum = min(relevee_notes)\n",
    "maximum = max(relevee_notes)\n",
    "somme = 0\n",
    "\n",
    "for notes in relevee_notes:\n",
    "    somme += float(notes)\n",
    "moyenne = (somme/len(relevee_notes))\n",
    "\n",
    "print(\"moyenne générale : \" + str(moyenne), \"| minimum : \" + str(minimum), \"| maximum : \" + str(maximum))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Veuillez entrer le nombre de notes que vous voulez saisir ? 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "Veuillez entrer une note : 15\n",
      "moyenne 14.666666666666666 minimum 5.0 maximum 20.0\n"
     ]
    }
   ],
   "source": [
    "nb_de_note= int(input(\"Veuillez entrer le nombre de notes que vous voulez saisir ? \"))\n",
    "\n",
    "while len(relevee_notes) < nb_de_note:\n",
    "    utilisateur = int(input(\"Veuillez entrer une note : \"))\n",
    "    relevee_notes.append(utilisateur)\n",
    "    \n",
    "minimum = min(relevee_notes)\n",
    "maximum = max(relevee_notes)\n",
    "somme = 0\n",
    "\n",
    "for notes in relevee_notes:\n",
    "    somme += int(notes)\n",
    "    \n",
    "moyenne = (somme / len(relevee_notes))\n",
    "\n",
    "print(\"moyenne \" + str(moyenne), \"minimum \" + str(minimum), \"maximum \" + str(maximum))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer une note : (fin pour finir) 15\n",
      "Entrer une note : (fin pour finir) 15\n",
      "Entrer une note : (fin pour finir) 15\n",
      "Entrer une note : (fin pour finir) 15\n",
      "Entrer une note : (fin pour finir) 15\n",
      "Entrer une note : (fin pour finir) fin\n",
      "moyenne 14.75 minimum 5.0 maximum 20.0\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    utilisateur = input(\"Entrer une note : (fin pour finir) \")\n",
    "    if utilisateur == \"fin\":\n",
    "        break\n",
    "    else:\n",
    "        relevee_notes.append(float(utilisateur))\n",
    "        minimum = min(relevee_notes)\n",
    "        maximum = max(relevee_notes)\n",
    "        somme = 0\n",
    "        for notes in relevee_notes:\n",
    "            somme += int(notes)\n",
    "        moyenne = (somme / len(relevee_notes))\n",
    "\n",
    "print(\"moyenne \" + str(moyenne), \"minimum \" + str(minimum), \"maximum \" + str(maximum))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 4 :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from random import *;\n",
    "\n",
    "def exo4():\n",
    "    aleatoire1 = randint(1,100)\n",
    "    correct = False\n",
    "    while not correct:\n",
    "        user = int(input(\"Devine le nombre entre 1 et 100 \"))\n",
    "        if aleatoire1 > user:\n",
    "            print(\"Trop petit\")\n",
    "        elif aleatoire1 < user:\n",
    "            print(\"trop grand\")\n",
    "        elif aleatoire1 == user:\n",
    "            break\n",
    "\n",
    "    if aleatoire1 == user:\n",
    "        rejoue = input (\"bien ouej fréro on rejoue ? (y or n) \")\n",
    "        if rejoue == 'y':\n",
    "            exo4()\n",
    "exo4()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "def justeprix():\n",
    "    juste_prix = 500\n",
    "    correct = False\n",
    "    while not correct:\n",
    "        saisi_utilisateur = int(input(\"Bienveue au Juste prix, Devine maintemant le prix exact entre 1 et 100 \"))\n",
    "        if juste_prix > saisi_utilisateur:\n",
    "            print(\"Plus grand\")\n",
    "        elif juste_prix < saisi_utilisateur:\n",
    "            print(\"Plus petit\")\n",
    "        elif juste_prix == saisi_utilisateur:\n",
    "            break\n",
    "\n",
    "    if juste_prix == saisi_utilisateur:\n",
    "        rejouer = input (\"Bravo c'est gagné, voulez-vous rejouer ? (y or n) \")\n",
    "        if rejouer == 'y':\n",
    "            justeprix()\n",
    "justeprix()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
