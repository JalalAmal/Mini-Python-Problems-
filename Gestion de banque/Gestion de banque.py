import random
import csv

Client = {}
Compte = {}
ClientCompte = {}


def ajouterClient(numCl, MPC, numC, SoldeC):
    
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC
    print("Client ajoute avec succes!")
    
def supprimerClient(numCl):
    
    Compte.pop(numCl)
    Compte.pop(ClientCompte[numCl])
    ClientCompte.pop(numCl)
    print("Client supprime avec succes!")
    
        
def Modifier_MPClient(numCl):
    print("Modifier votre MDP: ", end="")
    while True:
        mdp = input()
        if Client[numCl] == mdp:
            print("Enrer un nouveau MDP: ")
        else:
            Client[numCl] = mdp
            print("MDP modifie avec succes!")
            break            
            
    
def Deposer(numCl):
    numC = ClientCompte[numCl]
    Compte[numC] += float(input("Saisir un montant a ajouter: "))

  
def Retirer(numCl):
    numC = ClientCompte[numCl]
    montant = float(input("Saisir un montant a retirer: "))
    
    if Compte[numC] - montant < 0:
        return False
    else: 
        Compte[numC] -= montant
        print(f"Vous avez retire {montant}DH.")
        return True

def rechercherClient(numCl):
    if int(numCl) in ClientCompte: 
        return True
    else:
        return False

    
genererNumCompte = lambda numCl: str(numCl)+str(random.randint(0, 100))

def MenuClient():
    print("**************Menu**************")
    print("1. Afficher mon solde")
    print("2. Deposer une somme d'argent")
    print("3. Retirer une somme d'argent")
    print("4. Modifier mot de passe")


def MenuAgent():
    print("**************Menu**************")
    print("1. Ajouter un compte Client")
    print("2. Supprimer un compte client")
    print("3. Generer un fichier Client CSV")
    print("4. Afficher info")



def EcrireFichierCSV():
    f = open("Clients.csv", "w")
    ecr = csv.DictWriter(f, delimiter=";", fieldnames = ["Client", "Code secret"])
    ecr.writeheader()
    for x, y in Client.items():
        ecr.writerow({"Client": x, "Code secret": y})
    f.close()
        
        
def mdpClient(numCl, mdp):
    if Client[numCl] == mdp:
        
        return True
    else:
        
        return False
    
def mdpAgent(mdp):
    if mdp == "0000":
        return True
    else:
        return False
    
def checkClient(numCl):
    if numCl in Client.keys():
        return True
    else:
        return False
    

        
Compte = {16:200, 234:360}
Client = {1: "5667", 2:"8362"}
ClientCompte = {1:16 , 2:234}   
    

       
r = True
cont = True            
client = 2


while r:
    while True:
        choixAGCL = input("(1) pour client, (2) pour agent: ")
        if choixAGCL == "1" or choixAGCL == "2":
            break
        else:
            r = False
            break
    
    if choixAGCL == "1":
        cont = True
        while True:
            numCl = int(input("Entrer le numero du client: "))
            if checkClient(numCl):
                break
            else:
                print("Pas d'utilisateurs avec ce numero!")
        
        while True:
            mdp = input("Entrer votre MDP: ")
            if mdpClient(numCl, mdp):
                print("MDP correcte!")
                break
            else:
                print("MDP incorrect!")
                
                
        while cont:
            MenuClient()
            choixService = input("Choisir un service: ")
            match choixService:
                case "1":
                    solde = Compte[ClientCompte[numCl]]
                    print(f"Votre solde est de: {solde}DH")
                    
                    cont = False
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                    
                    
                case "2":
                    Deposer(numCl)
                    
                    cont = False
                    cont = bool(input("(1) pour continuer, (ENTER) pour quiter: "))
                    
                    
                case "3":
                    while not Retirer(numCl):
                        print("Solde insufisant!")
                        
                    cont = False
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                        
                        
                case "4":
                    while True:
                        nmdp = input("Choisir un nouveau MDP: ")
                        if mdpClient(numCl, nmdp) == False:
                            mdp = nmdp
                            Client[numCl] = nmdp
                            print("MDP change avec succes!")
                            break
                        else:
                            print("Vous ne pouvez pas entrer un ancien MDP!")
                            
                    cont = False
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                
                    
                                               
    elif choixAGCL == "2":
        cont = True
        while True:
            mdp = input("Entrer votre MDP: ")
            if mdpAgent(mdp):
                print("MDP correcte!")
                break
            else:
                print("MDP incorrect!")
        while cont:
            MenuAgent()
            choixService = input("Choisir un service: ")
            match choixService:
                case "1":
                    client += 1
                    mdp = input("Enter un MDP pour le client: ")
                    numC = genererNumCompte(client)
                    solde = float(input("Combien d'argent le client veut deposer en DH? "))
                    ajouterClient(client, mdp, numC, solde)
                    
                    cont = False   
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                            
                            
                case "2":
                    while True:
                        numCl = int(input("Entrer le numero du client que vous voulez supprimer: "))
                        if checkClient(numCl):
                            supprimerClient(numCl)
                            break
                        else:
                            print("Client introuvable!")
                    
                    cont = False   
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                    
                    
                case "3":
                    EcrireFichierCSV()
                    print("Fichier Client.cvs genere avec succes!")
                    print("Vous pouvez le trouver dans le dossier contenant ce programme.")
                    
                    cont = False   
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                
                
                case "4":
                    print("Liste Client: ")
                    print(Client)
                    print("Liste Compte: ")
                    print(Compte)
                    print("Liste ClientCompte: ")
                    print(ClientCompte)                               

                    cont = False   
                    cont = bool(input("(1) pour continuer, (ENTRER) pour quiter: "))
                    
                    
print("Au revoir!")
                   
                            
                    
        
    
            
            
    


    
    
        