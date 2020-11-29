<p align="RIGHT"> <a href ="https://github.com/DSAghicha/Credit-Calculator/blob/main/README.md">EN</a></p>

# Calculateur de Crédit

#### Créé à l’aide [Python 3.8](https://www.python.org/)

Ce programme est utile pour calculer les Paiements de Rente et les Paiements de Différenciés.

Navigation rapide:
- [Installation](FR_README.md#installation)
- [Détails du Programme](FR_README.md#détails-du-programme)
- [Paiements de Rente](FR_README.md#paiements-de-rente)
- [Paiements de Différenciés](FR_README.md#paiements-de-différenciés)
- [Crédits](FR_README.md#crédits)

### Installation

   Installer Python à partir d’ici -> [lien](https://www.python.org/downloads/)
   
   Pour vérifier si Python est installé correctement ouvert Command Prompt sur votre PC et tapez le code suivant:
   ```python  --version``` 
   
   Cela devrait renvoyer le numéro de version Python s’il est correctement installé

### Détails du Programme

Parfois, nous avons besoin d’un peu d’argent supplémentaire, donc, nous décidons de prendre un prêt.

Ce prêt peut être remboursé soit **rente mensuelle** ou **paiements différenciés**.

Ce programme peut être utilisé en deux formats:

1. Command Line Interface
   
   **Étapes**

   - Télécharger **cli.zip** de [Releases](https://github.com/DSAghicha/Credit-Calculator/releases/latest) et dézipez-le sur votre PC.
    
     Ce fichier zip aura un répertoire qui aura deux fichiers ```main.py``` & ```cli.py```.
   - Ouvrez le Terminal dans cet annuaire et exécutez ```python cli.py```.
   
     Alternativement, vous pouvez l’ouvrir dans votre éditeur de code préféré et l’exécuter à partir de là aussi.
        
2. Command Line Arguments
   
   **Étapes**
   
   - Télécharger **cl_args.zip** de [Releases](https://github.com/DSAghicha/Credit-Calculator/releases/latest) et dézipez-le sur votre PC.
   
     Ce fichier zip aura un répertoire qui aura deux fichiers ```main.py``` & ```arg_based.py```.
   - Ouvrez le Terminal dans cet annuaire et exécutez ```python arg_based.py --help```.
   
      Vous verrez la liste de tous les arguments facultatifs que vous devez fournir. Le script détectera celui qui n’est pas fourni et calculera ses résultats.
      
      ```python arg_based.py --all optional arguments```

__*For Demo: [Check out this video]()*__

### Paiements de Rente

*Le paiement de la rente* demeure inchangé pendant toute la durée de la convention de crédit. Cela signifie que chaque mois, vous paierez le prêt par versements égaux, qui se composent d’intérêts courus par prêt et d’une partie du capital.

La formule de calcul *Paiement de rente* est la suivante:

![formule de rente](https://user-images.githubusercontent.com/53931676/100551371-fff26380-32a5-11eb-88cb-72255d4241b4.png)

Les formules de calcul du capital de prêt et du nombre de paiements sont les suivantes ::

![formule de principal de prêt](https://user-images.githubusercontent.com/53931676/100551391-20222280-32a6-11eb-88bc-0e885ad567e8.png)

![formule de période](https://user-images.githubusercontent.com/53931676/100551405-3af49700-32a6-11eb-8f81-2f48f8eeb2e3.png)

<p>
    where,<br>
    <b>A<sub>ordinary_annuity</sub></b> = annuity payment;<br>
    <b>P</b> = loan principal;<br>
    <b>i</b> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage;<br>
    <b>n</b> = number of payments. This is usually the number of months in which repayments will be made.
</p>

### Differentiated Payment

In the case of *differentiated payments*, your monthly payment will decrease because the debt will be extinguished in equal installments and  interest will accrue monthly on the balance of the debt.

The formula to calculate *Differentiated Payment* is as follows:

![diff_formula](https://user-images.githubusercontent.com/53931676/100551415-58296580-32a6-11eb-859c-2d35ad7d704e.png)

<p>
    where,<br>
    <b>D<sub>m</sub></b> = mth differentiated payment;<br>
    <b>P</b> = loan principal;<br>
    <b>i</b> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage;<br>
    <b>n</b> = number of payments. This is usually the number of months in which repayments will be made;<br>
    <b>m</b> = current repayment month.
</p>

### Crédits

This project was a part of Hyperskill's teaching program to teach Python.

```arg_based.py``` & ```main.py``` files in  particular were submitted as my coursework.

**[Hyperskill](https://hyperskill.org/)** is a platform created by Jet Brains Academy which offers interactive project-based learning combined with powerful, professional development tools.

Be sure to check them out...

Let me know if you have any other queries...
