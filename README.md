# 📚 Sistema de Biblioteca — bancoPython

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, com persistência em **SQL Server** via *stored procedures* e interface gráfica em **PyQt5**.

---

## 🧩 Como o sistema funciona

O sistema permite gerenciar **clientes**, **funcionários**, **livros**, **endereços**, **telefones** e **empréstimos/devoluções** de uma biblioteca.

- Toda a regra de negócio crítica (validações, cadastro, exclusão, empréstimo/devolução) vive nas **stored procedures** do SQL Server.
- O Python se comunica com o banco via **pyodbc**, chamando as procedures através das classes **DAO**.
- As classes de domínio (`Usuario`, `Cliente`, `Funcionario`, `Livro`, `Endereco`, `Telefone`) fazem a validação dos dados no lado da aplicação (getters/setters com regras).
- A interface gráfica (PyQt5) organiza as funcionalidades em um menu lateral por seção (Clientes, Funcionários, Livros, Endereços, Telefones).
- Triggers no banco cuidam de efeitos colaterais automáticos, como:
  - Desativar endereço ao excluir um cliente/funcionário.
  - Atualizar a quantidade de exemplares de um livro ao emprestar/devolver.
  - Marcar empréstimo como `atrasado` ou `devolvido` conforme a data de devolução.

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **PyQt5** (interface gráfica)
- **SQL Server** (banco de dados relacional)
- **pyodbc** (conexão Python ↔ SQL Server)
- **requests** (consulta de CEP via API ViaCEP)
- **Programação Orientada a Objetos** (herança com classe abstrata `Usuario`)

---

## 🗄️ Estrutura de dados

Principais tabelas do banco `bancoPython`:

| Tabela | Descrição |
|---|---|
| `tbl_uf` | Unidades federativas (UF/estado) |
| `tbl_cidade` | Cidades, vinculadas a uma UF |
| `tbl_endereco` | Endereços, vinculados a uma cidade |
| `tbl_usuario` | Dados base do usuário (nome, CPF, e-mail, senha, nascimento, endereço) |
| `tbl_cliente` | Especialização de usuário como cliente |
| `tbl_funcionario` | Especialização de usuário como funcionário (cargo, salário) |
| `tbl_telefone` | Telefones vinculados a um usuário |
| `tbl_livro` | Acervo de livros |
| `tbl_emprestimo` | Empréstimos, ligando livro + cliente + funcionário |

**Camadas do código Python:**

```
classes/      → Usuario (abstrata), Cliente, Funcionario, Livro, Endereco, Telefone
dao/          → ClienteDAO, FuncionarioDAO, LivroDAO, EnderecoDAO, TelefoneDAO
conexao/      → Conexao (pyodbc)
gui/          → Interface PyQt5 (menu lateral + páginas por seção)
```

---

## ✅ Pré-requisitos

- Python 3.10+
- SQL Server (local ou instância acessível)
- Driver ODBC para SQL Server instalado
- Bibliotecas Python:
  ```
  pip install pyodbc PyQt5 requests
  ```

---

## ⚙️ Instalação e configuração

1. **Clonar o projeto**
   ```
   git clone <url-do-repositorio>
   cd sistema-biblioteca
   ```

2. **Criar o banco de dados**
   - Execute o script de criação das tabelas (`CREATE DATABASE bancoPython` + `CREATE TABLE`).
   - Execute o script de inserção das UFs.
   - Execute os scripts de *stored procedures* (endereço, cliente, funcionário, livro/empréstimo, telefone).

3. **Configurar a conexão**
   - Edite `conexao/Conexao.py` e ajuste `Server`, `Database`, `UID` e `PWD` conforme seu ambiente.

4. **Instalar as dependências Python**
   ```
   pip install -r requirements.txt
   ```

5. **Executar a interface**
   ```
   python main.py
   ```

---

## 💡 Exemplos de uso

- Cadastrar um cliente informando dados pessoais, endereço e telefone (via `ClienteDAO.cadastro_cliente`).
- Emprestar um livro para um cliente, vinculando o funcionário responsável (via `LivroDAO.emprestar_livro`).
- Consultar endereços por CEP, bairro, logradouro, UF ou cidade.
- Bloquear automaticamente um cliente com 4 ou mais empréstimos em atraso.

---

## 📌 Status do projeto

🚧 **Em desenvolvimento**

- Camada de banco de dados (tabelas, procedures, triggers): ✅ concluída
- Camada DAO (Python ↔ banco): ✅ concluída
- Classes de domínio com validação: ✅ concluídas
- Interface gráfica (PyQt5): 🚧 front-end pronto, **integração com as DAOs ainda pendente**
- Integração com API ViaCEP (`verCep`): ⚠️ contém erro de sintaxe a corrigir

---

## 🗺️ Roadmap / próximos passos

- [ ] Conectar os botões "Executar" da interface às respectivas DAOs
- [ ] Corrigir chamada `resposta.get("estado":"")` em `verCep` (sintaxe inválida)
- [ ] Adicionar telas de cadastro (formulários) na GUI
- [ ] Padronizar tratamento de erros retornados pelas procedures
- [ ] Adicionar testes automatizados

---

## 📄 Licença

Projeto acadêmico — uso educacional.

---

## 👤 Autor

**Luiz**

- 📧 E-mail: 
- 💼 LinkedIn: 
- 🐙 GitHub: 
- 📸 Instagram:
