import pathlib
import sqlite3
import logging
import sys



ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db/intretinere_bloc.db")

# configure logger
logging.root.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s")


class Menu:
    
    @staticmethod
    def add_block_of_flats_menu():       
        return {
            "nr_bloc": input("Adauga numarul de bloc: "),
            "scari": input("Cate scari are blocul?: "),
            "etaje": input("Cate etaje are blocul?: "),
            "apartamente": input("Cate apartamente se afla in bloc?: "),
            "adresa": input("Adresa blocului: ")          
        }
    
    @staticmethod
    def add_flat_menu():
        return {
            "nr_bloc": input("Adauga numarul apartamentului: "),
            "nume_proprietar": input("Adauga numele proprietarului/chiriasului: "),
            "etaj": input("La ce etaj se afla apartamentul?: "),
            "camere": input("Cate camere are apartamentul?: "),
            "nr_persoane": input("Cate persoane locuiesc in apartament?: "),
            "block_id": input("ID-ul blocului caruia ii apartine: ")      
        }

    @staticmethod
    def add_gas_invoice_menu():
        return {
            "cod_client": input("Introduceti codul de client: "),
            "nr_factura": input("Introduceti numarul facturii: "),
            "data_emitere": input("Data de emitere a facturii: "),
            "data_scadenta": input("Care este data scadenta a facturii?: "),
            "consum_kwh": input("Consumul de gase(in Kwh): "),
            "valoare_kwh": input("Valoarea in lei a unui Kwh de gase: "),
            "block_id": input("ID-ul blocului caruia ii apartine factura: ")      
        }

    @staticmethod
    def add_cold_water_invoice_menu():
        return {
            "cod_client": input("Introduceti codul de client: "),
            "nr_factura": input("Introduceti numarul facturii: "),
            "data_emitere": input("Data de emitere a facturii: "),
            "data_scadenta": input("Care este data scadenta a facturii?: "),
            "consum_m3": input("Consumul de apa(in metrii cubi): "),
            "valoare_m3": input("Valoarea in lei a unui metru cub de apa rece: "),
            "block_id": input("ID-ul blocului caruia ii apartine factura: ")      
        }

    @staticmethod
    def add_hot_water_invoice_menu():
        return {
            "cod_client": input("Introduceti codul de client: "),
            "nr_factura": input("Introduceti numarul facturii: "),
            "data_emitere": input("Data de emitere a facturii: "),
            "data_scadenta": input("Care este data scadenta a facturii?: "),
            "consum_m3": input("Consumul de apa(in metrii cubi): "),
            "valoare_m3": input("Valoarea in lei a unui metru cub de apa calda: "),
            "block_id": input("ID-ul blocului caruia ii apartine factura: ")      
        }
    
    @staticmethod
    def add_individual_meter_water_menu():
        return {
            "luna": input("Luna pentru care se adauga index-ul: "),
            "anul": input("Anul pentru caruia ii apartine index-ul: "),
            "index_apa_rece": input("Introduceti consumul de apa rece(in metrii cubi): "),
            "index_apa_calda": input("Introduceti consumul de apa calda(in metrii cubi): "),
            "nr_apartament": input("Nr-ul apartamentului pentru care se introduc index-urile: "),
            "block_id": input("ID-ul blocului din care apartine apartamentul: ")      
        }


