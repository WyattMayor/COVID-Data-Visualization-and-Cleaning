import pandas as pd
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go



###Stage 1


###Reading in csv to convert it into dataframe we can use
pio.renderers.default = "browser"
Confirmed = pd.read_csv(r'C:/Users/Colto/CovidGraphs/covid_confirmed_usafacts.csv')
County = pd.read_csv(r'C:/Users/Colto/CovidGraphs/covid_county_population_usafacts.csv')
Deaths = pd.read_csv(r'C:/Users/Colto/CovidGraphs/covid_deaths_usafacts.csv')

### Adding columns to Index
IndexReset = Confirmed.set_index(['countyFIPS', 'County Name', 'State', 'StateFIPS'])
### stacking non index colums into one column (dates)
StackedDates = IndexReset.stack()
### Turning the stacked series back into dataframe
TotalCasesColumn = StackedDates.to_frame('Total Cases')
### moving all colums out of the index
IndexReworked = TotalCasesColumn.reset_index()
###renaming the stacked column to dates
df = IndexReworked.rename(columns={"level_4": "dates"})
df['dates'] = pd.to_datetime(df["dates"])
### only shows entries that have a county fips 1001
CountyF = df[df['countyFIPS'] == 1001]


###Stage 2


### Using the groupby function to group the dates together and add up the cases
GroupDate = df.groupby(["dates"])['Total Cases'].sum()
GroupDate = GroupDate.to_frame()
GroupDate = GroupDate.reset_index()
USADateTotal = px.area(GroupDate, x= 'dates', y="Total Cases", title='Total USA Cases')
USADateTotal.show()

CountyF = df[df['countyFIPS'] == 17095]
CountyFDate = CountyF.groupby(["dates"])['Total Cases'].sum()
CountyFDate = CountyFDate.to_frame()
CountyFDate = CountyFDate.reset_index()
CountyGraph = px.area(CountyFDate, x= 'dates', y="Total Cases", title='Total Knox County Cases')
CountyGraph.show()



StateName = df[df['State'] == 'IL']
StateGroupDates = StateName.groupby(["dates"])['Total Cases'].sum()
StateGroupDates = StateGroupDates.to_frame()
StateGroupDates = StateGroupDates.reset_index()
IllinoisCases = px.area(StateGroupDates, x= 'dates', y="Total Cases", title='Total Illinois Cases')
IllinoisCases.show()





###SubPlots

#Covidillinois = make_subplots(rows=1, cols=2)
#Covidillinois.plt.





### Using the groupby function to group the states then the dates together and add up the cases
GroupStateThenDate = df.groupby(["State","dates"])['Total Cases'].sum()
GroupStateThenDate = GroupStateThenDate.to_frame()
GroupStateThenDate= GroupStateThenDate.reset_index()
# ### Graph that shows how the cases rise over time
DateTotalCases = px.area(GroupDate, x= 'dates', y="Total Cases", title='Total Autauga County Cases')
DateTotalCases.show()


###Stage 3
CoF = CountyFDate
CoF = CoF.set_index(['dates'])
CoFDate = CoF['Total Cases'].diff()
CoFNew = CoFDate.to_frame()
CoFNew = CoFNew.reset_index()
CoFNew = CoFNew.rename(columns = {"Total Cases": "New Cases"})
CoFNew = CoFNew.reset_index()
CountyGraph = px.bar(CoFNew, x= 'dates', y="New Cases", title='New Knox County Cases Per Day')
CountyGraph.show()

StoF = StateGroupDates
StoF = StoF.set_index(['dates'])
StoFDate = StoF['Total Cases'].diff()
StoFNew = StoFDate.to_frame()
StoFNew = StoFNew.reset_index()
StoFNew = StoFNew.rename(columns = {"Total Cases": "New Cases"})
StoFNew = StoFNew.reset_index()
ILGraph = px.bar(StoFNew, x= 'dates', y="New Cases", title='New IL Cases Per Day')
ILGraph.show()

USAoF = GroupDate
USAoF = USAoF.set_index(['dates'])
USAoFDate = USAoF['Total Cases'].diff()
USAoFNew = USAoFDate.to_frame()
USAoFNew = USAoFNew.reset_index()
USAoFNew = USAoFNew.rename(columns = {"Total Cases": "New Cases"})
USAoFNew = USAoFNew.reset_index()
ILGraph = px.bar(USAoFNew, x= 'dates', y="New Cases", title='New USA Cases Per Day')
ILGraph.show()
# ###Stage 4

