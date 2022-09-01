import pathlib
import sqlite3
import logging
import sys


ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("db/intretinere_bloc.db")

# configure logger
logging.root.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s")

class DataBase:
    
    def __init__(self, connection):
        self.conn = sqlite3.connect(connection)

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
            index_apa REAL NOT NULL,
            index_apa_calda REAL NOT NULL,
            index_gaze REAL NOT NULL,
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
            consum_m3 REAL NOT NULL,
            valoare_m3 REAL NOT NULL,
            sold_precendent REAL NOT NULL,
            valoarea_totala REAL NOT NULL,
            flat_id INTEGER NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (flat_id) REFERENCES flat(flat_id),
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
            sold_precendent REAL NOT NULL,
            valoarea_totala REAL NOT NULL,
            flat_id INTEGER NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (flat_id) REFERENCES flat(flat_id),
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
            sold_precendent REAL NOT NULL,
            valoarea_totala REAL NOT NULL,
            flat_id INTEGER NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (flat_id) REFERENCES flat(flat_id),
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()

    def individual_meter_cold_water(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS individual_meter_cold_water(
            id INTEGER PRIMARY KEY,
            luna INTEGER NOT NULL,
            anul INTEGER NOT NULL,
            index_precedent REAL NOT NULL,
            index_curent REAL NOT NULL,
            consum_m3 REAL NOT NULL,
            flat_id INTEGER NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (flat_id) REFERENCES flat(flat_id),
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()

    def individual_meter_hot_water(self):
        if not isinstance(self.conn, sqlite3.Connection):
            raise TypeError("Not a DB connection object.")

        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS individual_meter_hot_water(
            id INTEGER PRIMARY KEY,
            luna INTEGER NOT NULL,
            anul INTEGER NOT NULL,
            index_precedent REAL NOT NULL,
            index_curent REAL NOT NULL,
            consum_m3 REAL NOT NULL,
            flat_id INTEGER NOT NULL,
            block_id INTEGER NOT NULL,
            FOREIGN KEY (flat_id) REFERENCES flat(flat_id),
            FOREIGN KEY (block_id) REFERENCES block_of_flats(block_id))
        """)
    
        self.conn.commit()
    
    def add_block_of_flats(self, nr_bloc, scari, etaje, apartamente, adresa):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO block_of_flats(nr_bloc, scari, etaje, apartamente, adresa)
        VALUES
        ('{}', '{}', '{}', '{}', '{}')
        """, (nr_bloc, scari, etaje, apartamente, adresa))
        
        self.conn.commit()


    def add_flats(self, nr_apartament, nume_proprietar, etaj, camere, nr_persoane, index_apa, index_apa_calda, index_gaze, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO block_of_flats(nr_apartament, nume_proprietar, etaj, camere, nr_persoane, index_apa, index_apa_calda, index_gaze, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (nr_apartament, nume_proprietar, etaj, camere, nr_persoane, index_apa, index_apa_calda, index_gaze, block_id))
        
        self.conn.commit()

    def add_gas_invoice(self, cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO gas_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id))
        
        self.conn.commit()

    def add_cold_water_invoice(self, cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO cold_water_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id))
        
        self.conn.commit()

    def add_hot_water_invoice(self, cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO hot_water_invoice(cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (cod_client, nr_factura, data_emitere, data_scadenta, consum_m3, valoare_m3, sold_precendent, valoarea_totala, flat_id, block_id))
        
        self.conn.commit()

    def add_individual_meter_cold_water(self, luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO individual_meter_cold_water(luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id))
        
        self.conn.commit()

    def add_individual_meter_hot_water(self, luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO individual_meter_hot_water(luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')""", (luna, anul, index_precedent, index_curent, consum_m3, flat_id, block_id))
        
        self.conn.commit()


    def close_database(self):
        self.conn.close()


try:
    make_table = DataBase(DB_FILE)

    make_table.block_of_flats()
    make_table.flat()
    make_table.gas_invoice()
    make_table.cold_water_invoice()
    make_table.hot_water_invoice()
    make_table.individual_meter_cold_water()
    make_table.individual_meter_hot_water()
except (sqlite3.Error, TypeError) as err:
    logging.critical(err)

