from django import forms

class Login(forms.Form):
    loginMail = forms.EmailField(label = "", max_length=100, error_messages={
        "required": "Veuillez entrer une adresse valide"
        })
    mdp = forms.CharField(widget=forms.PasswordInput(), error_messages={
        "required": "Veuillez renseigner ce champ"
    })

class AddUser(forms.Form):
    nom = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    prenom = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    addrMail = forms.EmailField(label = "", max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    filiere = forms.CharField(label = "", max_length=100, required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    typeOfUser = forms.BooleanField(label = "", required = False, widget=forms.CheckboxInput(attrs={
        "class": "pointer"
    }))

class ModifyUser(forms.Form):
    nom = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    prenom = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    addrMail = forms.CharField(label = "", max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    filiere = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    typeOfUser = forms.BooleanField(label = "", required = False)

class ModifyDoc(forms.Form):
    titre = forms.CharField(label = "", max_length=100)
    typeOfDoc = forms.CharField(label = "", max_length=100)
    auteur = forms.CharField(label = "", max_length=100)
    resume = forms.CharField(widget=forms.Textarea)
    physique = forms.BooleanField(label="", required=False)
    filePath = forms.FileField(required=False)
    emplacement = forms.IntegerField(min_value=1, required=False)

class Search(forms.Form):
    target = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control shadow border"
    }))

class AddDoc(forms.Form):
    titre = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    typeOfDoc = forms.CharField(
        label = "", 
        max_length=100, 
        widget=forms.Select(
            attrs={
                "class": "form-control mb-4 shadow rounded-0 border"
                }, 
            choices=[
                ("cours", "Cours"), 
                ("dvt", "Développement personnel"), 
                ("epreuves", "Évpreuves"), 
                ("geographie", "Géographie"), 
                ("histoire", "Histoire"), 
                ("memoire", "Mémoire"), 
                ("programmation", "Programmation") 
                ]
            )
        )
    auteur = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    resume = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    physique = forms.BooleanField(label="", required=False)
    filePath = forms.FileField(widget=forms.FileInput(attrs={
        "class": "shadow col-sm-1 col-lg-auto"
    }), required = False)
    emplacement = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }), required = False)
    isbn = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border", 
        "value": "-"
    }))

class MdpForgot(forms.Form):
    loginMail = forms.EmailField(label = "", max_length=100, error_messages={
        "required": "Veuillez entrer une adresse valide"
    })
    recover = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "  Clef de récupération"
        }), error_messages={
            "required": "Veuillez renseigner ce champ"
            })
    options = forms.CharField(widget=forms.RadioSelect(choices=[
        ("all", "Déconnecter de tout les appareils"), 
        ("n", "Ne déconnecter d'aucun appareil")
        ]), required=True)

class AddEmprunt(forms.Form):
    loginMail = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))
    titre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border"
    }))

class xlsFile(forms.Form):
    xls_file = forms.FileField(required=True, widget=forms.FileInput(attrs={"class": "shadow border"}))

class Appreciation(forms.Form):
    note = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "form-control mb-4 shadow rounded-0 border", 
        "placeholder" : "Entrez la valeur de la note", 
        "max": "20"
        }), min_value=1, max_value=20)

class exportUser(forms.Form):
    opt = forms.CharField(required = True, widget=forms.RadioSelect(choices=[
        ("state", "En fonction de l'état"), 
        ("fil", "En fonction de la filière"), 
        ("elig", "En fonction de l'elligibilité"), 
        ("typ", "En fonction du type d'utilisateur"), 
        ("all", "Tout exporter")
        ]))

class exportDoc(forms.Form):
    opt = forms.CharField(required = True, widget=forms.RadioSelect(choices=[
        ("state", "En fonction de l'état"), 
        ("categ", "En fonction de la catégorie"), 
        ("typ", "En fonction du type"), 
        ("disp", "En fonction de la disponibilité"), 
        ("auteur", "En fonction de l'auteur"), 
        ("avg", "En fonction de la moyenne"),
        ("all", "Tout exporter")
        ]))

class firstLogin(forms.Form):
    mdp1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "  Entrez un nouveau mot de passe"
        }), error_messages={
            "required": "Veuillez renseigner ce champ"
            })
    mdp2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "  Retapez le nouveau mot de passe"
        }), error_messages={
            "required": "Veuillez renseigner ce champ"
            })