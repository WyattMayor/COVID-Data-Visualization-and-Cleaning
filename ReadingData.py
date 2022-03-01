import pandas as pd
import plotly.express as px
import plotly.io as pio



###Stage 1


###Reading in csv to convert it into dataframe we can use
pio.renderers.default = "browser"
Confirmed = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_confirmed_usafacts.csv')
County = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_county_population_usafacts.csv')
Deaths = pd.read_csv(r'/Users/wyattmayor/Comp240/CovidGraphs/covid_deaths_usafacts.csv')

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
### Using the groupby function to group the states then the dates together and add up the cases
GroupStateThenDate = df.groupby(["State","dates"])['Total Cases'].sum()
### Graph that shows how the cases rise over time
DateTotalCases = px.area(GroupDate, x= 'dates', y="Total Cases")
DateTotalCases.show()


###Stage 3


NewCases = CountyF.groupby(["dates"])['Total Cases'].diff()

###Stage 4

