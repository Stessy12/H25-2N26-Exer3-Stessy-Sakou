import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")
print(os.getcwd())


# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")
print(os.environ.get('USERPROFILE'))


# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
print(f"Q3{'_'*60}")
os.chdir(os.environ.get('USERPROFILE')+ "\\Documents")
print(os.getcwd())
# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")
print(os.listdir(os.environ.get('USERPROFILE')+ "\\Documents"))


# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")
#os.makedirs('OS-ExercQ5', exist_ok= True)
#print(os.listdir(os.environ.get('USERPROFILE')+ "\\Documents"))

# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
#os.makedirs('OS-ExercQ6/Subdir1', exist_ok= True)
#print(os.listdir(os.environ.get('USERPROFILE')+ "\\Documents"))

#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q6{'_'*60}")
os.chdir(os.environ.get('USERPROFILE')+ "\\Documents"+ "\\OS-ExercQ6")
os.rmdir('Sous_repertoire')
#os.rename('Subdir1', 'Sous_repertoire')


# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
os.chdir(os.environ.get('USERPROFILE')+ "\\Documents")
os.rmdir("OS-ExercQ6")
print(os.listdir(os.environ.get('USERPROFILE')+ "\\Documents"))




