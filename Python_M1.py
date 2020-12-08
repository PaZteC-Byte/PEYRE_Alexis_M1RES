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
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
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
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
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
    "exo 6 :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
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
      "Entrer une valeur de verite pour A: (entrer False ou True)f\n",
      "Entrer une valeur de verite pour B: (entrer False ou True)f\n",
      "Entrer une valeur de verite pour C: (entrer False ou True)f\n",
      "Entrer une expression Bolenne avec des \"non\", \"ou\", \"et\", et des parentheses:non\n",
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
    "# TD 2 :"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "exo 1 | 1-2 :"
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
    "exo 1 | 3 :"
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
    "exo 1 | 4 :"
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
    "exo 2 | 1 :"
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
    "exo 2 | 2 :"
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
    "exo 3 | 1-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tapez une phrase avec espaces entre chaque mots : je test ce code\n",
      "['ce', 'code', 'je', 'test']\n"
     ]
    }
   ],
   "source": [
    "n = input(\"Tapez une phrase avec espaces entre chaque mots : \")\n",
    "user_list = n.split()\n",
    "list_trie = sorted(user_list)\n",
    "print(list_trie)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-20-23463836df74>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mvaleurs\u001b[0m\u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m7\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m9\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"valet\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"dame\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"roi\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"as\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mx\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mCouleurs\u001b[0m \u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mCouleurs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0my\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mvaleurs\u001b[0m \u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvaleurs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'list' object is not callable"
     ]
    }
   ],
   "source": [
    "Couleurs= [\"Pique\",\"Trefle\",\"Carreau\",\"Coeur\"]\n",
    "valeurs= [2, 3, 4, 5, 6, 7, 8, 9, 10,\"valet\",\"dame\",\"roi\",\"as\"]\n",
    "for x in Couleurs :\n",
    "    print (Couleurs(x))\n",
    "    for y in valeurs :\n",
    "        print(valeurs(y))\n"
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
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
