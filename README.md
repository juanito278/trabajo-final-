CREATE DATABASE cursoPython;

USE cursoPython;

CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(50),
    direccion VARCHAR(200),
    fecha DATETIME
);
