# Cahier des Charges : Système MTS (Metropolis Transit System)

## 1. Objectif du Logiciel

Développer un moteur de gestion et de simulation de transport urbain en Python. L’application doit permettre de modéliser une infrastructure complexe (lignes, arrêts), de gérer une flotte de véhicules hétérogènes (thermiques, électriques) et d'assurer le suivi opérationnel (maintenance, affectation des chauffeurs) via une unité centrale de contrôle.

L'accent est mis sur la **conception orientée objet**, la **robustesse du code** (gestion d'erreurs) et la **modularité**.

---

## 2. Spécifications Fonctionnelles

### Module A : Ressources Humaines et Matérielles

* **Gestion des Chauffeurs :** Chaque chauffeur possède un nom, un matricule unique et un compteur d'heures de conduite. Un chauffeur ne peut pas conduire plus de 10h sans être "mis au repos".
* **La Flotte de Véhicules :** * **Base Commune :** Tout véhicule a un ID, une capacité de passagers et un odomètre (km).
* **Spécificité Thermique :** Gère un réservoir de carburant et une consommation au km.
* **Spécificité Électrique :** Gère une batterie (%) et une autonomie réduite. La charge diminue plus vite si le bus est plein (bonus logique).


* **Système de Maintenance :** Un véhicule doit être marqué "Hors Service" tous les 3000 km pour révision.

### Module B : Infrastructure Réseau

* **Arrêts :** Chaque arrêt a un nom et un "réservoir" de passagers en attente.
* **Lignes :** Une ligne est une séquence ordonnée d'arrêts. Elle doit être capable de calculer sa distance totale (somme des distances entre chaque arrêt).

### Module C : Le Dispatcher (Cœur du système)

La classe `CentraleControle` doit orchestrer l'ensemble :

* **Enregistrement :** Ajouter des bus et des chauffeurs via `*args`.
* **Affectation Dynamique :** Une méthode `assigner_mission` qui prend un véhicule, un chauffeur et une ligne.
* *Vérifications obligatoires :* Le bus est-il en maintenance ? Le chauffeur a-t-il dépassé ses heures ? Le bus a-t-il assez d'énergie pour la ligne complète ?


* **Statut de la Ville :** Une méthode utilisant `**kwargs` pour filtrer et afficher les véhicules selon des critères (ex: `afficher(type="electrique", etat="en_service")`).

---

## 3. Spécifications Techniques & Contraintes

* **Encapsulation :** Aucun attribut sensible (carburant, passagers) ne doit être modifié directement. Utilisez des `getters` et `setters` (ou le décorateur `@property`).
* **Héritage :** Obligation d'utiliser une classe mère `Vehicule` et d'utiliser `super().__init__()` dans les classes filles.
* **Gestion des Exceptions :** Créez des exceptions personnalisées (ex: `EnergyError`, `OverloadError`) pour gérer les cas critiques (panne sèche en plein trajet, bus trop plein).
* **Méthodes Spéciales :** Implémentez `__str__` pour chaque classe pour permettre un débogage lisible dans la console.

---

## 4. Livrables attendus (Scénario de test)

Le programme final doit exécuter le scénario suivant dans un bloc `if __name__ == "__main__":` :

1. Créer 5 arrêts et 2 lignes (A et B).
2. Créer une flotte de 3 bus (2 thermiques, 1 électrique) et 3 chauffeurs.
3. Tenter d'assigner un chauffeur surchargé à un bus en maintenance (doit lever une erreur).
4. Lancer une simulation de "Tournée" :
* Le bus parcourt la ligne.
* À chaque arrêt, il charge le maximum de personnes possibles.
* Afficher l'état du bus à chaque étape.


5. Afficher le rapport final : kilométrage total et nombre total de passagers transportés dans la journée.

---
