
# Projeto AD — Coleção de Mini‑Projetos de Ciência de Dados

Este repositório reúne **três mini‑projetos independentes** que ilustram etapas essenciais de um fluxo de *Data Science*:

1. **Primeiro contacto com dados** (Pt banking)  
2. **Limpeza de dados em dataset e tratamento de outliers** (Iris)  
3. **Exploração e visualização de dados** (Students Performance)

A ideia é construir, passo a passo, pequenos blocos reutilizáveis para um pipeline completo:  
*obter → limpar → explorar → visualizar → modelar*.

---

## Visão Geral dos Mini‑Projetos

| # | Script / Pasta                     | Tema                          | Foco principal                              |
|---|------------------------------------|--------------------------------|---------------------------------------------|
| 1 | `pt_banking.py` | **Pt banking**           | Primeiro contacto com dados |
| 2 | `iris_missing_outlier.py`        | **Iris**                      | Exemplo enxuto de limpeza em dataset pequeno |
| 3 | `dataviz_project.py` + `figures/`      | **Students Performance**      | Geração de 6 gráficos (univariados → multivariados) |

> Todos os scripts baixam o dataset via **kagglehub** (é necessário ter a API key configurada).

---

## Requisitos Comuns

```bash
python >= 3.9
pandas
numpy
matplotlib
seaborn        # apenas para o projeto 3
kagglehub
```

Instalação rápida:

```bash
pip install pandas numpy matplotlib seaborn kagglehub
```

Configure também a API key do Kaggle (`~/.kaggle/kaggle.json`) para que o **kagglehub** consiga baixar datasets.

---

## Como Executar Cada Mini‑Projeto

1. **Pt banking**  
   ```bash
   python pt_banking.py
   ```
   

2. **Iris**  
   ```bash
   python iris_missing_outlier.py
   ```
   

3. **Visualização (Students Performance)**  
   ```bash
   python dataviz_project.py
   ```
   > Siga a ordem que preferir: cada script é independente.

---
