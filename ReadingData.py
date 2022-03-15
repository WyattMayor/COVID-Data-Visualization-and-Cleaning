import pandas as pd
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

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

CoF = df[df['countyFIPS'] == 17095]
CoF = CoF.set_index(['dates','countyFIPS', 'County Name', 'State', 'StateFIPS'])
CoFDate = CoF['Total Cases'].diff()
CoFNew = CoFDate.to_frame()
CoFNew = CoFNew.reset_index()
CoFNew = CoFNew.rename(columns = {"Total Cases": "New Cases"})
CoFNew = CoFNew.reset_index()
CountyGraph = px.bar(CoFNew, x= 'dates', y="New Cases", title='New Knox County Cases Per Day')
CountyGraph.show()

StateName = df[df['State'] == 'IL']
StateGroupDates = StateName.groupby(["dates"])['Total Cases'].sum()
StateGroupDates = StateGroupDates.to_frame()
StateGroupDates = StateGroupDates.reset_index()
#IllinoisCases = px.area(StateGroupDates, x= 'dates', y="Total Cases", title='Total Illinois Cases')
#IllinoisCases.show()


###Plots combined
TotalCasesEach = go.Figure()
TotalCasesEach.add_trace(go.Scatter(x=GroupDate["dates"],y=GroupDate["Total Cases"],name='USA'))
TotalCasesEach.add_trace(go.Scatter(x=StateGroupDates["dates"],y=StateGroupDates["Total Cases"],name='Illinois'))
TotalCasesEach.add_trace(go.Scatter(x=CountyFDate["dates"],y=CountyFDate["Total Cases"],name='Knox County'))
TotalCasesEach.update_layout(
    title= 'Total Cases',
    yaxis_title="Number of Cases",
    xaxis_title="days",
    legend_title='Names')
TotalCasesEach.show()

StoF = df[df['State'] == 'IL']
StoF = StoF.set_index(['dates','countyFIPS', 'County Name', 'State', 'StateFIPS'])
StoFDate = StoF['Total Cases'].diff()
StoFNew = StoFDate.to_frame()
StoFNew = StoFNew.reset_index()
StoFNew = StoFNew.rename(columns = {"Total Cases": "New Cases"})
StoFNew = StoFNew.reset_index()
ILGraph = px.bar(StoFNew, x= 'dates', y="New Cases", title='New IL Cases Per Day')
ILGraph.show()

USAoF = df
USAoF = USAoF.set_index(['dates','countyFIPS', 'County Name', 'State', 'StateFIPS'])
USAoFDate = USAoF['Total Cases'].diff()
USAoFNew = USAoFDate.to_frame()
USAoFNew = USAoFNew.reset_index()
USAoFNew = USAoFNew.rename(columns = {"Total Cases": "New Cases"})
USAoFNew = USAoFNew.reset_index()
ILGraph = px.bar(USAoFNew, x= 'dates', y="New Cases", title='New USA Cases Per Day')
ILGraph.show()

###SubPlots
TotalCasesSep = make_subplots(rows=1,cols=3,
                              subplot_titles=("USA Total Cases","IL Total Cases", "Knox County Total Cases"))
TotalCasesSep.add_trace(go.Scatter(x=GroupDate["dates"],y=GroupDate["Total Cases"],name='USA'),row=1, col=1)
TotalCasesSep.add_trace(go.Scatter(x=StateGroupDates["dates"],y=StateGroupDates["Total Cases"],name='Illinois'),row=1, col=2)
TotalCasesSep.add_trace(go.Scatter(x=CountyFDate["dates"],y=CountyFDate["Total Cases"],name='Knox County'),row=1, col=3)
TotalCasesSep.update_layout(
    legend_title='Names')
TotalCasesSep.show()


### Using the groupby function to group the states then the dates together and add up the cases
GroupStateThenDate = df.groupby(["State","dates"])['Total Cases'].sum()
GroupStateThenDate = GroupStateThenDate.to_frame()
GroupStateThenDate= GroupStateThenDate.reset_index()
### Graph that shows how the cases rise over time

# ### Graph that shows how the cases rise over time

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


###Plots combined
NewCasesEachDay = go.Figure()
NewCasesEachDay.add_trace(go.Scatter(x=USAoFNew["dates"],y=USAoFNew["New Cases"],name='USA'))
NewCasesEachDay.add_trace(go.Scatter(x=StoFNew["dates"],y=StoFNew["New Cases"],name='Illinois'))
NewCasesEachDay.add_trace(go.Scatter(x=CoFNew["dates"],y=CoFNew["New Cases"],name='Knox County'))
NewCasesEachDay.update_layout(
    title= 'New Cases Per Day',
    yaxis_title="Number of Cases",
    xaxis_title="days",
    legend_title='Names')
NewCasesEachDay.show()

###SubPlots
NewCasesEachDay2 = make_subplots(rows=3,cols=1,
                              subplot_titles=("USA Total Cases","IL Total Cases", "Knox County Total Cases"))
NewCasesEachDay2.add_trace(go.Scatter(x=USAoFNew["dates"],y=USAoFNew["New Cases"],name='USA'),row=1, col=1)
NewCasesEachDay2.add_trace(go.Scatter(x=StoFNew["dates"],y=StoFNew["New Cases"],name='Illinois'),row=2, col=1)
NewCasesEachDay2.add_trace(go.Scatter(x=CoFNew["dates"],y=CoFNew["New Cases"],name='Knox County'),row=3, col=1)
NewCasesEachDay2.update_layout(
    legend_title='Names')
NewCasesEachDay2.show()


# ###Stage 4




