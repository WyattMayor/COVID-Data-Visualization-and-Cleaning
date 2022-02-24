import pandas as pd

Confirmed = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_confirmed_usafacts.csv')
County = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_county_population_usafacts.csv')
Deaths = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_deaths_usafacts.csv')

print (Confirmed)
#Confirmed = pd.DataFrame([[0,4],[0,2]], index=['date', 'countyFIPS', 'County Name', 'State'], columns=[ 'StateFIPS','Total cases/deaths'])
#Confirmed = comfirmed.
#Confirmed = Confirmed.reset_index()
Confirmed = Confirmed.set_index(['countyFIPS', 'County Name', 'State', 'StateFIPS'])
confirmed = Confirmed.stack()
confirmed = confirmed.to_frame('Total Cases')
confirmed = confirmed.reset_index()
Renamed = confirmed.rename(columns={"level_4": "dates"})
Renamed['dates'] = pd.to_datetime(Renamed["dates"])
Renamed = Renamed.set_index(['dates', 'State', 'County Name', 'countyFIPS'])
#Confirmed = Confirmed.stack()
#Confirmed = Confirmed.set_index(['dates','countyFIPS', 'County Name', 'State'])