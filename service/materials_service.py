from database.database import get_db

class MaterialsService():
    @staticmethod
    def get_current_prices():
        db = get_db()
        return db.execute('''
        SELECT materials.id, materials.name, prices.price, prices.added FROM materials
	        INNER JOIN (SELECT materials_id, MAX(id) as pid FROM prices GROUP BY materials_id) as latest_prices ON latest_prices.materials_id = materials.id
          INNER JOIN prices ON prices.id = latest_prices.pid
        ''').fetchall()
    
    @staticmethod
    def get_stats():
        db = get_db()
        return db.execute('''
          SELECT materials_id, materials.name, MAX(received) as latest_received, AVG(weight) as average_weight, SUM(weight) as total_received, COUNT(*) as total_received_count
            FROM collections
            INNER JOIN materials ON materials.id = collections.materials_id
            GROUP BY materials_id
        ''').fetchall()
    
    @staticmethod
    def add_new_material(name, price):
        db = get_db()
        try:
            result = db.execute('''
                INSERT INTO materials (name)
                VALUES (?)
            ''', [name])
            db.commit()
            material_id = result.lastrowid
            db.execute('''
                INSERT INTO prices (materials_id, price, added)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', [material_id, price])
            db.commit()
            return material_id
        except Exception:
            return -1
    
    @staticmethod
    def update_name(material_id, name):
        db = get_db()
        try:
            db.execute('''
                UPDATE materials SET name = ? WHERE id = ?
            ''', [name, material_id])
            db.commit()
            return True
        except Exception:
            return False

    @staticmethod
    def update_price(material_id, price):
        db = get_db()
        try:
            db.execute('''
                INSERT INTO prices (materials_id, price, added)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', [material_id, price])
            db.commit()
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_material_name(material_id):
        db = get_db()
        result = db.execute('''
            SELECT name FROM materials WHERE id = ?
        ''', [material_id]).fetchone()
        if result is None:
            return None
        return result['name']

    @staticmethod
    def get_materials():
        db = get_db()
        return db.execute('''
              SELECT materials.id, 
                     materials.name  
                FROM materials
            ''').fetchall()
