CREATE DATABASE BBDD_equip2;
USE BBDD_equip2;

-- Crear tablas
CREATE TABLE ONG (
    CIF VARCHAR(9) PRIMARY KEY,
    nombre_ong VARCHAR(100),
    pais_ong VARCHAR(50)
);

CREATE TABLE ANIMALES (
    id_especie VARCHAR(9) PRIMARY KEY,
    nombre_animal VARCHAR(40) NOT NULL,
    estado ENUM('vulnerable', 'peligro', 'extinto'),
    nombre_especie VARCHAR(100),
    CIF_ong VARCHAR(9),
    FOREIGN KEY (CIF_ong) REFERENCES ONG(CIF) ON DELETE CASCADE
);


drop database BBDD_equip2;
SELECT * FROM ANIMALES;
SELECT * FROM ONG;
SELECT * FROM ONG_ANIMALES;


