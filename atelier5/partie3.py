class Utilisateur:
    nom=""
    email=""
    mot_de_passe=""
    genre=""
    age=0
    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.genre = genre
        self.age = age

    def display(self):
        print("nom : ",self.nom)
        print("email : ",self.email)
        print("mot de passe : ",self.mot_de_passe)
        print("genre : ",self.genre)
        print("age : ",self.age)


class Module:

    nom = ""
    volume_horaire = 0
    semestre = ""
    MatiereList = []
    def __init__(self, nom="", volume_horaire=0, semestre=""):
        self.nom = nom
        self.volume_horaire = volume_horaire
        self.semestre = semestre

    def display(self):
        print("nom : ",self._nom)
        print("Volumme horaire : ",self.volume_horaire)
        print("semestre : ",self.semestre)


class Professeur(Utilisateur):

    ppr = 0
    grade = ""
    module = Module()
    MatieresList = []
    Annee_AcademiqueList = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super().__init__(self, nom, email, mot_de_passe, genre, age)
        self.ppr = ppr
        self.grade = grade

    def display(self):
        print("ppr : ", ppr)
        print("grade :",grade)


class Matiere:

    nom = ""
    pourcentage = 0.0
    module = Module()
    Annee_AcademiqueList = []
    def __init__(self, nom="", pourcentage=0.0):
        self.nom = nom
        self.pourcentage = pourcentage

    def display(self):
        print("Nom : ", nom)
        print("Pourcentage :",pourcentage,"%")



class Annee_Academique:

    anne = 2022
    EtudiantList = []
    MatiereList = []
    ProfesseurList = []

    def __init__(self, anne=2022):
        self.anne = anne

    def display(self):
        print("anne : ",anne)


class Etudiant(Utilisateur):

    code_massar = ""
    Annee_AcademiqueList = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.code_massar = code_massar

    def display(self):
        print("Code Massar : ",code_massar)


class Evaluation:

    note = 0.0
    matiere = Matiere()
    annee_acadimique = Annee_Academique()
    etudiant = Etudiant()

    def __init__(self, note=0.0):
        self.note = note

    def display(self):
        print("Note : ",note)

