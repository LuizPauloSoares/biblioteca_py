CREATE DATABASE bancoPython
GO

USE bancoPython
GO

CREATE TABLE tbl_uf(
	id_uf INT IDENTITY PRIMARY KEY,
	uf CHAR(2)UNIQUE NOT NULL ,
	estado VARCHAR(50)UNIQUE NOT NULL
)

CREATE TABLE tbl_cidade(
	id_cidade INT IDENTITY PRIMARY KEY,
	cidade VARCHAR(50)NOT NULL,
	id_uf_fk INT NOT NULL,
	FOREIGN KEY (id_uf_fk) REFERENCES tbl_uf (id_uf)
)

CREATE TABLE tbl_endereco(
	id_endereco INT IDENTITY PRIMARY KEY,
	logradouro VARCHAR(100)NOT NULL,
	cep CHAR(9)NOT NULL,
	bairro VARCHAR (100)NOT NULL,
	status_endereco VARCHAR (50)NOT NULL,
	id_cidadeFK INT NOT NULL,
	FOREIGN KEY (id_cidadeFK) REFERENCES tbl_cidade (id_cidade)
)


CREATE TABLE tbl_livro(
	id_livro INT IDENTITY PRIMARY KEY,
	titulo VARCHAR(100)NOT NULL,
	autor VARCHAR(100)NOT NULL,
	ano_lancamento INT NOT NULL,
	editora VARCHAR (50) NOT NULL,
	genero VARCHAR (50) NOT NULL,
	qnt_livro INT NOT NULL
)

CREATE TABLE tbl_usuario(
	id_usuario INT IDENTITY PRIMARY KEY,
	nome_usuario VARCHAR (50) NOT NULL,
	cpf CHAR(11) UNIQUE NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	senha VARCHAR(255) NOT NULL,
	data_nascimento DATE NOT NULL,
	numero_residencia VARCHAR(50) NOT NULL,
	complemento VARCHAR (50),
	id_endereco_fk INT NOT NULL,
	FOREIGN KEY (id_endereco_fk) REFERENCES tbl_endereco (id_endereco)
)

CREATE TABLE tbl_cliente(
	id_cliente INT IDENTITY PRIMARY KEY,
	data_cadastro DATE NOT NULL,
	status_cliente VARCHAR(100) NOT NULL,
	id_usuario_fk INT UNIQUE ,
	FOREIGN KEY (id_usuario_fk) REFERENCES tbl_usuario (id_usuario)

)


CREATE TABLE tbl_funcionario(
	id_matricula INT IDENTITY PRIMARY KEY,
	cargo VARCHAR (50)NOT NULL,
	salario DECIMAL (10,2)NOT NULL,
	id_usuario_fk INT UNIQUE ,
	FOREIGN KEY (id_usuario_fk) REFERENCES tbl_usuario (id_usuario)
)

CREATE TABLE tbl_telefone(
	id_telefone INT IDENTITY PRIMARY KEY,	
	tipo VARCHAR(50) NOT NULL,
	status_telefone VARCHAR(50) NOT NULL,
	telefone CHAR(11) NOT NULL,
	id_usuario_fk INT NOT NULL,
	FOREIGN KEY (id_usuario_fk) REFERENCES tbl_usuario (id_usuario)
)

CREATE TABLE tbl_emprestimo(
	id_emprestimo INT IDENTITY PRIMARY KEY,
	data_emprestimo DATE NOT NULL,
	data_previsao DATE,
	data_devolucao DATE,
	status_emprestimo VARCHAR(50)NOT NULL,
	id_livrofk INT NOT NULL,
	id_clientefk INT NOT NULL,
	id_funcionariofk INT NOT NULL,
	FOREIGN KEY (id_livrofk) REFERENCES tbl_livro (id_livro), 
	FOREIGN KEY (id_clientefk) REFERENCES tbl_cliente (id_cliente),
	FOREIGN KEY (id_funcionariofk) REFERENCES tbl_funcionario (id_matricula)
)





SELECT * FROM tbl_uf;

SELECT * FROM tbl_cidade;

SELECT * FROM tbl_endereco;

SELECT * FROM tbl_livro;

SELECT * FROM tbl_usuario;

SELECT * FROM tbl_cliente;

SELECT * FROM tbl_funcionario;

SELECT * FROM tbl_telefone;

SELECT * FROM tbl_emprestimo;

INSERT INTO tbl_uf (uf, estado) VALUES
('AC', 'Acre'),
('AL', 'Alagoas'),
('AP', 'Amapá'),
('AM', 'Amazonas'),
('BA', 'Bahia'),
('CE', 'Ceará'),
('DF', 'Distrito Federal'),
('ES', 'Espírito Santo'),
('GO', 'Goiás'),
('MA', 'Maranhão'),
('MT', 'Mato Grosso'),
('MS', 'Mato Grosso do Sul'),
('MG', 'Minas Gerais'),
('PA', 'Pará'),
('PB', 'Paraíba'),
('PR', 'Paraná'),
('PE', 'Pernambuco'),
('PI', 'Piauí'),
('RJ', 'Rio de Janeiro'),
('RN', 'Rio Grande do Norte'),
('RS', 'Rio Grande do Sul'),
('RO', 'Rondônia'),
('RR', 'Roraima'),
('SC', 'Santa Catarina'),
('SP', 'São Paulo'),
('SE', 'Sergipe'),
('TO', 'Tocantins')