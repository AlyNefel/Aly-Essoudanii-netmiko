Mon Projet Netmiko


## I. Initialiser un dépôt Git local

1. Créez un nouveau répertoire :

mkdir ali-essoudani-netmiko
2. git init

## II. Ajouter et commiter des fichiers
1. touch README.md
2. git add README.md
   git commit -m "Ajout du fichier README"

3. touch main.py
4. git add main.py
   git commit -m "Ajout du script Python principal"
5. git log --oneline

## III. Créer et fusionner des branches
1. git checkout -b feature/netmiko
3. git add main.py
git commit -m "Ajout de la fonction acces_netmiko"
4. git checkout main
5. git merge feature/netmiko

## IV. Travailler avec un dépôt distant sur GitHub
2. git remote add origin https://github.com/alynefel/ali-essoudanii-netmiko.git
3. git branch -M main
git push -u origin main
6. git fetch origin
git checkout -b feature/salut origin/feature/salut
8. git add main.py
git commit -m "Ajout de la fonction dire_salut"
9. git push origin feature/salut
12. git checkout main
git pull origin main

