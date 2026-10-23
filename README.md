# ATV09 - Migração do Portal para Django

**Dupla:** Amanda Bispo Barros de Araújo e Maisa Bezerra Azarias  
**Turma:** 513  

---

##  Descrição do Projeto
Este projeto consiste na reestruturação e migração do portal web Black Coquette (desenvolvido na ATV07) para o framework Django. A aplicação utiliza arquitetura baseada em banco de dados e rotas dinâmicas, permitindo a gestão de conteúdos e itens do menu de navegação por meio da interface do Django Admin.

---

##  Tecnologias Utilizadas
* **Python 3**
* **Django**
* **HTML5 / CSS3** (com layouts em Flexbox e estilos customizados)
* **JavaScript** (efeito interativo de brilho)
* **SQLite** (banco de dados padrão do Django)

---

##  Estrutura de Arquivos
```text
ATV09_AMANDA_MAISA/
├── amanda_maisa/           # Configurações do projeto Django (settings, urls principais)
├── portal/                 # Aplicação do portal
│   ├── static/             # Arquivos estáticos (css, imagens, pdf)
│   │   └── portal/
│   │       ├── css/
│   │       ├── img/
│   │       └── pdf/
│   ├── templates/          # Templates HTML com tags Django
│   │   └── portal/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── conteudo.html
│   ├── admin.py            # Cadastro dos Models no Django Admin
│   ├── models.py           # Modelos de dados (Conteudo e Menu)
│   ├── urls.py             # Mapeamento de rotas e slugs
│   └── views.py            # Regras de negócio e renderização
├── db.sqlite3              # Banco de dados com o conteúdo cadastrado
├── manage.py
└── README.md
