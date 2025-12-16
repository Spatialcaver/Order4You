

---

# 🧾O **Order4You** é um sistema robusto de recebimento e gestão de pedidos online, desenvolvido com **Django Rest Framework (DRF)**. Diferente de sistemas de pedidos convencionais, ele possui um **ERP embutido** focado no controle rigoroso de vendas e estoque de matéria-prima.

## 🚀 Diferencial do Projeto: 
### Baixa Automática por Composição. O grande destaque deste projeto é a inteligência na gestão de insumos através do **BOM (Bill of Materials)**.

#### Quando um produto é vendido, o sistema não apenas reduz a unidade do produto final, mas calcula e subtrai automaticamente as quantidades de cada ingrediente do estoque. Por exemplo:

* **Venda**: 1x Pizza Calabresa.
* **Baixa automática**: 500g de queijo, 50g de molho e 200g de calabresa.

## 🏗️ Estrutura de Módulos:
### O projeto é organizado de forma modular para garantir escalabilidade e manutenção:

* **`catalog`**: Gestão de produtos, categorias e a árvore de composição (BOM).
* **`estoque`**: Controle de matéria-prima, fornecedores, saldo atual e histórico de movimentações (Entradas/Saídas).
* **`order`**: Fluxo completo de pedidos, desde o rascunho até a entrega e pagamento.
* **`user`**: Sistema de autenticação com 4 níveis de acesso (Admin, Gerente, Funcionário e Cliente).
* **`venda`**: Módulo financeiro para registro de vendas concluídas e análise de custos de produção.

## 👥 Perfis de Acesso:
### O sistema gerencia permissões específicas para cada tipo de usuário:

1. **Admin**: Acesso total ao sistema e configurações de infraestrutura.
2. **Gerente**: Visão total do ERP, gestão de estoque, custos, relatórios financeiros e catálogo.
3. **Funcionário**: Operação focada no fluxo de gestão e visualização de pedidos (Cozinha/Expedição).
4. **Cliente**: Interface simplificada para login e realização de pedidos.

## 🛠️ Tecnologias Utilizadas:
* **Python 3.x**
* **Django 6.0**
* **Django Rest Framework (DRF)**
* **SQLite** (Ambiente de desenvolvimento)

## ⚙️ Regras de Negócio Implementadas:
###  **Gating de Estoque**: Produtos produzidos ficam automaticamente indisponíveis se algum ingrediente essencial estiver abaixo do nível necessário.
* **Integridade Financeira**: Registros de vendas são protegidos contra exclusão acidental através de `models.PROTECT` nos relacionamentos críticos.
* **Rastreabilidade**: Toda alteração no estoque gera um registro de movimentação com o saldo anterior e o atual para auditoria.

---

### Como rodar o projeto localmente
1. Clone o repositório.
2. Crie um ambiente virtual:  `python -m venv venv`
3. Ative o venv: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac).
4. Instale as dependências (se houver um `requirements.txt`).
5. Execute as migrações: `python manage.py migrate`.
6. Inicie o servidor: `python manage.py runserver`.

---

