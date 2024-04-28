import os
import sys
import time
import json
from getpass import getpass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour créer le fichier 'users.txt' s'il n'existe pas
def create_users_file_if_not_exists():
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w') as f:
            f.write('{}')

# Fonction pour gérer l'inscription d'un nouvel utilisateur
def signup():
    clear_screen()
    username = input("\nEnter username: ")
    password = input("\nEnter password: ")
    eid = input("\nEnter email id: ")
    mobile_no = input("\nEnter mobile number: ")

    while True:
        try:
            balance = int(input("\nEnter initial balance: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    acc_no = input("\nEnter account number: ")

    # Créer un dictionnai
    # re avec les informations d'inscription
    user_data = {
        'Username': username,
        'Password': password,
        'Email ID': eid,
        'Mobile No': mobile_no,
        'Balance': balance
    }

    try:
        # Charger les données actuelles des utilisateurs
        with open('users.txt', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    # Ajouter les nouvelles données utilisateur au dictionnaire existant
    users[acc_no] = user_data

    # Enregistrer les données mises à jour dans le fichier users.txt
    with open('users.txt', 'w') as f:
        json.dump(users, f)

    print("\nAccount created successfully")
    time.sleep(2)  # Attendre quelques secondes avant de retourner au menu principal
    menu()  # Retour au menu principal après l'inscription réussie

    # Ajouter les nouvelles données utilisateur au dictionnaire existant
    users[acc_no] = user_data

    # Enregistrer les données mises à jour dans le fichier users.txt
    with open('users.txt', 'w') as f:
        json.dump(users, f)

    print("\nAccount created successfully")



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def animation():
    print("\n ############### Welcome to #####################")
    print("\033[94m" + "B" + "\033[0m" + "\033[34m" + "A" + "\033[0m" + "\033[94m" + "N" + "\033[0m" + "\033[34m" + "K" + "\033[0m" + "\033[94m" + "_" + "\033[0m" + "\033[34m" + "I" + "\033[0m" + "\033[94m" + "A" + "\033[0m" + "\033[34m" + "V" + "\033[0m")
    print("▄▄▄█████▓ ██░ ██ ▓█████  ██▀███   ██▓ ███▄    █ ")
    print("▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▓██▒ ██ ▀█   █ ")
    print("▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒")
    print("░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒")
    print("  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██▓ ▒██▒░██░▒██░   ▓██░")
    print("  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒ ")
    print("    ░     ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░")
    print("  ░       ░  ░░ ░   ░     ░░   ░  ▒ ░   ░   ░ ░ ")
    print("          ░  ░  ░   ░  ░   ░      ░           ░ ")
    print("\033[91m  Réalisée par : Dounia Benmoussa et Hiba Echchaia\033[00m")

    #Affiche le message pendant 5 secondes
    time.sleep(5)

    # Efface l'écran
    clear_screen()

def menu():
    clear_screen()
    animation()  # Appel de la fonction d'animation
    print("\n1. Login \n2. Signup \n3. Remove Account \n4. Admin \n5. Exit")
    try:
        user_input = int(input("\nSelect option: "))
        if user_input == 1:
            login()
        elif user_input == 2:
            signup()
        elif user_input == 3:
            remove_account()
        elif user_input == 4:
            admin()
        elif user_input == 5:
            sys.exit()
        else:
            print("Invalid option. Please try again.")
            time.sleep(2)
            menu()
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        menu()

# Fonction pour ajouter un montant au solde
def credit_balance(acc_no):
    try:
        amount = float(input("\nEnter credit amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    with open('users.txt', 'r') as f:
        users = json.load(f)

    if acc_no in users:
        users[acc_no]['Balance'] += amount
        with open('users.txt', 'w') as f:
            json.dump(users, f)
        print(f"\nCredit of {amount} successfully added to account {acc_no}.")
    else:
        print("\nNo such account exists.")
#
# Fonction pour afficher le solde du compte
def show_balance(acc_no):
    with open('users.txt', 'r') as f:
        users = json.load(f)
        if acc_no in users:
            print("\nCurrent balance:", users[acc_no]['Balance'])
        else:
            print("\nNo such account exists.")
# Fonction pour débiter le solde du compte
def debit_balance(acc_no):
    with open('users.txt', 'r+') as f:
        users = json.load(f)
        if acc_no in users:
            while True:
                try:
                    amount = float(input("\nEnter amount to debit: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            if amount > users[acc_no]['Balance']:
                print("\nInsufficient balance.")
            else:
                users[acc_no]['Balance'] -= amount
                f.seek(0)
                json.dump(users, f)
                f.truncate()
                print("\nDebit successful.")
        else:
            print("\nNo such account exists.")
#
# Fonction pour mettre à jour les détails du compte utilisateur
def update_account(acc_no):
    with open('users.txt', 'r') as f:
        users = json.load(f)
        if acc_no in users:
            print("\nCurrent Details:")
            print("1. Username:", users[acc_no]['Username'])
            print("2. Email ID:", users[acc_no]['Email ID'])
            print("3. Mobile Number:", users[acc_no]['Mobile No'])
            print("4. Cancel")
            update_input = input("\nSelect option to update (1-3) or press Enter to cancel: ")
            if update_input == '1':
                new_username = input("\nEnter new username: ")
                users[acc_no]['Username'] = new_username
                print("Username updated successfully.")
            elif update_input == '2':
                new_eid = input("\nEnter new email id: ")
                users[acc_no]['Email ID'] = new_eid
                print("Email ID updated successfully.")
            elif update_input == '3':
                new_mobile_no = input("\nEnter new mobile number: ")
                users[acc_no]['Mobile No'] = new_mobile_no
                print("Mobile number updated successfully.")
            elif update_input == '4':
                pass  # Cancel the update operation
            else:
                print("Invalid option. Please try again.")
        else:
            print("\nNo such account exists.")

    # Enregistrer les données mises à jour dans le fichier users.txt
    with open('users.txt', 'w') as f:
        json.dump(users, f)

# Fonction pour le menu de sous-operations après l'authentification
def submenu(acc_no):
    while True:
        print("\n1. Debit balance \n2. Credit balance \n3. Show balance \n4. Update account details \n5. Show account details \n6. Logout")
        try:
            login_input = int(input("\nSelect option: "))
            if login_input == 1:
                debit_balance(acc_no)
            elif login_input == 2:
                credit_balance(acc_no)
            elif login_input == 3:
                show_balance(acc_no)
            elif login_input == 4:
                update_account(acc_no)
            elif login_input == 5:
                show_account(acc_no)
            elif login_input == 6:
                menu()  # Retour au menu principal
                break  # Sortie de la boucle while
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
#voir le compte bancaire mes informations personnelles 
def show_account(acc_no):
    with open('users.txt', 'r') as f:
        users = json.load(f)
        if acc_no in users:
            print("\nAccount Details:")
            print("Username:", users[acc_no]['Username'])
            print("Email ID:", users[acc_no]['Email ID'])
            print("Mobile Number:", users[acc_no]['Mobile No'])
            print("Balance:", users[acc_no]['Balance'])
        else:
            print("\nNo such account exists.")

# Fonction pour gérer l'authentification de l'utilisateur
def login():
    clear_screen()
    acc_no = input("\nEnter account no: ")
    username = input("\nEnter username: ")
    password = getpass("\nEnter password: ")

    try:
        with open('users.txt', 'r') as f:
            users = json.load(f)
            if acc_no in users:
                if users[acc_no]['Username'] == username and users[acc_no]['Password'] == password:
                    print("\nLogin successful!")
                    time.sleep(2)
                    submenu(acc_no)
                else:
                    print("\nInvalid username or password. Please try again.")
                    time.sleep(2)
                    menu()
            else:
                print("\nNo such account exists.")
                time.sleep(2)
                menu()
    except FileNotFoundError:
        print("\nNo user accounts found. Please sign up first.")
        time.sleep(2)
        menu()
#admin 
def admin():
    clear_screen()
    print("\nAdmin Panel")
    print("1. Remove Single Account")
    print("2. Remove Multiple Accounts")
    print("3. View All Accounts")
    print("4. Back to Main Menu")
    try:
        admin_choice = int(input("\nSelect option: "))
        if admin_choice == 1:
            remove_single_account()
        elif admin_choice == 2:
            remove_multiple_accounts()
        elif admin_choice == 3:
            view_all_accounts()
        elif admin_choice == 4:
            menu()
        else:
            print("Invalid option. Please try again.")
            time.sleep(2)
            admin()
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        admin()

def remove_single_account():
    acc_no = input("\nEnter the account number to remove: ")
    with open('users.txt', 'r') as f:
        users = json.load(f)
    if acc_no in users:
        del users[acc_no]
        with open('users.txt', 'w') as f:
            json.dump(users, f)
        print(f"\nAccount {acc_no} successfully removed.")
    else:
        print("\nNo such account exists.")
    time.sleep(2)
    menu()  # Retour au menu principal après l'opération

def remove_multiple_accounts():
    acc_nos = input("\nEnter the account numbers to remove (separated by commas): ").split(',')
    with open('users.txt', 'r') as f:
        users = json.load(f)
    removed_accounts = []
    for acc_no in acc_nos:
        if acc_no in users:
            del users[acc_no]
            removed_accounts.append(acc_no)
    with open('users.txt', 'w') as f:
        json.dump(users, f)
    if removed_accounts:
        print(f"\nAccounts {', '.join(removed_accounts)} successfully removed.")
    else:
        print("\nNo such accounts exist.")
    time.sleep(2)
    menu()  # Retour au menu principal après l'opération

def view_all_accounts():
    with open('users.txt', 'r') as f:
        users = json.load(f)
    if users:
        print("\nAll Accounts:")
        for acc_no, user_data in users.items():
            print(f"Account Number: {acc_no}")
            print(f"Username: {user_data['Username']}")
            print(f"Email ID: {user_data['Email ID']}")
            print(f"Mobile Number: {user_data['Mobile No']}")
            print(f"Balance: {user_data['Balance']}\n")
    else:
        print("\nNo accounts found.")
    time.sleep(60)
    menu()  # Retour au menu principal après l'opération

# Assurez-vous d'ajouter ces nouvelles fonctions à votre importation des modules et de mettre à jour le menu principal pour inclure l'option d'administration.


# Assurez-vous d'ajouter ces nouvelles fonctions à votre importation des modules et de mettre à jour le menu principal pour inclure l'option d'administration.

# Autres fonctions à définir (remove_account(), admin())

# Programme principal
create_users_file_if_not_exists()
menu()
