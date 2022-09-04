from database import DataBase, Menu
import logging
from datetime import datetime
import sys
import os

project_name = "INTRETINERE BLOC"

def cls():
    os.system("cls" if os.name == "nt" else "clear") 

def print_banner(title):
    """Print project banner."""
    cls()
    print("+", "-" * (len(title) + 2), "+", sep="")
    print("|", title, "|")
    print("+", "-" * (len(title) + 2), "+", sep="")

def print_message(*msg):
    print()
    print("-" * 50)
    print(*msg)
    print("-" * 50)
    print()

def get_menu_add_invoices():
    """Show Invoices menu items asking the user for a choice."""
    choice_ok = False
    menu_invoices_entries = {
        1: {"text": "Adauga Factura de Gaze.", "f": Menu.add_gas_invoice_menu},
        2: {"text": "Adauga Factura de Apa Rece.", "f": Menu.add_cold_water_invoice_menu},
        3: {"text": "Adauga Factura de Apa Calda.", "f": Menu.add_hot_water_invoice_menu},
        0: {"text": "Revino la meniul principal.", "f": sys.exit}
    }
    while not choice_ok:
        print_banner("Adauga Contract")
        for k, v in menu_invoices_entries.items():
            print(k, ". ", v["text"], sep="")
        choice = input("\nAlege un numar: ")
        if not choice.isnumeric() or int(choice) not in menu_invoices_entries.keys():
            cls()
            print("EROARE: Te rog sa alegi un numar din lista de mai jos. \n\n")
        else: 
            choice_ok = True
    return menu_invoices_entries[int(choice)]["f"]

def get_main_menu_choice():
    """Show main menu items asking the user for a choice."""
    
    choice_ok = False
    m_menu_entries = {
        1: {"text": "Adauga Bloc.", "f": Menu.add_block_of_flats_menu},
        2: {"text": "Adauga Apartament.", "f": Menu.add_flat_menu},
        3: {"text": "Editare Bloc.", "f": DataBase.add_block_of_flats},
        4: {"text": "Editare Apartament.", "f": DataBase.add_block_of_flats},
        5: {"text": "Adauga Contract.", "f": get_menu_add_invoices},
        6: {"text": "Adauga Index apa.", "f": Menu.add_individual_meter_water_menu},
        7: {"text": "Print Raport.", "f": DataBase.add_block_of_flats},
        0: {"text": "Inchide Programul.", "f": sys.exit}

    }
    while not choice_ok:
        for k, v in m_menu_entries.items():
            print(k, ". ", v["text"], sep="")
        choice = input("\nAlege un numar: ")
        if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
            cls()
            print("EROARE: Te rog sa alegi un numar din lista de mai jos. \n\n")
        else: 
            choice_ok = True
    return m_menu_entries[int(choice)]["f"]
    

def main():
    while True:
        print_banner(project_name)
        current_flow = get_main_menu_choice()
        current_flow()

if __name__ == "__main__":
    main()
