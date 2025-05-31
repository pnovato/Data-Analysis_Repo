# Mini-Projeto: Limpeza de Dados com KaggleHub

Este repositório mostra, em pequenos scripts Python, como:

1. **Fazer download automático** de datasets públicos do Kaggle usando **kagglehub**.  
2. **Carregar** os dados com *pandas*.  
3. **Lidar com valores ausentes** (imputação por média ou moda).  
4. **Detectar e tratar outliers** pelo método IQR (winsorização/capping).  
5. **Gravar** um arquivo CSV limpo e gerar **boxplots** para inspeção rápida.

> Os exemplos seguem a mesma estrutura para facilitar a leitura e adaptação a outros conjuntos de dados.

---

## Estrutura dos Scripts

| Script                           | Dataset            | Tamanho                | Observações                                            |
|----------------------------------|--------------------|------------------------|--------------------------------------------------------|
| `Iris_missing_outlier.py`        | Iris               | 150 linhas, 5 colunas  | Padroniza nomes de colunas em minúsculas               |

Cada ficheiro segue as **5 secções-chave**:

1. **Download & Localização** – `kagglehub.dataset_download()` + descoberta do CSV.  
2. **Carregamento** – `pd.read_csv()`.  
3. **Missing Values** – imputação condicional.  
4. **Outliers (IQR)** – cálculo dos limites e `clip()`.  
5. **Salvar & Gráfico** – escreve `*_cleaned.csv` e mostra boxplot.

---

## Requisitos

```bash
python >= 3.9
pandas
numpy
matplotlib
kagglehub
```

Instale tudo com:

```bash
pip install pandas numpy matplotlib kagglehub
```

> **Nota:** para `kagglehub` funcionar, configure a sua API key do Kaggle (ficheiro `~/.kaggle/kaggle.json`).

---

## Como Executar

```bash
# Ambiente virtual opcional
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
Jupyter lab   
```
---
