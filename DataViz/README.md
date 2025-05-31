
# Mini-Projeto de Visualização de Dados (Students Performance)

Este mini-projeto demonstra um fluxo completo de **download**, **exploração** e **visualização** de dados.

O script-único `dataviz_project.py` executa tudo:

1. Baixa automaticamente o dataset **Students Performance in Exams** (`spscientist/students-performance-in-exams`) com **kagglehub**.  
2. Carrega o CSV em *pandas* e imprime informações básicas.  
3. Cria **seis** gráficos padrão (PNG) — 2 univariados, 2 bivariados e 2 multivariados/facetados — aplicando boas práticas de design.

> Resultado ➜ arquivos `.png` guardados na pasta **figures/**.

---

## Estrutura

```
├── dataviz_project.py      # script principal
├── figures/                # ← gerada automaticamente
│   ├── univariate_gender_count.png
│   ├── univariate_math_hist.png
│   ├── bivariate_box_math_gender.png
│   ├── bivariate_scatter_read_write.png
│   ├── multivariate_scatter_hue_style.png
│   └── multivariate_facet_math_gender.png
└── README_dataviz.md       # este documento
```

---

## Requisitos

```bash
python >= 3.9
pandas
numpy
matplotlib
seaborn
kagglehub
```
Instalação rápida:
```bash
pip install pandas numpy matplotlib seaborn kagglehub
```
> **Observação:** configure a sua API key do Kaggle (`~/.kaggle/kaggle.json`) para que o `kagglehub` consiga baixar datasets.

---

## Como Executar

```bash
python dataviz_project.py
```
O script:
1. Descobre o CSV e carrega em `df`.  
2. Exibe `df.head()`, `df.info()` e `df.describe()` no terminal.  
3. Gera e salva os 6 gráficos.

Abra a pasta **figures/** para visualizar as imagens.

---

## Gráficos Gerados

| Categoria     | Descrição                                          | Arquivo |
|---------------|----------------------------------------------------|---------|
| Univariado    | Contagem de estudantes por gênero                  | `univariate_gender_count.png` |
| Univariado    | Histograma + KDE das notas de matemática           | `univariate_math_hist.png` |
| Bivariado     | Boxplot das notas de matemática por gênero         | `bivariate_box_math_gender.png` |
| Bivariado     | Dispersão Reading vs Writing scores                | `bivariate_scatter_read_write.png` |
| Multivariado  | Dispersão Reading×Writing (hue=gender, style=prep) | `multivariate_scatter_hue_style.png` |
| Multivariado  | FacetGrid: distribuição de Math score por gênero   | `multivariate_facet_math_gender.png` |

---

