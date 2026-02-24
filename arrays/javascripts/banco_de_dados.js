/*
npm init -y
npm i express mysql2 dotenv
npm i -D nodemon

PORT=3000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=clientes_db
DB_PORT=3306


*/


const mysql = require("mysql2/promise");
require("dotenv").config();

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: Number(process.env.DB_PORT || 3306),
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});


async function testConnection() {
    try {
        const connection = await pool.getConnection();
        console.log("Conexão bem-sucedida ao banco de dados!");
        connection.release();
    }
    catch (error) {
        console.error("Erro ao conectar ao banco de dados:", error);
    }
}

async function cadastrarCliente(nome, email, phone) {
    try {
        const connection = await pool.getConnection();
        const query = "INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)";
        const [result] = await connection.execute(query, [nome, email, phone]);
        console.log("Cliente cadastrado com sucesso! ID:", result.insertId);
        connection.release();
    }
    catch (error) {
        console.error("Erro ao cadastrar cliente:", error);
    }
}

async function listarClientes() {
    try {
        const connection = await pool.getConnection();
        const query = "SELECT * FROM clients";
        const [rows] = await connection.execute(query);
        console.log("Clientes cadastrados:", rows);
        connection.release();
    }
    catch (error) {
        console.error("Erro ao listar clientes:", error);
    }
}

async function getClienteById(id) {
    try {
        const connection = await pool.getConnection();
        const query = "SELECT * FROM clients WHERE id = ?";
        const [rows] = await connection.execute(query, [id]);
        if (rows.length > 0) {
            console.log("Cliente encontrado:", rows[0]);
        }
        else {
            console.log("Cliente não encontrado com ID:", id);
        }
        connection.release();
    }
    catch (error) {
        console.error("Erro ao buscar cliente por ID:", error);
    }
}

async function atualizarCliente(id, nome, email, phone) {
    try {
        const connection = await pool.getConnection();
        const query = "UPDATE clients SET name = ?, email = ?, phone = ? WHERE id = ?";
        const [result] = await connection.execute(query, [nome, email, phone, id]);
        if (result.affectedRows > 0) {
            console.log("Cliente atualizado com sucesso! ID:", id);
        }
        else {
            console.log("Cliente não encontrado para atualização com ID:", id);
        }
        connection.release();
    }
    catch (error) {
        console.error("Erro ao atualizar cliente:", error);
    }
}

async function deletarCliente(id) {
    try {
        const connection = await pool.getConnection();
        const query = "DELETE FROM clients WHERE id = ?";
        const [result] = await connection.execute(query, [id]);
        if (result.affectedRows > 0) {
            console.log("Cliente deletado com sucesso! ID:", id);
        }
        else {
            console.log("Cliente não encontrado para deleção com ID:", id);
        }
        connection.release();
    }
    catch (error) {
        console.error("Erro ao deletar cliente:", error);
    }
}

// // testConnection();
// cadastrarCliente("Carlos", "na@nana.com", "123456789");
// listarClientes();
// getClienteById(2);
// atualizarCliente(1, "Carlos Silva", "cc@aaa.com", "987654321");
deletarCliente(1);

module.exports = pool;
