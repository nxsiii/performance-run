import matplotlib.pyplot as plt 
import random 

# PROJET : PERFORMANCE-AI VISUALIZER

print("Lancement du module d'analyse de données sportives...")
def generer_donnees_entrainement(semaines=10):
    """
    Simule des données de course réalistes.
    Génère une progression non-linéaire (comme dans la vraie vie).
    """
    performances = []
    vitesse_base = 10.0 #km/h

    for i in range(semaines):
        
        facteur_forme = random.uniform(-0.5, 1.2) 
        vitesse_base += facteur_forme
        performances.append(vitesse_base)

    return performances
def afficher_graphique(data):
    """
    Utilise Matplotlib pour générer un rendu visuel professionnel.
    """
    semaines = list(range(1, len(data) + 1))

    
    plt.figure(figsize=(10, 6))
    plt.plot(semaines, data, marker='o', linestyle='-', color='#007acc', label='Vitesse Moyenne (km/h)')

    
    plt.axhline(y=12, color='r', linestyle='--', label='Objectif Seuil (12 km/h)')

    plt.title('Analyse de Progression : Running Performance', fontsize=14, fontweight='bold')
    plt.xlabel('Semaines d\'entraînement')
    plt.ylabel('Vitesse (km/h)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    print(">> 📊 Génération du graphique en cours...")
    plt.show()

donnees = generer_donnees_entrainement(12) # Simulation sur 12 semaines
afficher_graphique(donnees)
