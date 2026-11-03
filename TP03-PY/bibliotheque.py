class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        """Affiche les informations générales du document."""
        print(f"{self.titre} ({self.annee})")


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)  
        self.auteur = auteur

    def afficher(self):
        """Redéfinition de la méthode afficher pour un livre."""
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)  # Initialise les attributs de la classe parente
        self.numero = numero

    def afficher(self):
        """Redéfinition de la méthode afficher pour un magazine."""
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")


if __name__ == "__main__":
    docs = [
        Livre("1984", 1949, "George Orwell"),
        Magazine("Science & Vie", 2023, 456),
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
    ]

    for d in docs:
        d.afficher()