import sqlite3

class SQLither:

    def __init__(self, database) -> object:
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        self.c.execute("""
CREATE TABLE IF NOT EXISTS "users" (
"user_id" INTEGER NOT NULL,
"first_name" TEXT NULL,
"last_name" TEXT NULL,
"username" TEXT NULL)
""")
        self.c.execute("""
CREATE TABLE IF NOT EXISTS "evacuator_data" (
"full_name_driver" TEXT NULL,
"license_car" TEXT NULL,
"phone_number" TEXT NULL)
""")
        self.c.execute("""
CREATE TABLE IF NOT EXISTS "payment_data" (
"photo" BLOB NOT NULL,
"wincode" TEXT NOT NULL)
""")

    def exists_user(self, user_id):
        return bool(self.c.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone())

    def add_to_db_users(self, user_id, first_name, last_name, username):
        self.c.execute("INSERT INTO users(user_id, first_name, last_name, username) VALUES(?,?,?,?)", (user_id, first_name, last_name, username))
        self.conn.commit()

    def exists_driver_data(self, full_name_driver):
        return bool(self.c.execute("SELECT * FROM evacuator_data WHERE full_name_driver=?", (full_name_driver,)).fetchone())

    def add_to_db_drivers(self, full_name_driver, license_car, phone_number):
        self.c.execute("INSERT INTO evacuator_data(full_name_driver, license_car, phone_number) VALUES(?,?,?)", (full_name_driver, license_car, phone_number))
        self.conn.commit()

    def exists_payment(self, wincode):
        return bool(self.c.execute("SELECT * FROM payment_data WHERE wincode=?", (wincode,)).fetchone())

    def add_to_db_payment(self, photo, wincode):
        self.c.execute("INSERT INTO payment_data(photo, wincode) VALUES(?,?)", (photo, wincode))
        self.conn.commit()