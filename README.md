# 🏊‍♂️ Projeto TCC — Sistema de Cadastro de Competidores

Sistema web desenvolvido como Trabalho de Conclusão de Curso (TCC) para gerenciamento de competidores de natação, permitindo cadastro e futura administração dos dados via interface web.

## 📌 Objetivo

Desenvolver uma aplicação web simples e funcional utilizando Flask e MySQL para registrar competidores, aplicando conceitos de:

* desenvolvimento backend
* integração com banco de dados
* arquitetura web
* versionamento com Git/GitHub

## 🚀 Tecnologias utilizadas

* Python
* Flask
* MySQL
* HTML5
* CSS3
* Git e GitHub

## 🧠 Funcionalidades implementadas até o momento

* Cadastro de competidores via formulário
* Integração com banco MySQL
* Inserção de dados persistente
* Mensagem de confirmação ao cadastrar
* Interface estilizada com CSS
* Estrutura organizada (templates + static)

## 🗂 Estrutura do projeto

```
TCC/
│ app.py
│
├── templates/
│     home.html
│
└── static/
      └── css/
            style.css
```

## 🛠 Como executar o projeto

1. Clonar o repositório:

```
git clone https://github.com/PabloVavrik/Projeto-TCC.git
```

2. Entrar na pasta:

```
cd Projeto-TCC
```

3. Instalar dependências:

```
pip install flask mysql-connector-python
```

4. Configurar o MySQL:

* criar banco `natacao`
* criar tabela `competidores`

Exemplo:

```sql
CREATE DATABASE natacao;

USE natacao;

CREATE TABLE competidores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    modalidade VARCHAR(100)
);
```

5. Rodar a aplicação:

```
python app.py
```

6. Acessar no navegador:

```
http://localhost:5000
```

## 📈 Próximos passos do projeto

* Listagem de competidores (READ)
* Atualização de dados (UPDATE)
* Exclusão de registros (DELETE)
* Estruturação em MVC
* Documentação com Swagger
* Interface administrativa

## 👨‍💻 Autor

Projeto desenvolvido por Pablo Vavrik como parte do Trabalho de Conclusão de Curso em Análise e Desenvolvimento de Sistemas.
