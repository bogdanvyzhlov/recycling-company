DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS materials;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS collections;

CREATE TABLE roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL UNIQUE
);

CREATE TABLE materials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  phone TEXT NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  registration INTEGER DEFAULT CURRENT_TIMESTAMP,
  activation INTEGER,
  activated INTEGER DEFAULT 0,
  roles_id INTEGER NOT NULL,
  FOREIGN KEY (roles_id) REFERENCES roles (id)
);

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  main INTEGER DEFAULT 0 NOT NULL,
  street TEXT NOT NULL,
  city TEXT NOT NULL,
  postalcode INTEGER NOT NULL,
  users_id INTEGER NOT NULL,
  FOREIGN KEY (users_id) REFERENCES users (id)
);

CREATE TABLE prices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  price REAL NOT NULL,
  added INTEGER DEFAULT CURRENT_TIMESTAMP NOT NULL,
  materials_id INTEGER NOT NULL,
  FOREIGN KEY (materials_id) REFERENCES materials (id)
);

CREATE TABLE collections (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  weight REAL NOT NULL,
  received INTEGER CURRENT_TIMESTAMP NOT NULL,
  description TEXT,
  users_id INTEGER NOT NULL,
  materials_id INTEGER NOT NULL,
  FOREIGN KEY (users_id) REFERENCES users (id),
  FOREIGN KEY (materials_id) REFERENCES materials (id)
);

-------- Insert initial data
INSERT INTO roles (title) VALUES ('default');
INSERT INTO roles (title) VALUES ('employee');
INSERT INTO roles (title) VALUES ('admin');




INSERT INTO materials (name) VALUES ('Železo');
INSERT INTO materials (name) VALUES ('Ocel');
INSERT INTO materials (name) VALUES ('Hliník');
INSERT INTO materials (name) VALUES ('Měď');
INSERT INTO materials (name) VALUES ('Mosaz');
INSERT INTO materials (name) VALUES ('Stříbro');
INSERT INTO materials (name) VALUES ('Zlato');
INSERT INTO materials (name) VALUES ('Platina');




INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('282367de@seznam45164.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125243', 'Anna', 'Novotná', '2022-10-01 11:34:01', '2022-10-02 11:34:01', 1, 3);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('09e8b2c1@seznam14441.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126251', 'Aleš', 'Nový', '2022-10-03 09:22:12', '2022-10-04 09:22:12', 1, 2);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('b7db49a4@seznam8641.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125242', 'Boris', 'Starý', '2022-10-05 14:29:32', '2022-10-06 14:29:32', 1, 2);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('570b615b@seznam44866.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126252', 'Berta', 'Mladá', '2022-11-02 05:11:46', '2022-11-03 05:11:46', 1, 1);
INSERT INTO users (email, password, phone, firstname, lastname, registration, roles_id) VALUES ('bf41c779@seznam7942.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125241', 'Karel', 'Dlouhý', '2022-11-04 08:02:05', 1);
INSERT INTO users (email, password, phone, firstname, lastname, registration, roles_id) VALUES ('5ca935a9@seznam21476.cz', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126253', 'Klára', 'Prokopová', '2022-01-06 12:44:09', 1); 



INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Adamcova 23', 'Brno', 62378, 1);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Dlouhá 31', 'Praha', 62007, 2);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Husova 32', 'Liberec', 62252, 3);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Smetanova 37', 'Třinec', 62035, 4);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (0, 'Aloise Havla 45', 'Brno', 62833, 5);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (0, 'Bakalovo nábřeží 61', 'Brno', 62730, 6);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Bohatcova 15', 'Brno', 62514, 1);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Celní 21', 'Brno', 62953, 5);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Divišova 54', 'Brno', 62228, 3);




