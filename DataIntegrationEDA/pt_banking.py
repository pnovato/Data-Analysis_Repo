{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0f476a04-860d-4652-aa49-318e3bcf356d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Warning: Looks like you're using an outdated `kagglehub` version (installed: 0.3.10), please consider upgrading to the latest version (0.3.12).\n",
      "Path to dataset files: /home/ptrck/.cache/kagglehub/datasets/aakashverma8900/portuguese-bank-marketing/versions/1/Bank Marketing.csv\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 45211 entries, 0 to 45210\n",
      "Data columns (total 17 columns):\n",
      " #   Column                 Non-Null Count  Dtype \n",
      "---  ------                 --------------  ----- \n",
      " 0   Age                    45211 non-null  int64 \n",
      " 1   Job                    45211 non-null  object\n",
      " 2   Marital Status         45211 non-null  object\n",
      " 3   Education              45211 non-null  object\n",
      " 4   Credit                 45211 non-null  object\n",
      " 5   Balance (euros)        45211 non-null  int64 \n",
      " 6   Housing Loan           45211 non-null  object\n",
      " 7   Personal Loan          45211 non-null  object\n",
      " 8   Contact                45211 non-null  object\n",
      " 9   Last Contact Day       45211 non-null  int64 \n",
      " 10  Last Contact Month     45211 non-null  object\n",
      " 11  Last Contact Duration  45211 non-null  int64 \n",
      " 12  Campaign               45211 non-null  int64 \n",
      " 13  Pdays                  45211 non-null  int64 \n",
      " 14  Previous               45211 non-null  int64 \n",
      " 15  Poutcome               45211 non-null  object\n",
      " 16  Subscription           45211 non-null  int64 \n",
      "dtypes: int64(8), object(9)\n",
      "memory usage: 5.9+ MB\n",
      "\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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27ZtVo8ePazrrrvOi13/OsuWLbNWrFhh7du3zyosLLT+8pe/WA0aNLB27dplWZY5c55uy5Yt1pVXXml16NDBGj58uL3flFknTJhg/eEPf7C+/fZbe/vuu+/sdVPmPHLkiNWyZUvrgQcesDZv3mx99dVX1sqVK60vv/zSrpk8ebLldDqtpUuXWp9//rl16623WrGxsdYPP/zgxc7PX2lpqcfzmZuba0myPvnkE8uyzHlOJ02aZIWHh1vLly+3ioqKrMWLF1uNGjWypk+fbteY8pxalmXdddddVlxcnLVu3Tpr//791oQJEyyHw2EdPHjQsiyzZj0XhBwvKS0ttSRZ69atsyzLssrKyqwGDRpYixcvtmv27NljSbLy8vK81WadadKkifXmm28aOeexY8es1q1bW7m5udYf//hHO+SYNOuECROsjh07nnXNpDnHjh1rXX/99T+7XlNTY0VGRlpTp06195WVlVnBwcHWO++8cyFarDfDhw+3WrVqZdXU1Bj1nA4YMMAaMmSIx7477rjDSk1NtSzLrOf0+++/twICAqzly5d77O/SpYs1fvx4o2Y9V7xd5SXl5eWSpKZNm0qS8vPzVV1drcTERLumbdu2atGihfLy8rzSY104deqU3n33XVVWViohIcHIOdPT0zVgwACPmSTzntP9+/crOjpaV111lVJTU3XgwAFJZs25bNkydevWTX/605/UvHlzde7cWW+88Ya9XlRUJJfL5TGr0+lUfHy8z816uhMnTujtt9/WkCFD5OfnZ9Rzet1112n16tXat2+fJOnzzz/Xhg0bdNNNN0ky6zk9efKkTp06pZCQEI/9oaGh2rBhg1Gzniufv+KxL6qpqdGIESPUs2dPXXPNNZIkl8uloKCgM34wNCIiQi6Xywtd/jY7d+5UQkKCjh8/rkaNGmnJkiWKi4tTQUGBUXO+++672r59u8d73rVMek7j4+M1d+5ctWnTRt9++62efvpp9erVS7t27TJqzq+++kozZ87UqFGj9Je//EVbt27VY489pqCgIA0ePNie56c/HeOLs55u6dKlKisr0wMPPCDJrH93MzMz5Xa71bZtWwUEBOjUqVOaNGmSUlNTJcmo57Rx48ZKSEjQs88+q3bt2ikiIkLvvPOO8vLydPXVVxs167ki5HhBenq6du3apQ0bNni7lXrTpk0bFRQUqLy8XH//+981ePBgrVu3zttt1ani4mINHz5cubm5Z/yfk2lq/69Xkjp06KD4+Hi1bNlSixYtUmhoqBc7q1s1NTXq1q2bnn/+eUlS586dtWvXLs2aNUuDBw/2cnf1Z86cObrpppsUHR3t7Vbq3KJFizR//nwtWLBAf/jDH1RQUKARI0YoOjrayOf0f//3fzVkyBBdfvnlCggIUJcuXXT33XcrPz/f2615BW9XXWAZGRlavny5PvnkE11xxRX2/sjISJ04cUJlZWUe9SUlJYqMjLzAXf52QUFBuvrqq9W1a1dlZ2erY8eOmj59ulFz5ufnq7S0VF26dFFgYKACAwO1bt06zZgxQ4GBgYqIiDBm1p8KCwvT73//e3355ZdGPadRUVGKi4vz2NeuXTv7rbnaeX76LSNfnLXWN998o48//lhDhw6195n0nD7xxBPKzMzUoEGD1L59e913330aOXKksrOzJZn3nLZq1Urr1q1TRUWFiouLtWXLFlVXV+uqq64ybtZzQci5QCzLUkZGhpYsWaI1a9YoNjbWY71r165q0KCBVq9ebe8rLCzUgQMHlJCQcKHbrXM1NTWqqqoyas4+ffpo586dKigosLdu3bopNTXV/mdTZv2piooK/fOf/1RUVJRRz2nPnj3PuLTDvn371LJlS0lSbGysIiMjPWZ1u93avHmzz81a66233lLz5s01YMAAe59Jz+n3338vf3/Pl7qAgADV1NRIMvM5laSGDRsqKipKR48e1cqVK3XbbbcZO+u/5e1PPl8qHnnkEcvpdFpr1671+Nrm999/b9c8/PDDVosWLaw1a9ZY27ZtsxISEqyEhAQvdv3rZGZmWuvWrbOKioqsHTt2WJmZmZafn5+1atUqy7LMmfNsTv92lWWZM+vo0aOttWvXWkVFRdbGjRutxMREq1mzZlZpaallWebMuWXLFiswMNCaNGmStX//fmv+/PnWZZddZr399tt2zeTJk62wsDDr/ffft3bs2GHddtttPvsV3FOnTlktWrSwxo4de8aaKc/p4MGDrcsvv9z+Cvl7771nNWvWzBozZoxdY9JzmpOTY3300UfWV199Za1atcrq2LGjFR8fb504ccKyLLNmPReEnAtE0lm3t956y6754YcfrD//+c9WkyZNrMsuu8y6/fbbrW+//dZ7Tf9KQ4YMsVq2bGkFBQVZv/vd76w+ffrYAceyzJnzbH4ackyZdeDAgVZUVJQVFBRkXX755dbAgQM9rh1jypyWZVkffPCBdc0111jBwcFW27ZtrdmzZ3us19TUWE899ZQVERFhBQcHW3369LEKCwu91O1vs3LlSkvSWfs35Tl1u93W8OHDrRYtWlghISHWVVddZY0fP96qqqqya0x6ThcuXGhdddVVVlBQkBUZGWmlp6dbZWVl9rpJs54LP8s67bKPAAAAhuAzOQAAwEiEHAAAYCRCDgAAMBIhBwAAGImQAwAAjETIAQAARiLkAAAAIxFyAACAkQg5AHxKXl6eAgICPH5rCQDOhiseA/ApQ4cOVaNGjTRnzhwVFhYqOjra2y0BuEhxJgeAz6ioqNDChQv1yCOPaMCAAZo7d67H+rJly9S6dWuFhIToxhtv1Lx58+Tn56eysjK7ZsOGDerVq5dCQ0MVExOjxx57TJWVlRd2EAAXBCEHgM9YtGiR2rZtqzZt2ujee+/Vf//3f6v2ZHRRUZHuvPNOJScn6/PPP9dDDz2k8ePHe9z/n//8p/r166eUlBTt2LFDCxcu1IYNG5SRkeGNcQDUM96uAuAzevbsqbvuukvDhw/XyZMnFRUVpcWLF+uGG25QZmamVqxYoZ07d9r1Tz75pCZNmqSjR48qLCxMQ4cOVUBAgP72t7/ZNRs2bNAf//hHVVZWKiQkxBtjAagnnMkB4BMKCwu1ZcsW3X333ZKkwMBADRw4UHPmzLHXu3fv7nGfa6+91uP2559/rrlz56pRo0b2lpSUpJqaGhUVFV2YQQBcMIHebgAAzsWcOXN08uRJjw8aW5al4OBgvfrqq+d0jIqKCj300EN67LHHzlhr0aJFnfUK4OJAyAFw0Tt58qT+53/+R9OmTVPfvn091pKTk/XOO++oTZs2+vDDDz3Wtm7d6nG7S5cu+uKLL3T11VfXe88AvI/P5AC46C1dulQDBw5UaWmpnE6nx9rYsWO1Zs0aLVq0SG3atNHIkSOVlpamgoICjR49WgcPHlRZWZmcTqd27NihHj16aMiQIRo6dKgaNmyoL774Qrm5ued8NgiA7+AzOQAuenPmzFFiYuIZAUeSUlJStG3bNh07dkx///vf9d5776lDhw6aOXOm/e2q4OBgSVKHDh20bt067du3T7169VLnzp2VlZXFtXYAQ3EmB4CxJk2apFmzZqm4uNjbrQDwAj6TA8AYr7/+urp3767w8HBt3LhRU6dO5Ro4wCWMkAPAGPv379dzzz2nI0eOqEWLFho9erTGjRvn7bYAeAlvVwEAACPxwWMAAGAkQg4AADASIQcAABiJkAMAAIxEyAEAAEYi5AAAACMRcgAAgJEIOQAAwEiEHAAAYKT/Bzvk3rRdUSXiAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import kagglehub\n",
    "import os\n",
    "import tqdm\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as pl\n",
    "\n",
    "\n",
    "\n",
    "# Download latest version\n",
    "data_path = kagglehub.dataset_download(\"aakashverma8900/portuguese-bank-marketing\")\n",
    "\n",
    "# Encontrar o arquivo CSV dentro do diretório baixado\n",
    "csv_file = [f for f in os.listdir(data_path) if f.endswith(\".csv\")][0]  # Pega o primeiro CSV encontrado\n",
    "\n",
    "# Criar o caminho completo do arquivo\n",
    "csv_path = os.path.join(data_path, csv_file)\n",
    "\n",
    "# Carregar o CSV no Pandas\n",
    "df = pd.read_csv(csv_path, delimiter=\",\")\n",
    "\n",
    "# 3 MÉTODOS MAIS UTILIZADOS NOS OBJETOS E NOS INTEIROS\n",
    "# OBJETOS --> str.lower(PASSA PARA MINUSCULO)\n",
    "#         --> str.upper(PASSA PARA MAIUSCULO)\n",
    "#         --> str.contains(RETORNA TRUE SE ENCONTRAR A PALAVRA)\n",
    "#         --> str.len(CRIA UMA NOVA COLUNA COM O TAMANHO DAS STRINGS)\n",
    "\n",
    "#INT64 --> .sum(SOMA TODOS OS VALORES INTEIROS DA COLUNA)\n",
    "#      --> .mean(RETIRA A MÉDIA DA COLUNA)\n",
    "#      --> .describe(ESTATÍTICA DESCRITIVA)\n",
    "\n",
    "\n",
    "\n",
    "print(\"Path to dataset files:\", csv_path)\n",
    "#df.head()\n",
    "df.info()\n",
    "print(\"\\n\")\n",
    "#print(df[\"Age\"].describe())\n",
    "#df[\"Job\"] = df[\"Job\"].str.upper()\n",
    "#print(df[\"Job\"].str.contains(\"management\"))\n",
    "#print(df[\"Age\"].sum())\n",
    "#print(df[\"Job\"])\n",
    "\n",
    "\n",
    "# VISUALIÇÃO\n",
    "pl.hist(df['Age'], bins=10, color='skyblue')\n",
    "pl.xlabel('Age')\n",
    "pl.title('Job')\n",
    "pl.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4185ad57-5806-4ab9-9322-6a6f53b6fdd0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
