-- =========================================================
-- CRIAR BANCO DE DADOS
-- =========================================================

DROP DATABASE IF EXISTS restau_calabresa;
CREATE DATABASE restau_calabresa;

USE restau_calabresa;


-- =========================================================
-- FUNCIONÁRIOS
-- =========================================================

CREATE TABLE funcionarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50)
);

INSERT INTO funcionarios (nome)
VALUE ("Justin Bieber");

ALTER TABLE funcionarios
ADD COLUMN cargo VARCHAR(30);

ALTER TABLE funcionarios
ADD COLUMN data_nascimento DATE;

ALTER TABLE funcionarios
ADD COLUMN salario DOUBLE;

INSERT INTO funcionarios (nome, cargo, data_nascimento, salario)
VALUE ("Elias da Silva", "Caixa", "2000-07-12", 1996.50);

INSERT INTO funcionarios (nome, cargo, data_nascimento, salario)
VALUE ("Victor sem C", "Manobrista", "2012-09-29", 300.00);

INSERT INTO funcionarios (nome, cargo, data_nascimento, salario)
VALUE ("Peter Souza", "Cozinheiro Junior", "1995-02-28", 6795.30);


-- =========================================================
-- PRATOS FEITOS
-- =========================================================

CREATE TABLE pratos_feitos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    custo DOUBLE NOT NULL
);

INSERT INTO pratos_feitos (nome, custo)
VALUE ("X-Calabresa sem carne", 60.9);

INSERT INTO pratos_feitos (nome, custo)
VALUE ("Pizza de Calabresa de 10cm", 25);

INSERT INTO pratos_feitos (nome, custo) VALUES
("Folhado de Calabresa", 17.28),
("Kalzone de Calabresa", 86.45),
("Calabresa Cheddar e Batata Frita", 9.75),
("Calabresa no Pão de queijo", 133.35),
("Pirão banco com calabresa e ovo", 17.55),
("Pão de alho e calabresa", 67.77),
("Sopa de cala com lingua de boi", 100.6),
("Fondue de Chocolate", 823.4);


-- =========================================================
-- CLIENTES
-- =========================================================

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    documento VARCHAR(18) NOT NULL,
    telefone VARCHAR(15) NOT NULL
);

INSERT INTO clientes (nome, documento, telefone) VALUES
("Luquita da galera", "24.740.464/0001-00", "(96) 3741-5005"),
("Leandro Antonio Melo", "834.931.626-85", "(71) 2929-9455"),
("Isis Rebeca Vanessa Sales", "936.423.500-20", "(11) 98693-3252");

INSERT INTO clientes (nome, documento, telefone) VALUES
("Samuca", "04.422.160/0001-80", "(47) 99277-1029");


-- =========================================================
-- BEBIDAS
-- =========================================================

CREATE TABLE bebidas(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    valor DOUBLE NOT NULL,
    tipo VARCHAR(255) NOT NULL
);

INSERT INTO bebidas (nome, valor, tipo) VALUES
("Laranjinha", 18.00, "Refrigerante"),
("Fruki", 10.00, "Refrigerante"),
("Corote", 27.00, "Vodka"),
("Vinho Campo Largo 750ml", 74.43, "Vinho"),
("Del Valle 100% Laranja 1L", 66.50, "Suco");

ALTER TABLE bebidas
ADD COLUMN data_vencimento DATE;


-- =========================================================
-- MESAS
-- =========================================================

CREATE TABLE mesas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero CHAR(3) NOT NULL,
    lugares INT NOT NULL
);

INSERT INTO mesas (numero, lugares) VALUES
("002", 12),
("003", 4),
("004", 8),
("005", 5),
("006", 9),
("007", 5),
("008", 3),
("009", 2),
("010", 1),
("001", 7);


-- =========================================================
-- COMANDAS
-- =========================================================

CREATE TABLE comandas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    total DOUBLE DEFAULT(0.0),
    data_criacao DATETIME DEFAULT NOW(),

    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

INSERT INTO comandas (id_cliente) VALUES (1);
INSERT INTO comandas (id_cliente) VALUES (3);
INSERT INTO comandas (id_cliente) VALUES (4);

ALTER TABLE comandas
RENAME COLUMN data_criacao TO data_hora_criacao;


-- =========================================================
-- COMANDAS / PRATOS FEITOS
-- =========================================================

CREATE TABLE comandas_pratos_feitos (
    id INT PRIMARY KEY AUTO_INCREMENT,

    id_comanda INT NOT NULL,
    id_prato_feito INT NOT NULL,
    quantidade INT NOT NULL,

    FOREIGN KEY (id_comanda)
        REFERENCES comandas(id),

    FOREIGN KEY (id_prato_feito)
        REFERENCES pratos_feitos(id)
);

INSERT INTO comandas_pratos_feitos
(id_comanda, id_prato_feito, quantidade)
VALUES
(1, 7, 2);

INSERT INTO comandas_pratos_feitos
(id_comanda, id_prato_feito, quantidade)
VALUES
(2, 1, 4);

INSERT INTO comandas_pratos_feitos
(id_comanda, id_prato_feito, quantidade)
VALUES
(3, 6, 3),
(3, 10, 2);
