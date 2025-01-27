import sys
# V rifier si deux arguments sont fournis
if len(sys.argv) != 3:
    print("Erreur:Deux arguments sont necessaires.")
    sys.exit(1)
# Interpr ter les arguments
    
try:
    arg1 = float(sys.argv[1]) 
    arg2 = float(sys.argv[2])
except ValueError:
    print("Erreur:Les arguments doiventetre des nombres.")
    sys.exit(1)
    
# Calculer la somme
resultat = arg1 + arg2
# Afficher le r sultat
print(resultat)
