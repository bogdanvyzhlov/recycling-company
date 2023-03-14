from database.database import get_db

class CollectionsService():
    @staticmethod
    def register_collection(weight, description, users_id, materials_id):
      db = get_db()
      try:
          result = db.execute('''
              INSERT INTO collections (weight, description, users_id, materials_id, received)
              VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
          ''', [weight, description, users_id, materials_id])
          db.commit()
          return result.lastrowid
      except Exception:
          #if collection is received, return collection id (inserted id), else return -1
          return -1

    @staticmethod
    def get_collections():
      db = get_db()
      return db.execute('''
        SELECT cid, users_id, weight, price as pricePerUnit, (weight*price) as total_price, received, added, materials_id, name, pid FROM (
          SELECT DENSE_RANK() OVER (PARTITION BY cid ORDER BY (JULIANDAY(received)-JULIANDAY(added))) as rank, (JULIANDAY(received)-JULIANDAY(added)) as datediff, * FROM (
            SELECT
                c.id as cid, c.weight, c.received, c.users_id, c.materials_id, m.name, p.id as pid, p.price, p.added
            FROM collections as c
            INNER JOIN materials as m
                on m.id = c.materials_id
            INNER JOIN prices as p
                ON p.materials_id = c.materials_id AND p.added <= c.received
          ) as t1 order by cid, rank
        ) as t2 WHERE rank = 1
      ''').fetchall()

    @staticmethod
    def get_collections_by_user(user_id):
      db = get_db()
      return db.execute('''
        SELECT cid, users_id, weight, price as pricePerUnit, (weight*price) as total_price, received, added, materials_id, name, pid FROM (
          SELECT DENSE_RANK() OVER (PARTITION BY cid ORDER BY (JULIANDAY(received)-JULIANDAY(added))) as rank, (JULIANDAY(received)-JULIANDAY(added)) as datediff, * FROM (
            SELECT
                c.id as cid, c.weight, c.received, c.users_id, c.materials_id, m.name, p.id as pid, p.price, p.added
            FROM collections as c
            INNER JOIN materials as m
                on m.id = c.materials_id
            INNER JOIN prices as p
                ON p.materials_id = c.materials_id AND p.added <= c.received
          ) as t1 order by cid, rank
        ) as t2 WHERE rank = 1 AND users_id = ?
      ''', [user_id]).fetchall()

    @staticmethod
    def get_all_collections():
        db = get_db()
        return db.execute('''
               SELECT c.id as id_col, u.email as email, m.name as material,
                    c.weight as weight, c.received as received, c.description as description 
                FROM collections as c
               INNER JOIN materials as m 
                    ON m.id = c.materials_id
                INNER JOIN users as u 
                    ON u.id = c.users_id
                ORDER BY c.id DESC
             ''').fetchall()

    @staticmethod
    def get_total_price_by_user_actual_month(user_id):
        db = get_db()
        return db.execute('''
           SELECT cid, users_id, round(sum(weight*price),2) as total_price, received, strftime('%m.%Y',received) as curr_month, added, materials_id, name, pid FROM (
             SELECT DENSE_RANK() OVER (PARTITION BY cid ORDER BY (JULIANDAY(received)-JULIANDAY(added))) as rank, (JULIANDAY(received)-JULIANDAY(added)) as datediff, * FROM (
               SELECT
                   c.id as cid, c.weight, c.received, c.users_id, c.materials_id, m.name, p.id as pid, p.price, p.added
               FROM collections as c
               INNER JOIN materials as m
                   on m.id = c.materials_id
               INNER JOIN prices as p
                   ON p.materials_id = c.materials_id AND p.added <= c.received 
             ) as t1 order by cid, rank
           ) as t2 WHERE rank = 1 AND users_id = ? and strftime('%m', received) = strftime('%m', datetime('now')) and strftime('%Y', received) = strftime('%Y', datetime('now'))
         ''', [user_id]).fetchone()