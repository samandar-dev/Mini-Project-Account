# ----------------------------Account-----------------------------

import mysql.connector
import os

my_db = mysql.connector.connect(
      host="localhost",
      user="Samandar",
      passwd="samandar",
      database="Jadval"
)

mycursor = my_db.cursor()

class Account:
      def registration(self):
            fam = input("\n\tFamilya: >>>>> ").strip().capitalize()
            while not fam.isalpha():
                  fam = input("Xato kiritingiz qayta kiriting: >>").strip().capitalize()

            ism = input("\tIsm kiriting: >>>>").strip().capitalize()
            while not fam.isalpha():
                  ism = input("Xato kiritingiz qayta kiriting: >>").strip().capitalize()

            yosh = input("\tYoshni kiriting: >>>>").strip()
            if len(yosh) >= 4:
                  print("Bunday yoshdagi odam yoq qayta kiriting: ")
                  yosh = input("\tYoshni kiriting: >>>>").strip()

            while not yosh.isnumeric():
                  yosh = input("Xato son kiriting: >>>").strip()

            login = input("\tLogin kiriting: >>>>").strip()
            while not login.isalpha() and not login.isalnum():
                  login = input("Xato boshqa login kiriting: >>>").strip()

            password_ = input("\tPassword kiriting: >>>").strip()

            pass_account = f" select password from Account where password='{password_}'"
            mycursor.execute(pass_account)
            pass_account__ = mycursor.fetchall()

            while pass_account__:
                  print("Bunday password bor boshqa kiriting: ")
                  password_ = input("\tPassword kiriting: >>>").strip()

                  pass_account = f" select password from Account where password='{password_}'"
                  mycursor.execute(pass_account)
                  pass_account__ = mycursor.fetchall()

            if not password_ not in pass_account:
                  mycursor.execute(f"insert into Account (fam, ism, yosh, login, password) values "
                  f"('{fam}', '{ism}', {yosh}, '{login}', '{password_}')")
                  my_db.commit()

                  self.clear()
                  print("\n\tYangi account qoshildi")
                  self.Tanlov()

      def log_in(self):
            print("\n\tAccountga kirish uchun login password kiriting:")
            login = input("\nLoginni kiriting: >>>>").strip()
            password = input("Passwordni kiriting: >>>>").strip()

            login_tek = f"select login from Account where login='{login}'"
            mycursor.execute(login_tek)
            login_tek = mycursor.fetchall()

            password_tek = f"select password from Account where password='{password}'"
            mycursor.execute(password_tek)
            password_tek = mycursor.fetchall()

            sanoq = 2
            while not login_tek or not password_tek:
                  sanoq -= 1
                  print("\n\tBunday Account yo'q qayta kiriting: ")
                  login = input("Loginni kiriting: >>>>").strip()
                  password = input("Passwordni kiriting: >>>>").strip()

                  login_tek = f"select login from Account where login='{login}'"
                  mycursor.execute(login_tek)
                  login_tek = mycursor.fetchall()

                  password_tek = f"select password from Account where password='{password}'"
                  mycursor.execute(password_tek)
                  password_tek = mycursor.fetchall()

                  if login_tek and password_tek:
                        account = f"select * from Account where password='{password}'"
                        mycursor.execute(account)
                        account__ = mycursor.fetchall()

                        for i in account__:
                              self.clear()

                              print(f"""
                              ____________________________________________________________
                              | id |   fam   |   ism   | yosh |   login   |   password   |
                              |----|---------|---------|------|-----------|--------------|

                  \t\t{i}\n""")

                              self.pri()

                  if sanoq == 0:
                        self.clear()
                        print("\n\t\tBunday login password lar yoq??????")
                        self.Tanlov()

            if login_tek and password_tek:
                  account = f"select * from Account where password='{password}'"
                  mycursor.execute(account)
                  account__ = mycursor.fetchall()

                  for i in account__:
                        self.clear()

                        print(f"""
                        ____________________________________________________________
                        | id |   fam   |   ism   | yosh |   login   |   password   |
                        |----|---------|---------|------|-----------|--------------|

            \t\t{i}\n""")

                        self.pri()

      def update_login(self):
            print("Eski loginni kiriting: ")
            login = input("Kiriting: >> ").strip()

            login_tek = f"select login from Account where login='{login}'"
            mycursor.execute(login_tek)
            login_tek = mycursor.fetchall()

            print("Loginni ozgartirish:")

            new_login = input("Kiriting: >>>").strip()
            while not new_login.isalpha() and not new_login.isalnum():
                  new_login = input("Xato boshqa login kiriting: >>>").strip()

            for i in login_tek:
                  self.clear()
                  print(f"\n\tlogin ->> {i}")

            new_login_ = mycursor.execute(f"update Account set login='{new_login}' where login='{login}'")
            my_db.commit()

            new_login_ = f"select login from Account where login='{new_login}'"
            mycursor.execute(new_login_)
            new_login_ = mycursor.fetchall()

            print("\tLogin ozgartirilldi:")

            for i in new_login_:
                  print(f"\tnew_login ->> {i}\n")
                  self.pri()

      def update_password(self):
            print("Eski password kiriting: ")
            password = input("Kiriting: >> ").strip()

            password_tek = f"select password from Account where password='{password}'"
            mycursor.execute(password_tek)
            password_tek = mycursor.fetchall()

            print("Password ozgartirish:")
            new_password = input("Kiriting: >>>").strip()

            for i in password_tek:
                  self.clear()
                  print(f"\n\tPassword ->> {i}")

            new_password_ = mycursor.execute(f"update Account set password='{new_password}' where password='{password}'")
            my_db.commit()

            new_password_ = f"select password from Account where password='{new_password}'"
            mycursor.execute(new_password_)
            new_password_ = mycursor.fetchall()

            print("\tPassword ozgartirilldi:")

            for i in new_password_:
                  print(f"\tnew_password ->> {i}\n")
                  self.pri()

      def log_out(self):
            self.clear()
            self.Tanlov()

      def delete_account(self):
            print("\n\tDelete account qilish uchun password ni kiriting: ")
            password_ = input("password >>>").strip()

            account = f"select * from Account where password='{password_}'"
            mycursor.execute(account)
            account = mycursor.fetchall()

            sanoq = 3
            while not account:
                  sanoq -= 1
                  print("Bunday password yoq qayta urinip korin: ")
                  password_ = input("password >>>").strip()

                  account = f"select * from Account where password='{password_}'"
                  mycursor.execute(account)
                  account = mycursor.fetchall()

                  if sanoq == 0:
                        print("Keginroq harakat qilipkorin:")
                        self.clear()
                        self.Tanlov()

            if account:
                  delete_account = f"delete from Account where password='{password_}'"
                  mycursor.execute(delete_account)
                  my_db.commit()

                  self.clear()
                  print("\n\tAccount ochirildi:")
                  self.Tanlov()

      def Tanlov(self):
            son = ['1', '2']
            print(f"""
                 __________________
                 |1. Registratsia |
                 |----------------|
                 |2. Login        |
                 |----------------|
                  """)

            n = input(">>>>>>").strip()
            while n not in son:
                  n = input("Xato kiritingiz: ").strip()

            if n == son[0]:
                  self.clear()
                  self.registration()
            else:
                  self.clear()
                  self.log_in()

      def pri(self):
            sonlar = ['1', '2', '3', '4', '5']
            print(f"""
                  1. update_login
                  2. update_password
                  3. log_out
                  4. delete_account
                  5. Exit
                  """)

            n = input(">>>>").strip()
            while n not in sonlar:
                  n = input(">>>>").strip()

            if n == sonlar[0]:
                  self.clear()
                  self.update_login()
            elif n == sonlar[1]:
                  self.clear()
                  self.update_password()
            elif n == sonlar[2]:
                  self.clear()
                  self.log_out()
            elif n == sonlar[3]:
                  self.clear()
                  self.delete_account()
            else:
                  print("----------------Xayr-----------")
                  exit()

      def clear(self):
            return os.system("clear")


foy = Account()
foy.Tanlov()
