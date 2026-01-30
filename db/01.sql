CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

-- 1) CARGOS
CREATE TABLE cargos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(60) NOT NULL,
  nivel ENUM('JUNIOR','PLENO','SENIOR','LEAD','GERENCIA') NOT NULL,
  salario_base DECIMAL(10,2) NOT NULL,
  UNIQUE (nome, nivel)
);

-- 2) FUNCIONARIOS
CREATE TABLE funcionarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(120) NOT NULL,
  cpf CHAR(11) NOT NULL UNIQUE,
  email VARCHAR(120) UNIQUE,
  data_admissao DATE NOT NULL,
  cargo_id INT NOT NULL,
  salario DECIMAL(10,2) NOT NULL,
  ativo TINYINT(1) NOT NULL DEFAULT 1,
  CONSTRAINT fk_func_cargo
    FOREIGN KEY (cargo_id) REFERENCES cargos(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- 3) DEPENDENTES
CREATE TABLE dependentes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  funcionario_id INT NOT NULL,
  nome VARCHAR(120) NOT NULL,
  parentesco ENUM('FILHO','FILHA','CONJUGE','PAI','MAE','OUTRO') NOT NULL,
  data_nascimento DATE NOT NULL,
  CONSTRAINT fk_dep_func
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


-- CARGOS
INSERT INTO cargos (nome, nivel, salario_base) VALUES
('Desenvolvedor', 'JUNIOR', 3500.00),
('Desenvolvedor', 'PLENO', 6000.00),
('Desenvolvedor', 'SENIOR', 9000.00),
('QA', 'PLENO', 5000.00),
('Tech Lead', 'LEAD', 12000.00),
('Gerente', 'GERENCIA', 15000.00);

-- FUNCIONARIOS
INSERT INTO funcionarios (nome, cpf, email, data_admissao, cargo_id, salario, ativo) VALUES
('Ana Souza',     '12345678901', 'ana@empresa.com',     '2023-01-10', 1, 3800.00, 1),
('Bruno Lima',    '12345678902', 'bruno@empresa.com',   '2022-07-05', 2, 6500.00, 1),
('Carla Mendes',  '12345678903', 'carla@empresa.com',   '2021-03-20', 3, 9800.00, 1),
('Diego Alves',   '12345678904', 'diego@empresa.com',   '2024-02-01', 4, 5200.00, 1),
('Erika Santos',  '12345678905', 'erika@empresa.com',   '2020-11-11', 5, 12500.00, 1),
('Fabio Rocha',   '12345678906', 'fabio@empresa.com',   '2019-08-25', 6, 16000.00, 0);

-- DEPENDENTES
INSERT INTO dependentes (funcionario_id, nome, parentesco, data_nascimento) VALUES
(1, 'Lucas Souza', 'FILHO',   '2016-05-12'),
(1, 'Marina Souza','FILHA',   '2019-10-02'),
(2, 'Paula Lima',  'CONJUGE', '1995-09-18'),
(3, 'Rafael Mendes','FILHO',  '2013-12-01'),
(5, 'Joana Santos','CONJUGE', '1992-04-07'),
(5, 'Pedro Santos','FILHO',   '2018-01-30');


SELECT
  f.id,
  f.nome,
  f.email,
  c.nome AS cargo,
  c.nivel,
  f.salario,
  f.data_admissao
FROM funcionarios f
JOIN cargos c ON c.id = f.cargo_id
ORDER BY f.nome;



SELECT
  f.nome AS funcionario,
  c.nome AS cargo,
  c.nivel,
  d.nome AS dependente,
  d.parentesco,
  d.data_nascimento
FROM funcionarios f
JOIN cargos c ON c.id = f.cargo_id
LEFT JOIN dependentes d ON d.funcionario_id = f.id
ORDER BY f.nome, d.data_nascimento;



SELECT
  f.id,
  f.nome,
  c.nome AS cargo,
  c.nivel,
  COUNT(d.id) AS total_dependentes
FROM funcionarios f
JOIN cargos c ON c.id = f.cargo_id
LEFT JOIN dependentes d ON d.funcionario_id = f.id
GROUP BY f.id, f.nome, c.nome, c.nivel
ORDER BY total_dependentes DESC, f.nome;




SELECT
  f.nome,
  c.nome AS cargo,
  c.nivel,
  c.salario_base,
  f.salario,
  (f.salario - c.salario_base) AS diferenca
FROM funcionarios f
JOIN cargos c ON c.id = f.cargo_id
WHERE f.salario > c.salario_base
ORDER BY diferenca DESC;


SELECT
  f.nome,
  c.nome AS cargo,
  c.nivel,
  f.salario
FROM funcionarios f
JOIN cargos c ON c.id = f.cargo_id
WHERE f.ativo = 1
ORDER BY f.nome;


SELECT
  d.nome AS dependente,
  d.parentesco,
  d.data_nascimento,
  f.nome AS funcionario,
  c.nome AS cargo,
  c.nivel
FROM dependentes d
JOIN funcionarios f ON f.id = d.funcionario_id
JOIN cargos c ON c.id = f.cargo_id
ORDER BY d.nome;



