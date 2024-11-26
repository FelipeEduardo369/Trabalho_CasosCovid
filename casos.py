import pandas as pd
import matplotlib.pyplot as plt

# URL do arquivo CSV
url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"

# Carregar os dados diretamente do CSV
covid_data = pd.read_csv(url)

# Renomear colunas para facilitar o manuseio (já fornecidas corretamente)
covid_data.columns = covid_data.columns.str.lower()

# Agrupar os dados por estado
state_group = covid_data.groupby('state').sum()

# Identificar cidades e estados com mais/menos casos e mortes
city_most_cases = covid_data.loc[covid_data['totalcases'].idxmax()]
city_least_cases = covid_data.loc[covid_data['totalcases'].idxmin()]
city_most_deaths = covid_data.loc[covid_data['deaths'].idxmax()]
city_least_deaths = covid_data.loc[covid_data['deaths'].idxmin()]

state_most_cases = state_group.loc[state_group['totalcases'].idxmax()]
state_least_cases = state_group.loc[state_group['totalcases'].idxmin()]
state_most_deaths = state_group.loc[state_group['deaths'].idxmax()]
state_least_deaths = state_group.loc[state_group['deaths'].idxmin()]

# Totais de casos e mortes no Brasil
total_cases_brazil = state_group['totalcases'].sum()
total_deaths_brazil = state_group['deaths'].sum()

# Dados para os gráficos
top5_states_deaths = state_group.nlargest(5, 'deaths').reset_index()
bottom5_states_deaths = state_group.nsmallest(5, 'deaths').reset_index()

# Gerar gráficos
plt.figure(figsize=(10, 6))
plt.bar(top5_states_deaths['state'], top5_states_deaths['deaths'], color='red')
plt.title('Top 5 Estados com Mais Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(bottom5_states_deaths['state'], bottom5_states_deaths['deaths'], color='blue')
plt.title('Top 5 Estados com Menos Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

# Resultados resumidos
summary = {
    "Cidade com Mais Casos": city_most_cases[['city', 'totalcases']].to_dict(),
    "Cidade com Menos Casos": city_least_cases[['city', 'totalcases']].to_dict(),
    "Estado com Mais Casos": {"state": state_group['totalcases'].idxmax(), "cases": state_most_cases['totalcases']},
    "Estado com Menos Casos": {"state": state_group['totalcases'].idxmin(), "cases": state_least_cases['totalcases']},
    "Cidade com Mais Mortes": city_most_deaths[['city', 'deaths']].to_dict(),
    "Cidade com Menos Mortes": city_least_deaths[['city', 'deaths']].to_dict(),
    "Estado com Mais Mortes": {"state": state_group['deaths'].idxmax(), "deaths": state_most_deaths['deaths']},
    "Estado com Menos Mortes": {"state": state_group['deaths'].idxmin(), "deaths": state_least_deaths['deaths']},
    "Total de Casos no Brasil": total_cases_brazil,
    "Total de Mortes no Brasil": total_deaths_brazil
}

# Exibir o resumo
print(summary)