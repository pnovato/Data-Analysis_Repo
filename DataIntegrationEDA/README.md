# Marketing Bancário Português – Notebook de EDA Rápido

## Visão geral
Este notebook demonstra um fluxo de trabalho compacto para:

1. Baixar o **conjunto de dados Portuguese Bank Marketing** diretamente do Kaggle via `kagglehub`.  
2. Carregar os dados no pandas.  
3. Realizar uma primeira inspeção (`info`, `describe`, verificação de tipos).  
4. Plotar um histograma simples da coluna **age**.

O roteiro segue a ordem recomendada nos PDFs compartilhados (importar → inspecionar → limpar → visualizar).

---

## Conjunto de dados
| Item | Detalhes |
|------|----------|
| **Slug no Kaggle** | `aakashverma8900/portuguese-bank-marketing` |
| **Fonte original** | UCI ML Repository – Bank Marketing |
| **Variável‑alvo** | `y` (binária: o cliente subscreveu um depósito a prazo?) |
| **Arquivos** | `bank-full.csv` (ou nome equivalente) – todas as linhas e variáveis |

---

## Pré‑requisitos
```bash
python 3.8+
pip install kagglehub kaggle pandas matplotlib
```

### Token da API do Kaggle
1. No Kaggle: **Account → API → Create New Token**.  
2. Mova `kaggle.json` para `~/.kaggle/` e ajuste permissões:
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

---

## Células do notebook (copiar/colar no Jupyter Lab)
```python
# Imports
import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt

# Baixar a versão mais recente do dataset
data_path = kagglehub.dataset_download("aakashverma8900/portuguese-bank-marketing")

# Encontrar o arquivo CSV
csv_file = [f for f in os.listdir(data_path) if f.endswith(".csv")][0]
csv_path = os.path.join(data_path, csv_file)

# Carregar no DataFrame
df = pd.read_csv(csv_path, delimiter=",")

# ─── Inspeção rápida ───
df.info()
df.head()
df.describe()

# ─── Exemplos de limpeza ───
# df.columns = df.columns.str.lower().str.strip()
# df.drop_duplicates(inplace=True)

# ─── Visualização simples ───
plt.hist(df['age'], bins=10)
plt.xlabel('Age')
plt.title('Distribuição de idade')
plt.show()
```
> **Nomes de colunas**  
> No arquivo bruto a coluna está em minúsculas (`age`). Caso necessário, padronize com `df.columns = df.columns.str.lower()`.

---

## Métodos úteis do pandas (exemplos)

### Strings
```python
df['job'] = df['job'].str.upper()
df['job'].str.contains("MANAGEMENT")
df['job'].str.len()
```

### Numéricos
```python
df['balance'].sum()
df['balance'].mean()
df.describe()
```

---
