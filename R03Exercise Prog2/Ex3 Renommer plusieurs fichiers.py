# importez os
import os
# # allez dans le dossier Ex3 Videos
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

os.chdir("Ex3 Videos")

# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
for ligne in os.listdir():
    print(ligne)
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
    #ligne1 = os.path.splitext(ligne)
    # #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
    ligne2 =ligne.split('_')
    # #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
    ligne3 = ligne2[0].strip()
    chiffre = ligne2[2].strip()
    chiffre = chiffre[1:]
    # #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
    chiffre = chiffre.zfill(7)
    # #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
    ligne5 = ligne3 + chiffre
    os.rename("ligne", "ligne5")