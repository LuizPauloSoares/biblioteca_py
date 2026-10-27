# 📚 Library System — bancoPython

[🇧🇷 Português](README.md) | [🇺🇸 English](README.en.md)

Library management system built with **Python**, with persistence in **SQL Server** through *stored procedures* and a graphical interface in **PyQt5**.

---

## 🧩 How it works

The system manages a library's **customers**, **employees**, **books**, **addresses**, **phone numbers** and **loans/returns**.

- All critical business logic (validations, registration, deletion, loans/returns) lives in the SQL Server **stored procedures**.
- Python talks to the database through **pyodbc**, calling the procedures via **DAO** classes.
- The domain classes (`Usuario`, `Cliente`, `Funcionario`, `Livro`, `Endereco`, `Telefone`) validate data on the application side (getters/setters with rules).
- The graphical interface (PyQt5) organizes features in a side menu by section (Customers, Employees, Books, Addresses, Phones).
- Database triggers handle automatic side effects, such as:
  - Deactivating the address when a customer/employee is deleted.
  - Updating a book's number of copies when it is borrowed/returned.
  - Marking a loan as `atrasado` (late) or `devolvido` (returned) according to the return date.

---

## 🛠️ Technologies

- **Python 3**
- **PyQt5** (graphical interface)
- **SQL Server** (relational database)
- **pyodbc** (Python ↔ SQL Server connection)
- **requests** (ZIP code lookup via the ViaCEP API)
- **Object-Oriented Programming** (inheritance with the abstract class `Usuario`)

---

## 🗄️ Data structure

Main tables of the `bancoPython` database:

| Table | Description |
|---|---|
| `tbl_uf` | Federative units (UF/state) |
| `tbl_cidade` | Cities, linked to a UF |
| `tbl_endereco` | Addresses, linked to a city |
| `tbl_usuario` | Base user data (name, CPF, email, password, birth date, address) |
| `tbl_cliente` | User specialization as a customer |
| `tbl_funcionario` | User specialization as an employee (role, salary) |
| `tbl_telefone` | Phone numbers linked to a user |
| `tbl_livro` | Book collection |
| `tbl_emprestimo` | Loans, linking book + customer + employee |

**Python code layers:**

```
classes/      → Usuario (abstract), Cliente, Funcionario, Livro, Endereco, Telefone
dao/          → ClienteDAO, FuncionarioDAO, LivroDAO, EnderecoDAO, TelefoneDAO
conexao/      → Conexao (pyodbc)
gui/          → PyQt5 interface (side menu + pages per section)
```

---

## ✅ Prerequisites

- Python 3.10+
- SQL Server (local or an accessible instance)
- ODBC driver for SQL Server installed
- Python libraries:
  ```
  pip install pyodbc PyQt5 requests
  ```

---

## ⚙️ Installation and setup

1. **Clone the project**
   ```
   git clone https://github.com/LuizPauloSoares/REPOSITORY-NAME.git
   cd REPOSITORY-NAME
   ```

2. **Create the database**
   - Run the table creation script (`CREATE DATABASE bancoPython` + `CREATE TABLE`).
   - Run the script that inserts the UFs.
   - Run the *stored procedure* scripts (address, customer, employee, book/loan, phone).

3. **Configure the connection**
   - Edit `conexao/Conexao.py` and set `Server`, `Database`, `UID` and `PWD` for your environment.

4. **Install the Python dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Run the interface**
   ```
   python main.py
   ```

---

## 💡 Usage examples

- Register a customer with personal data, address and phone (via `ClienteDAO.cadastro_cliente`).
- Lend a book to a customer, linking the responsible employee (via `LivroDAO.emprestar_livro`).
- Search addresses by ZIP code (CEP), neighborhood, street, UF or city.
- Automatically block a customer with 4 or more overdue loans.

---

## 📌 Project status

🚧 **In development**

- Database layer (tables, procedures, triggers): ✅ done
- DAO layer (Python ↔ database): ✅ done
- Domain classes with validation: ✅ done
- Graphical interface (PyQt5): 🚧 front-end ready, **integration with the DAOs still pending**
- ViaCEP API integration (`verCep`): ⚠️ contains a syntax error to fix

---

## 🗺️ Roadmap / next steps

- [ ] Connect the interface's "Executar" (Run) buttons to the respective DAOs
- [ ] Fix the `resposta.get("estado":"")` call in `verCep` (invalid syntax)
- [ ] Add registration screens (forms) to the GUI
- [ ] Standardize handling of errors returned by the procedures
- [ ] Add automated tests

---

## 📄 License

Academic project — educational use.

---

## 👤 Author

**Luiz Paulo Soares**

- 📧 Email: [luizdayspring@gmail.com](mailto:luizdayspring@gmail.com)
- 💼 LinkedIn: [luiz-paulo-soares](https://www.linkedin.com/in/luiz-paulo-soares/)
- 🐙 GitHub: [LuizPauloSoares](https://github.com/LuizPauloSoares)
- 📸 Instagram: [@lu1z_st](https://instagram.com/lu1z_st)
