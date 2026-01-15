import express from 'express';

const app = express();
const PORT = 3000;

app.use(express.json());

let alunos = [
  { matricula: '2024001', nome: 'João Silva', idade: 20, curso: 'Engenharia' },
  { matricula: '2024002', nome: 'Maria Santos', idade: 22, curso: 'Medicina' }
];

app.get('/alunos', (req, res) => {
  res.json(alunos);
});

app.get('/alunos/:matricula', (req, res) => {
  const aluno = alunos.find(a => a.matricula === req.params.matricula);
  
  if (!aluno) {
    return res.status(404).json({ erro: 'Aluno não encontrado' });
  }
  
  res.json(aluno);
});

app.post('/alunos', (req, res) => {
  const { matricula, nome, idade, curso } = req.body;
  
  if (!matricula || !nome || !idade || !curso) {
    return res.status(400).json({ erro: 'Todos os campos são obrigatórios' });
  }
  
  if (alunos.find(a => a.matricula === matricula)) {
    return res.status(400).json({ erro: 'Matrícula já cadastrada' });
  }
  
  const novoAluno = { 
    matricula, 
    nome, 
    idade: Number(idade), 
    curso 
  };
  
  alunos.push(novoAluno);
  
  res.status(201).json(novoAluno);
});

app.put('/alunos/:matricula', (req, res) => {
  const { matricula } = req.params;
  const { nome, idade, curso } = req.body;
  
  const index = alunos.findIndex(a => a.matricula === matricula);
  
  if (index === -1) {
    return res.status(404).json({ erro: 'Aluno não encontrado' });
  }
  
  // Atualiza apenas os campos fornecidos
  if (nome) alunos[index].nome = nome;
  if (idade) alunos[index].idade = Number(idade);
  if (curso) alunos[index].curso = curso;
  
  res.json(alunos[index]);
});

app.delete('/alunos/:matricula', (req, res) => {
  const { matricula } = req.params;
  
  const index = alunos.findIndex(a => a.matricula === matricula);
  
  if (index === -1) {
    return res.status(404).json({ erro: 'Aluno não encontrado' });
  }
  
  const alunoRemovido = alunos.splice(index, 1)[0];
  
  res.json({ 
    mensagem: 'Aluno removido com sucesso', 
    aluno: alunoRemovido 
  });
});

app.listen(PORT, () => {
  console.log(`🚀 Servidor rodando em http://localhost:${PORT}`);
});