INSERT INTO prices (price, added, materials_id) VALUES ('317', '2022-09-01 08:10:00', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('481', '2022-09-01 08:10:00', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('6', '2022-09-01 08:10:00', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('297', '2022-09-01 08:10:00', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('349', '2022-09-01 08:10:00', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('290', '2022-09-01 08:10:00', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('336', '2022-09-01 08:10:00', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('494', '2022-09-01 08:10:00', 8);
INSERT INTO prices (price, added, materials_id) VALUES ('233', '2022-09-19 08:10:00', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('84', '2022-09-19 08:10:00', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('577', '2022-09-19 08:10:00', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('278', '2022-09-19 08:10:00', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('347', '2022-09-19 08:10:00', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('318', '2022-09-19 08:10:00', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('96', '2022-09-19 08:10:00', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('380', '2022-09-19 08:10:00', 8);
INSERT INTO prices (price, added, materials_id) VALUES ('219', '2022-10-07 08:10:00', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('103', '2022-10-07 08:10:00', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('526', '2022-10-07 08:10:00', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('263', '2022-10-07 08:10:00', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('233', '2022-10-07 08:10:00', 8);
INSERT INTO prices (price, added, materials_id) VALUES ('184', '2022-10-12 09:10:00', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('544', '2022-10-12 09:10:00', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('494', '2022-10-12 09:10:00', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('403', '2022-10-12 09:10:00', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('112', '2022-10-12 09:10:00', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('608', '2022-10-12 09:10:00', 8);
INSERT INTO prices (price, added, materials_id) VALUES ('322', '2022-11-15 08:10:00', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('287', '2022-11-15 08:10:00', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('251', '2022-11-15 08:10:00', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('616', '2022-11-15 08:10:00', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('632', '2022-11-15 08:10:00', 8);
INSERT INTO prices (price, added, materials_id) VALUES ('574', '2022-11-20 08:10:00', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('333', '2022-11-20 08:10:00', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('431', '2022-11-20 08:10:00', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('593', '2022-11-20 08:10:00', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('113', '2022-11-20 08:10:00', 8);




INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('7.23', '2022-09-05 12:07:32', '4', '4');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('62.35', '2022-09-05 10:09:10', '5', '3');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('41.53', '2022-09-05 11:42:58', '5', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('64.28', '2022-09-05 10:30:52', '2', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('15.19', '2022-09-05 07:37:58', '3', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('27.26', '2022-09-05 13:32:46', '3', '1');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('18.1', '2022-09-05 10:02:36', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('23.56', '2022-09-05 13:41:33', '5', '7');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('32.65', '2022-09-20 16:35:19', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('13.61', '2022-09-19 18:21:49', '4', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('61.15', '2022-09-19 21:14:23', '2', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('46.5', '2022-09-20 16:11:24', '3', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('54.11', '2022-09-20 03:42:00', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('49.47', '2022-10-09 00:02:28', '4', '4');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('5.57', '2022-10-08 20:01:53', '3', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('9.55', '2022-10-08 20:11:04', '3', '3');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('43.9', '2022-10-09 01:53:03', '2', '2');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('4.34', '2022-10-15 09:50:11', '5', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('14.60', '2022-10-15 06:13:00', '4', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('25.26', '2022-10-15 13:27:06', 'Popis ed33ee55-6fce-5b3b-aa28-6fbebdb317be', '4', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('34.24', '2022-10-15 08:07:42', 'Popis 549c3362-3eb9-504a-a284-c70d492d9145', '3', '3');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('1.55', '2022-10-15 20:12:23', 'Popis 7741eeab-95a5-507a-9c54-751ca186fefb', '3', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('51.31', '2022-11-18 16:47:12', 'Popis 92d97c40-5213-5652-806e-378949b2253a', '6', '7');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('16.25', '2022-11-18 17:55:12', 'Popis bf824ec3-59f5-5650-a421-c5369709ac1f', '3', '7');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('51.24', '2022-11-18 10:25:41', 'Popis cd22dedf-a6f1-5658-8ed4-4ce452ab90e0', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('28.11', '2022-11-18 03:54:55', 'Popis cd3ff6f0-ce9d-5bd6-8dea-d3d2df17d3b3', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('33.34', '2022-11-18 00:07:11', 'Popis 37eac29a-0471-54a2-9d48-e421dfba992d', '2', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('60.42', '2022-11-17 22:32:58', 'Popis 47262876-e576-596c-82cc-008861160e32', '3', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('13.29', '2022-11-17 22:17:59', 'Popis 1735bbae-2b41-5c3c-89fa-d65a93026b68', '4', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('62.25', '2022-11-18 00:28:14', 'Popis 9c0eab2d-50a0-5701-8d33-db21f693cdc1', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('34.16', '2022-11-23 04:27:54', 'Popis 06f89af5-e6e0-5cc7-9e75-3b7657c85ead', '2', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('47.53', '2022-11-23 05:50:50', 'Popis 767b5567-4eb5-5e6e-b947-d1baaa180ea2', '2', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('58.1', '2022-11-22 20:27:31', 'Popis 231dc65f-1533-5030-9bf6-ca93cf7c095e', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('14.31', '2022-11-22 11:30:50', 'Popis fa08332e-3b60-5a81-8f01-3f76af8a3eda', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('61.60', '2022-11-22 15:03:18', 'Popis 528615f7-0caa-5606-b35e-0d308f9af05c', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('13.3', '2022-11-23 00:43:55', 'Popis f173389f-5f64-5173-9082-3b509e5b1c4b', '3', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('36.3', '2022-11-22 09:47:37', 'Popis 7e2c50cb-b95b-5cb1-a7a0-a9f95000935f', '4', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('4.53', '2022-11-22 21:13:23', 'Popis 3ee50e11-59cb-5a1b-a9a3-8c3ee59755c7', '6', '3');