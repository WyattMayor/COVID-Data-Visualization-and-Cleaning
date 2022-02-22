import pandas as pd

Comfirmed = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_confirmed_usafacts.csv')
County = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_county_population_usafacts.csv')
Deaths = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_deaths_usafacts.csv')

print (Comfirmed)
