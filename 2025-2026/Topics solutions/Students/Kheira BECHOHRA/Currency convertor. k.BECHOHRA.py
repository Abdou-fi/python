print("=== Convertisseur de devises ===")
print("Devises disponibles : DZD, EUR, SAR")

devise_source = input("Entrez la devise de départ : ").upper()
devise_cible = input("Entrez la devise cible : ").upper()

taux = float(input(
    f"Entrez le taux de change (1 {devise_source} = combien de {devise_cible}) : "
))

montant = float(input("Entrez le montant à convertir : "))

resultat = montant * taux

print(f"{montant} {devise_source} = {resultat:.2f} {devise_cible}")