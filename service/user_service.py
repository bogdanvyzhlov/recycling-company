import hashlib
from database.database import get_db
import config

class UserService():
    @staticmethod
    def verify(email, password):
        db = get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.activated,
                roles.title
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE email = ? AND password = ?
        ''', [email, hash.hexdigest()]).fetchone()
        if result:
            return result
        else:
            return None

    @staticmethod
    def register(email, password, phone, firstname, lastname):
        db = get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())
        try:
            result = db.execute('''
                INSERT INTO users (email, password, phone, firstname, lastname, roles_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', [email, hash.hexdigest(), phone, firstname, lastname, config.DEFAULT_ROLE_ID])
            db.commit()
            return result.lastrowid
        except Exception:
            #if new account is created, return user id (inserted id), else return -1
            return -1


    @staticmethod
    def update_user(email, password, phone, id):
        db= get_db()
        hash = hashlib.sha256(f'{password}{config.PASSWORD_SALT}'.encode())

        db.execute('''
                    UPDATE users
                    SET
                    email= ?,
                    password= ?,
                    phone= ?
                    where users.id = ?
        ''', [email, hash.hexdigest(), phone, id])
        db.commit()


    @staticmethod
    def update_address_main(street, city, postalcode, id):
        db=get_db()
        main=1
        db.execute('''
                DELETE FROM addresses
                WHERE users_id= ? AND main = 1
         ''', [id])
        db.commit()
        db.execute('''
                      INSERT INTO addresses (main,street,city,postalcode, users_id)
                      VALUES(?,?,?,?,?)
                   ''', [main, street, city, postalcode, id])
        db.commit()





    @staticmethod
    def update_address(street, city, postalcode, id):
        db = get_db()
        main = 0
        db.execute('''
                        DELETE FROM addresses
                        WHERE users_id= ? AND main = 0
                 ''', [id])
        db.commit()
        db.execute('''
                              INSERT INTO addresses (main,street,city,postalcode, users_id)
                              VALUES(?,?,?,?,?)
                           ''', [main, street, city, postalcode, id])
        db.commit()

    @staticmethod
    def get_user(id):
        db=get_db()
        result = db.execute('''
                                    SELECT 
                                     users.firstname, 
                                     users.lastname, 
                                     users.email, 
                                     users.phone,
                                     users.activated
                                    FROM users
                                    where users.id = ?
                                ''', [id]).fetchone()
        if result:
            return result
        else:
            return None

    @staticmethod
    def get_addresses_by_user_main(id):
        db = get_db()

        result = db.execute('''
                                        SELECT 
                                         addresses.street, 
                                         addresses.city, 
                                         addresses.postalcode, 
                                         addresses.main
                                        FROM addresses
                                        where addresses.users_id = ? and addresses.main=1
                                    ''', [id]).fetchall()
        if result:
            return result
        else:
            return None

    @staticmethod
    def get_addresses_by_user(id):
        db = get_db()

        result = db.execute('''
                                          SELECT 
                                           addresses.street, 
                                           addresses.city, 
                                           addresses.postalcode, 
                                           addresses.main
                                          FROM addresses
                                          where addresses.users_id = ? and addresses.main=0
                                      ''', [id]).fetchall()
        if result:
            return result
        else:
            return None

    @staticmethod
    def get_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.registration,
                users.activation,
                users.activated,
                users.roles_id,
                roles.title,
                IIF(activated == 1, 'Approved', 'Waiting') as state
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
        ''').fetchall()
        return result

    @staticmethod
    def get_activated_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.registration,
                users.activation,
                users.activated,
                users.roles_id,
                roles.title
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE activated = 1
        ''').fetchall()
        return result
    
    @staticmethod
    def get_unactivated_users():
        db = get_db()
        result = db.execute('''
            SELECT
                users.id,
                users.email,
                users.phone,
                users.firstname,
                users.lastname,
                users.registration,
                users.activation,
                users.activated,
                users.roles_id,
                roles.title,
                IIF(activated == 1, 'Approved', 'Waiting') as state
            FROM users
                INNER JOIN roles ON roles.id = users.roles_id
            WHERE activated = 0 and roles_id = 1
        ''').fetchall()
        return result
    
    @staticmethod
    def activate_user(user_id):
        db = get_db()
        try:
            db.execute('''
                UPDATE users
                SET
                    activation = CURRENT_TIMESTAMP,
                    activated = 1
                WHERE id = ?
            ''', [user_id])
            db.commit()
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_roles():
        db = get_db()
        result = db.execute('''
            SELECT
                roles.id,
                roles.title
            FROM roles
        ''').fetchall()
        return result
    
    @staticmethod
    def set_user_role(user_id, role_id):
        db = get_db()
        try:
            db.execute('''
                UPDATE users
                SET roles_id = ?
                WHERE id = ?
            ''', [role_id, user_id])
            db.commit()
            return True
        except Exception:
            return False
    
    @staticmethod
    def delete_user(user_id):
        db = get_db()
        try:
            db.execute('''
                DELETE FROM users
                WHERE id = ?
            ''', [user_id])
            db.commit()
            return True
        except Exception:
            return False

    @staticmethod
    def get_user_id(email):
        db = get_db()
        result = db.execute('''
            SELECT id FROM users WHERE email = ?
            ''', [email]).fetchone()
        if result is None:
            return -1
        return result['id']
