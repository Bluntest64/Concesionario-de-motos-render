-- ============================================================
--  Concesionario de Motocicletas de Alta Gama
--  Script de base de datos
-- ============================================================

CREATE DATABASE IF NOT EXISTS concesionario_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE concesionario_db;

-- Tabla vehiculos
CREATE TABLE IF NOT EXISTS vehiculos (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    marca       VARCHAR(100) NOT NULL,
    modelo      VARCHAR(100) NOT NULL,
    precio      DECIMAL(12, 2) NOT NULL,
    cilindraje  INT NOT NULL,
    color       VARCHAR(50),
    anio        INT,
    estado      ENUM('disponible', 'vendido') DEFAULT 'disponible',
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(150) NOT NULL,
    documento   VARCHAR(30) NOT NULL UNIQUE,
    telefono    VARCHAR(20),
    email       VARCHAR(120),
    direccion   VARCHAR(200),
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla ventas
CREATE TABLE IF NOT EXISTS ventas (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente   INT NOT NULL,
    id_vehiculo  INT NOT NULL,
    fecha_venta  DATE NOT NULL,
    valor        DECIMAL(12, 2) NOT NULL,
    observacion  TEXT,
    FOREIGN KEY (id_cliente)  REFERENCES clientes(id)  ON DELETE RESTRICT,
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id) ON DELETE RESTRICT
);

-- Datos de ejemplo
INSERT INTO vehiculos (marca, modelo, precio, cilindraje, color, anio, estado) VALUES
('Ducati',      'Panigale V4',  85000000, 1103, 'Rojo',    2024, 'disponible'),
('BMW',         'S1000RR',      75000000, 999,  'Blanco',  2024, 'disponible'),
('Kawasaki',    'Ninja H2R',    95000000, 998,  'Negro',   2023, 'disponible'),
('Honda',       'CBR1000RR-R',  70000000, 999,  'Rojo',    2023, 'vendido'),
('Yamaha',      'YZF-R1M',      65000000, 998,  'Azul',    2024, 'disponible');

INSERT INTO clientes (nombre, documento, telefono, email, direccion) VALUES
('Carlos Mendoza',  '1020304050', '3101234567', 'carlos@email.com', 'Calle 50 #20-30, Bogotá'),
('Laura Gómez',     '1030405060', '3157654321', 'laura@email.com',  'Carrera 15 #80-10, Medellín'),
('Andrés Torres',   '1040506070', '3209876543', 'andres@email.com', 'Av. 68 #5-20, Bogotá');

INSERT INTO ventas (id_cliente, id_vehiculo, fecha_venta, valor, observacion) VALUES
(1, 4, '2024-11-15', 70000000, 'Pago de contado');
