# 🏋️‍♂️ Gym Manager - Multi-Agent System

Este é um projeto de **sistema multi-agente** desenvolvido com o **Agent Development Kit (ADK) da Google**, com o objetivo de gerenciar diferentes aspectos relacionados à academia, como **Nutrição** e **Treinamento**.

---

## 📂 Estrutura de Pastas

```gym_manager/
├── sub_agents/
│   ├── nutrition_agent/
│   │   ├── tools/
│   │   │   ├── creatine_calculator.py
│   │   │   ├── imc_calculator.py
│   │   │   ├── protein_calculator.py
│   │   │   ├── tmb_calculator.py
│   │   │   └── water_per_day.py
│   │   └── agent.py
│   └── train_agent/
│       └── agent.py
├── tools/
├── agent.py
├── config.py
├── prompt.py
└── .env
```

---

## 🧠 Arquitetura dos Agentes

O sistema possui um **Agente Raiz (Root Agent)** chamado `gym_manager`, que gerencia dois sub-agentes especializados:
- **Descrição:** Gerente geral que coordena os agentes especializados.
- **Sub-agentes:**
  - `nutrition_agent`
  - `train_agent`

---

### 🍎 Sub-Agente: `nutrition_agent`

- **Responsável por:** Consultas relacionadas a **nutrição**, **cálculo de macros**, **IMC**, **TMB**, **hidratação diária** e **suplementação**.
- **Tools incluídas:**
  - `creatine_calculator.py`
  - `imc_calculator.py`
  - `protein_calculator.py`
  - `tmb_calculator.py`
  - `water_per_day.py`

---

### 🏋️ Sub-Agente: `train_agent`

- **Responsável por:** Consultas relacionadas a **treinos**, **planejamento de exercícios** e **rotinas de academia**.

---

## ⚙️ Configuração Inicial

### Pré-requisitos

- Python 3.8+
- Google Agent Development Kit (ADK)
- Variáveis de ambiente (definidas no arquivo `.env`)

---

### Instalação

1. **Crie um ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

```bash
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux/maxOS
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute o código:**
```bash
adk web
```

## 📌 Sobre o Projeto
Este projeto foi criado para fins de aprendizado e experimentação com sistemas multi-agente, com foco em aplicações para saúde, bem-estar e academia, utilizando o Google ADK como base para a arquitetura conversacional.