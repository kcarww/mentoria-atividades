// server.js
/*
npm init -y
npm i express mysql2 dotenv
npm i -D nodemon

Crie um .env:
PORT=3000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=clientes_db
DB_PORT=3306

Rodar:
node server.js
ou (dev):
npx nodemon server.js
*/

const express = require("express");
const mysql = require("mysql2/promise");
require("dotenv").config();

const app = express();
app.use(express.json());

// Pool (igual ao seu)
const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: Number(process.env.DB_PORT || 3306),
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

// helpers simples
function toInt(value) {
  const n = Number(value);
  return Number.isInteger(n) && n > 0 ? n : null;
}

function validateBody(req, res) {
  const { name, email, phone } = req.body || {};
  if (!name || !email || !phone) {
    res.status(400).json({ error: "Campos obrigatórios: name, email, phone" });
    return null;
  }
  return { name, email, phone };
}

// HEALTH (testa conexão)
app.get("/health", async (req, res) => {
  try {
    const connection = await pool.getConnection();
    connection.release();
    return res.json({ ok: true, message: "Conexão bem-sucedida ao banco!" });
  } catch (error) {
    return res.status(500).json({ ok: false, error: String(error.message || error) });
  }
});

// CREATE
app.post("/clients", async (req, res) => {
  const body = validateBody(req, res);
  if (!body) return;

  try {
    const query = "INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)";
    const [result] = await pool.execute(query, [body.name, body.email, body.phone]);
    return res.status(201).json({ message: "Cliente cadastrado!", id: result.insertId });
  } catch (error) {
    return res.status(500).json({ error: String(error.message || error) });
  }
});

// LIST
app.get("/clients", async (req, res) => {
  try {
    const query = "SELECT * FROM clients";
    const [rows] = await pool.execute(query);
    return res.json(rows);
  } catch (error) {
    return res.status(500).json({ error: String(error.message || error) });
  }
});

// GET BY ID
app.get("/clients/:id", async (req, res) => {
  const id = toInt(req.params.id);
  if (!id) return res.status(400).json({ error: "ID inválido" });

  try {
    const query = "SELECT * FROM clients WHERE id = ?";
    const [rows] = await pool.execute(query, [id]);

    if (rows.length === 0) return res.status(404).json({ error: "Cliente não encontrado" });
    return res.json(rows[0]);
  } catch (error) {
    return res.status(500).json({ error: String(error.message || error) });
  }
});

// UPDATE
app.put("/clients/:id", async (req, res) => {
  const id = toInt(req.params.id);
  if (!id) return res.status(400).json({ error: "ID inválido" });

  const body = validateBody(req, res);
  if (!body) return;

  try {
    const query = "UPDATE clients SET name = ?, email = ?, phone = ? WHERE id = ?";
    const [result] = await pool.execute(query, [body.name, body.email, body.phone, id]);

    if (result.affectedRows === 0) return res.status(404).json({ error: "Cliente não encontrado" });
    return res.json({ message: "Cliente atualizado!", id });
  } catch (error) {
    return res.status(500).json({ error: String(error.message || error) });
  }
});

// DELETE
app.delete("/clients/:id", async (req, res) => {
  const id = toInt(req.params.id);
  if (!id) return res.status(400).json({ error: "ID inválido" });

  try {
    const query = "DELETE FROM clients WHERE id = ?";
    const [result] = await pool.execute(query, [id]);

    if (result.affectedRows === 0) return res.status(404).json({ error: "Cliente não encontrado" });
    return res.json({ message: "Cliente deletado!", id });
  } catch (error) {
    return res.status(500).json({ error: String(error.message || error) });
  }
});

const PORT = Number(process.env.PORT || 3000);
app.listen(PORT, () => console.log(`API rodando em http://localhost:${PORT}`));
