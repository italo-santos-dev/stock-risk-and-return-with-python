import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Tickers das ações
tickers = ['BBDC3.SA', 'SANB11.SA']

sec_data = pd.DataFrame()

for t in tickers:
    try:
        sec_data[t] = yf.download(t, start='2010-01-01')['Adj Close']
    except Exception as e:
        print(f"Não foi possível recuperar os dados para {t}: {e}")

sec_returns = np.log(sec_data / sec_data.shift(1))

returnAnnual = sec_returns.mean() * 250

returnAnnualStandardDeviation = sec_returns.std() * np.sqrt(250)

print("Retorno Anual Médio (%):")
print(returnAnnual.apply(lambda x: f'{x*100:.2f}%'))

print("Desvio Padrão Anual (%):")
print(returnAnnualStandardDeviation.apply(lambda x: f'{x*100:.2f}%'))

plt.figure(figsize=(14, 7))
for t in tickers:
    sec_data[t].plot(label=t)
plt.title('Preços Ajustados de Fechamento')
plt.xlabel('Data')
plt.ylabel('Preço Ajustado de Fechamento')
plt.legend()
plt.show()

plt.figure(figsize=(14, 7))
for t in tickers:
    sec_returns[t].plot(label=t)
plt.title('Retornos Logarítmicos Diários')
plt.xlabel('Data')
plt.ylabel('Retorno Logarítmico Diário')
plt.legend()
plt.show()