class DataBase:
    
    def __init__(self, connection):
        try:
            self.conn = sqlite3.connect(connection)
        except sqlite3.Error as err:
            logging.critical(err)
            sys.exit(1)
   
    def block_of_flats(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS block_of_flats(
            block_id INTEGER PRIMARY KEY,
            nr_bloc TEXT NOT NULL,
            scari INTEGER NOT NULL,
            etaje INTEGER NOT NULL,
            apartamente INTEGER NOT NULL,
            adresa TEXT NOT NULL)
        """)
    
        self.conn.commit()

    def flat(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flat(
            flat_id INTEGER PRIMARY KEY,
            nr_apartament TEXT NOT NULL,
            nume_proprietar TEXT NOT NULL,
            etaj INTEGER NOT NULL,
            camere INTEGER NOT NULL,
            nr_persoane INTEGER NOT NULL,         
            block_id INTEGER NOT NULL,
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()

    def gas_invoice(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gas_invoice(
            id INTEGER PRIMARY KEY,
            cod_client TEXT NOT NULL,
            nr_factura TEXT NOT NULL,
            data_emitere DATA NOT NULL,
            data_scadenta DATA NOT NULL,
            consum_kwh REAL NOT NULL,
            valoare_kwh REAL NOT NULL,            
            valoarea_totala REAL NOT NULL,            
            block_id INTEGER NOT NULL,            
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()

    def cold_water_invoice(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cold_water_invoice(
            id INTEGER PRIMARY KEY,
            cod_client TEXT NOT NULL,
            nr_factura TEXT NOT NULL,
            data_emitere DATA NOT NULL,
            data_scadenta DATA NOT NULL,
            consum_m3 REAL NOT NULL,
            valoare_m3 REAL NOT NULL,            
            valoarea_totala REAL NOT NULL,            
            block_id INTEGER NOT NULL,            
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()
    
    def hot_water_invoice(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hot_water_invoice(
            id INTEGER PRIMARY KEY,
            cod_client TEXT NOT NULL,
            nr_factura TEXT NOT NULL,
            data_emitere DATA NOT NULL,
            data_scadenta DATA NOT NULL,
            consum_m3 REAL NOT NULL,
            valoare_m3 REAL NOT NULL,            
            valoarea_totala REAL NOT NULL,           
            block_id INTEGER NOT NULL,            
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()

    def individual_meter_water(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS individual_meter_cold_water(
            id INTEGER PRIMARY KEY,
            luna INTEGER NOT NULL,
            anul INTEGER NOT NULL,
            index_apa_rece REAL NOT NULL,
            index_apa_calda REAL NOT NULL,            
            nr_apartament TEXT NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (nr_apartament) REFERENCES flat(nr_apartament),
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()
   
    def add_block_of_flats(self, block_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO block_of_flats(nr_bloc, scari, etaje, apartamente, adresa)
        VALUES
        (?, ?, ?, ?, ?)
        """, (block_data["nr_bloc"], block_data["scari"], block_data["etaje"], block_data["apartamente"], block_data["adresa"]))
        
        self.conn.commit()


    def add_flats(self, flats_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO block_of_flats(nr_apartament, nume_proprietar, etaj, camere, nr_persoane, block_id)
        VALUES(?, ?, ?, ?, ?, ?)
        """, (flats_data["nr_apartament"], flats_data["nume_proprietar"], flats_data["etaj"], flats_data["camere"], 
        flats_data["nr_persoane"], flats_data["block_id"]))
        
        self.conn.commit()

    def add_gas_invoice(self, gas_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO gas_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_kwh, valoare_kwh, valoarea_totala, block_id)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, (gas_data["cod_client"], gas_data["nr_factura"], gas_data["data_emitere"], gas_data["data_scadenta"], 
        gas_data["consum_kwh"], gas_data["valoare_kwh"], gas_data(["consum_kwh"] * ["valoare_kwh"]), gas_data["block_id"]))
        
        self.conn.commit()

    def add_cold_water_invoice(self, cold_water_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO cold_water_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, valoarea_totala, block_id)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, (cold_water_data["cod_client"], cold_water_data["nr_factura"], cold_water_data["data_emitere"], cold_water_data["data_scadenta"], 
        cold_water_data["consum_m3"], cold_water_data["valoare_m3"], cold_water_data(["consum_m3"] * ["valoare_m3"]), cold_water_data["block_id"]))
        
        self.conn.commit()

    def add_hot_water_invoice(self, hot_water_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO hot_water_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, valoarea_totala, block_id)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, (hot_water_data["cod_client"], hot_water_data["nr_factura"], hot_water_data["data_emitere"], hot_water_data["data_scadenta"], 
        hot_water_data["consum_m3"], hot_water_data["valoare_m3"], hot_water_data(["consum_m3"] * ["valoare_m3"]), hot_water_data["block_id"]))
        
        self.conn.commit()

    def add_individual_meter_water(self, individual_meter_data):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO individual_meter_cold_water(luna, anul, index_apa_rece, index_apa_calda, nr_apartament, block_id)
        VALUES(?, ?, ?, ?, ?, ?)
        """, (individual_meter_data["luna"], individual_meter_data["anul"], individual_meter_data["index_apa_rece"], 
        individual_meter_data["index_apa_calda"], individual_meter_data["nr_apartament"], individual_meter_data["block_id"]))
        
        self.conn.commit()

    def close_database(self):
        self.conn.close()

class BlockFlats:

    def __init__(self, blockflats_data):
        self.__nr_bloc = blockflats_data["nr_bloc"]
        self.__scari = blockflats_data["scari"]
        self.__etaje = blockflats_data["etaje"]
        self.__apartamente = blockflats_data["apartamente"]
        self.__adresa = blockflats_data["adresa"]

class Suite:

    def __init__(self, suite_data):
        self.__nr_apartament = suite_data["nr_apartament"]
        self.__nume_proprietar = suite_data["nume_proprietar"]
        self.__etaj = suite_data["etaj"]
        self.__camere = suite_data["camere"]
        self.__nr_persoane = suite_data["nr_persoane"]
        self.__block_id = suite_data["block_id"]


try:
    make_table = DataBase(DB_FILE)

    make_table.block_of_flats()
    make_table.flat()
    make_table.gas_invoice()
    make_table.cold_water_invoice()
    make_table.hot_water_invoice()
    make_table.individual_meter_water()
except (sqlite3.Error, TypeError) as err:
     logging.critical(err)
else:
    try:
        block_input = Menu.add_block_of_flats_menu()
        block1 = BlockFlats(block_input)
        make_table.add_block_of_flats(block_input)

        suite_input = Menu.add_flat_menu()
        flat1 = Suite(suite_input)
        make_table.add_flats(suite_input)
    except sqlite3.Error as err:
        logging.error(err)



"""
#     try:
#         block_input = Menu.add_block_of_flats_menu()
#         flat_input = Menu.add_flat_menu()
#         gas_invoice_input = Menu.add_gas_invoice_menu()
#         cold_water_invoice_input = Menu.add_cold_water_invoice_menu()
#         hot_water_invoice_input = Menu.add_hot_water_invoice_menu()
#         individual_meter_input = Menu.add_individual_meter_water_menu()

#         make_table.add_block_of_flats(block_input)
#         # make_table.add_flats(flat_input)
#         # make_table.add_gas_invoice(gas_invoice_input)
#         # make_table.add_cold_water_invoice(cold_water_invoice_input)
#         # make_table.add_hot_water_invoice(hot_water_invoice_input)
#         # make_table.add_individual_meter_water(individual_meter_input)
#     except sqlite3.Error as err:
#         logging.error(err)
"""
