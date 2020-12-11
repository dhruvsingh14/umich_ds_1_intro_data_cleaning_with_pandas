#####################################
# Assignment 4: Statistical Testing #
#####################################
# libraries
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

###################
# Question 1: NHL #
###################
# nhl win loss data
nhl_df = pd.read_csv("data/nhl.csv")
# cities population data
cities=pd.read_html("data/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nhl_correlation():
    # nhl win loss data
    global nhl_df
    # restricting to 2018
    nhl_df = nhl_df[nhl_df['year'] == 2018]
    # subsetting columns
    nhl_df = nhl_df[['team', 'W', 'L']]
    # converting to numeric
    nhl_df['W'] = pd.to_numeric(nhl_df['W'], errors='coerce')
    nhl_df['L'] = pd.to_numeric(nhl_df['L'], errors='coerce')
    nhl_df['team'] = nhl_df['team'].str.replace('*', '')
    # dropping rows with a NaN for an entry
    nhl_df = nhl_df[nhl_df['W'].notna()]
    # extracting team names
    nhl_df['team_name'] = nhl_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    nhl_df['team_name'] = nhl_df['team_name'].str.replace('Bay |Jersey ', '')
    nhl_df['team_name'] = nhl_df['team_name'].str.replace('York | Louis ', '')
    nhl_df['team_name'] = nhl_df['team_name'].str.replace('Jose | Angeles ', '')
    # trimming leading whitespaces for consistency in grouping
    nhl_df['team_name'] = nhl_df['team_name'].str.lstrip()
    # combining metropolitan teams into 1
    nhl_df['team_name'] = nhl_df['team_name'].str.replace('Kings|Ducks', 'KingsDucks')
    nhl_df['team_name'] = nhl_df['team_name'].str.replace('Rangers|Islanders|Devils', 'RangersIslandersDevils')
    # win loss ratios before collapsing rows
    nhl_df['win_loss_ratio'] = (nhl_df['W'])/(nhl_df['W']+nhl_df['L'])
    # setting team names to index, for merge
    nhl_df = nhl_df.groupby("team_name").agg({"win_loss_ratio":(np.nanmean)})

    # cities population data
    global cities
    # dropping non nhl columns
    cities = cities.drop(['NFL', 'MLB', 'NBA'], axis=1)
    # renaming population column
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    # changing population to numeric
    cities['Population'] = pd.to_numeric(cities['Population'])
    # dropping rows with a dash for an entry
    cities = cities[cities['NHL'] != '—']
    # replacing bracket characters with blank
    cities['NHL'] = cities['NHL'].str.replace('\[.*\]', '')
    cities = cities[cities['NHL'] != '']
    cities = cities.sort_values(by='NHL')
    cities = cities.set_index('NHL')

    # merging two datasets
    nhl_combined = pd.merge(nhl_df, cities, how='inner', left_index=True, right_index=True)

    # creating series / vectors
    population_by_region = nhl_combined['Population']
    win_loss_by_region = nhl_combined['win_loss_ratio']

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    # returning correlation coefficient, and p-value
    return stats.pearsonr(population_by_region, win_loss_by_region)
    raise NotImplementedError()

###################
# Question 2: NBA #
###################
# nba win loss data
nba_df = pd.read_csv("data/nba.csv")
# cities population data
cities=pd.read_html("data/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nba_correlation():
    # nba win loss data
    global nba_df
    # restricting to 2018
    nba_df = nba_df[nba_df['year'] == 2018]
    # subsetting columns
    nba_df = nba_df[['team', 'W/L%']]
    nba_df['W/L%'] = pd.to_numeric(nba_df['W/L%'], errors='coerce')
    # extracting team names
    nba_df['team_name'] = nba_df.team.str.extract('((?=\s).*(?<=\())')
    # standardizing strings to include team names, without city
    nba_df['team_name'] = nba_df['team_name'].str.replace('York|State|City|Orleans|Antonio|Angeles', '')
    nba_df['team_name'] = nba_df['team_name'].str.replace('\(|\*', '')
    # trimming leading whitespaces for consistency in grouping
    nba_df['team_name'] = nba_df['team_name'].str.lstrip()
    nba_df['team_name'] = nba_df['team_name'].str.rstrip()
    # combining metropolitan teams into 1
    nba_df['team_name'] = nba_df['team_name'].str.replace('Clippers|Lakers', 'LakersClippers')
    nba_df['team_name'] = nba_df['team_name'].str.replace('Knicks|Nets', 'KnicksNets')
    # setting team names to index, for merge
    nba_df = nba_df.groupby("team_name").agg({"W/L%":(np.nanmean)})

    # cities population data
    global cities
    # dropping non nba columns
    cities = cities.drop(['NFL', 'MLB', 'NHL'], axis=1)
    # renaming population column
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    # changing population to numeric
    cities['Population'] = pd.to_numeric(cities['Population'])
    # dropping rows with a dash for an entry
    cities = cities[cities['NBA'] != '—']
    # replacing bracket characters with blank
    cities['NBA'] = cities['NBA'].str.replace('\[.*\]', '')
    cities = cities[cities['NBA'] != '']
    cities = cities.sort_values(by='NBA')
    cities = cities.set_index('NBA')

    # merging two datasets
    nba_combined = pd.merge(nba_df, cities, how='inner', left_index=True, right_index=True)
    # creating series / vectors
    population_by_region = nba_combined['Population']
    win_loss_by_region = nba_combined['W/L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    # returning correlation coefficient, and p-value
    return stats.pearsonr(population_by_region, win_loss_by_region)
    raise NotImplementedError()

###################
# Question 3: MLB #
###################
# mlb win loss data
mlb_df = pd.read_csv("data/mlb.csv")
# cities population data
cities=pd.read_html("data/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def mlb_correlation():
    # mlb win loss data
    global mlb_df
    # restricting to 2018
    mlb_df = mlb_df[mlb_df['year'] == 2018]
    # subsetting columns
    mlb_df = mlb_df[['team', 'W-L%']]
    mlb_df['W-L%'] = pd.to_numeric(mlb_df['W-L%'], errors='coerce')
    # extracting team names
    mlb_df['team_name'] = mlb_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    mlb_df['team_name'] = mlb_df['team_name'].str.replace('York|Bay|City|Angeles|Louis|Francisco|Diego', '')
    # trimming leading whitespaces for consistency in grouping
    mlb_df['team_name'] = mlb_df['team_name'].str.lstrip()
    mlb_df['team_name'] = mlb_df['team_name'].str.rstrip()
    # combining metropolitan teams into 1
    mlb_df['team_name'] = mlb_df['team_name'].str.replace('Yankees|Mets', 'YankeesMets')
    mlb_df['team_name'] = mlb_df['team_name'].str.replace('Dodgers|Angels', 'DodgersAngels')
    mlb_df['team_name'] = mlb_df['team_name'].str.replace('Giants|Athletics', 'GiantsAthletics')
    mlb_df['team_name'] = mlb_df['team_name'].str.replace('Cubs|White Sox', 'CubsWhite Sox')
    # setting team names to index, for merge
    mlb_df = mlb_df.groupby("team_name").agg({"W-L%":(np.nanmean)})

    # cities population data
    global cities
    # dropping non mlb columns
    cities = cities.drop(['NFL', 'NBA', 'NHL'], axis=1)
    # renaming population column
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    # changing population to numeric
    cities['Population'] = pd.to_numeric(cities['Population'])
    # dropping rows with a dash for an entry
    cities = cities[cities['MLB'] != '—']
    # replacing bracket characters with blank
    cities['MLB'] = cities['MLB'].str.replace('\[.*\]', '')
    cities = cities[cities['MLB'] != '']
    cities = cities.sort_values(by='MLB')
    cities = cities.set_index('MLB')

    # merging two datasets
    mlb_combined = pd.merge(mlb_df, cities, how='inner', left_index=True, right_index=True)
    # creating series / vectors
    population_by_region = mlb_combined['Population']
    win_loss_by_region = mlb_combined['W-L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    # returning correlation coefficient, and p-value
    return stats.pearsonr(population_by_region, win_loss_by_region)
    raise NotImplementedError()

###################
# Question 4: NFL #
###################
# nfl win loss data
nfl_df = pd.read_csv("data/nfl.csv")
# cities population data
cities=pd.read_html("data/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nfl_correlation():
    # nfl win loss data
    global nfl_df
    # restricting to 2018
    nfl_df = nfl_df[nfl_df['year'] == 2018]
    # subsetting columns
    nfl_df = nfl_df[['team', 'W-L%']]
    nfl_df['W-L%'] = pd.to_numeric(nfl_df['W-L%'], errors='coerce')
    nfl_df['team'] = nfl_df.team.str.extract('(.*\w)')
    # dropping rows with a NaN for an entry
    nfl_df = nfl_df[nfl_df['W-L%'].notna()]
    # extracting team names
    nfl_df['team_name'] = nfl_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    nfl_df['team_name'] = nfl_df['team_name'].str.replace('England|City|Angeles|York|Bay|Orleans|Francisco', '')
    # trimming leading whitespaces for consistency in grouping
    nfl_df['team_name'] = nfl_df['team_name'].str.lstrip()
    nfl_df['team_name'] = nfl_df['team_name'].str.rstrip()
    # combining metropolitan teams into 1
    nfl_df['team_name'] = nfl_df['team_name'].str.replace('Giants|Jets', 'GiantsJets')
    nfl_df['team_name'] = nfl_df['team_name'].str.replace('Rams|Chargers', 'RamsChargers')
    nfl_df['team_name'] = nfl_df['team_name'].str.replace('49ers|Raiders', '49ersRaiders')
    # setting team names to index, for merge
    nfl_df = nfl_df.groupby("team_name").agg({"W-L%":(np.nanmean)})

    # cities population data
    global cities
    # dropping non nfl columns
    cities = cities.drop(['MLB', 'NBA', 'NHL'], axis=1)
    # renaming population column
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    # changing population to numeric
    cities['Population'] = pd.to_numeric(cities['Population'])
    # replacing bracket characters with blank
    cities['NFL'] = cities['NFL'].str.replace('\[.*\]', '')
    # dropping rows with a dash for an entry
    cities = cities[cities['NFL'] != '—']
    cities = cities[cities['NFL'] != '— '] # could've done rtrim for toronto, better practice
    cities = cities[cities['NFL'] != '']
    cities = cities.sort_values(by='NFL')
    cities = cities.set_index('NFL')

    # merging two datasets
    nfl_combined = pd.merge(nfl_df, cities, how='inner', left_index=True, right_index=True)
    # creating series / vectors
    population_by_region = nfl_combined['Population']
    win_loss_by_region = nfl_combined['W-L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 26 teams being analysed for NFL"

    # returning correlation coefficient, and p-value
    return stats.pearsonr(population_by_region, win_loss_by_region)
    raise NotImplementedError()

######################
# Question 5: TTests #
######################
# ttesting win loss data
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

# sports team win loss data
mlb_df = pd.read_csv("data/mlb.csv")
nhl_df = pd.read_csv("data/nhl.csv")
nba_df = pd.read_csv("data/nba.csv")
nfl_df = pd.read_csv("data/nfl.csv")
# cities population data
cities=pd.read_html("data/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def sports_team_performance():

    #### SPORT 1: NHL

    # nhl win loss data
    global nhl_df
    # restricting to 2018
    nhl_df = nhl_df[nhl_df['year'] == 2018]
    # subsetting columns
    nhl_df = nhl_df[['team', 'W', 'L']]
    # converting to numeric
    nhl_df['W'] = pd.to_numeric(nhl_df['W'], errors='coerce')
    nhl_df['L'] = pd.to_numeric(nhl_df['L'], errors='coerce')
    nhl_df['team'] = nhl_df['team'].str.replace('*', '')
    # dropping rows with a NaN for an entry
    nhl_df = nhl_df[nhl_df['W'].notna()]
    # extracting team names
    nhl_df['NHL'] = nhl_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    nhl_df['NHL'] = nhl_df['NHL'].str.replace('Bay |Jersey ', '')
    nhl_df['NHL'] = nhl_df['NHL'].str.replace('York | Louis ', '')
    nhl_df['NHL'] = nhl_df['NHL'].str.replace('Jose | Angeles ', '')
    # trimming leading whitespaces for consistency in grouping
    nhl_df['NHL'] = nhl_df['NHL'].str.lstrip()
    # combining metropolitan teams into 1
    nhl_df['NHL'] = nhl_df['NHL'].str.replace('Kings|Ducks', 'KingsDucks')
    nhl_df['NHL'] = nhl_df['NHL'].str.replace('Rangers|Islanders|Devils', 'RangersIslandersDevils')
    # win loss ratios before collapsing rows
    nhl_df['NHL_W/L%'] = (nhl_df['W'])/(nhl_df['W']+nhl_df['L'])
    # setting team names to index, for merge
    nhl_df = nhl_df.groupby("NHL").agg({"NHL_W/L%":(np.nanmean)})

    #### CITIES DATA

    # cities population data
    global cities
    # renaming population column
    cities = cities.rename(columns={'Population (2016 est.)[8]': 'Population'})
    # changing population to numeric
    cities['Population'] = pd.to_numeric(cities['Population'])
    # replacing bracket characters with blank
    cities['NHL'] = cities['NHL'].str.replace('\[.*\]', '')
    cities['NFL'] = cities['NFL'].str.replace('\[.*\]', '')
    cities['NFL'] = cities['NFL'].str.replace(' ', '') # for toronto
    cities['MLB'] = cities['MLB'].str.replace('\[.*\]', '')
    cities['NBA'] = cities['NBA'].str.replace('\[.*\]', '')

    # filling in NaNs for missing values
    cities['NHL'] = cities['NHL'].replace('—', np.NaN)
    cities['NFL'] = cities['NFL'].replace('—', np.NaN)
    cities['MLB'] = cities['MLB'].replace('—', np.NaN)
    cities['NBA'] = cities['NBA'].replace('—', np.NaN)

    cities['NHL'] = cities['NHL'].replace('', np.NaN)
    cities['NFL'] = cities['NFL'].replace('', np.NaN)
    cities['MLB'] = cities['MLB'].replace('', np.NaN)
    cities['NBA'] = cities['NBA'].replace('', np.NaN)
    cities = cities.sort_values(by='NHL')
    cities = cities.set_index('NHL')

    # merging two datasets: NHL and Cities
    nhl_combined = pd.merge(nhl_df, cities, how='outer', left_index=True, right_index=True)
    nhl_combined = nhl_combined.reset_index()
    nhl_combined = nhl_combined.sort_values(by='NBA')
    nhl_combined = nhl_combined.set_index('NBA')


    ##### SPORT 2: NBA

    # nba win loss data
    global nba_df
    # restricting to 2018
    nba_df = nba_df[nba_df['year'] == 2018]
    # subsetting columns
    nba_df = nba_df[['team', 'W/L%']]
    nba_df = nba_df.rename(columns={'W/L%': 'NBA_W/L%'})
    nba_df['NBA_W/L%'] = pd.to_numeric(nba_df['NBA_W/L%'], errors='coerce')
    # extracting team names
    nba_df['NBA'] = nba_df.team.str.extract('((?=\s).*(?<=\())')
    # standardizing strings to include team names, without city
    nba_df['NBA'] = nba_df['NBA'].str.replace('York|State|City|Orleans|Antonio|Angeles', '')
    nba_df['NBA'] = nba_df['NBA'].str.replace('\(|\*', '')
    # trimming leading whitespaces for consistency in grouping
    nba_df['NBA'] = nba_df['NBA'].str.lstrip()
    nba_df['NBA'] = nba_df['NBA'].str.rstrip()
    # combining metropolitan teams into 1
    nba_df['NBA'] = nba_df['NBA'].str.replace('Clippers|Lakers', 'LakersClippers')
    nba_df['NBA'] = nba_df['NBA'].str.replace('Knicks|Nets', 'KnicksNets')
    # setting team names to index, for merge
    nba_df = nba_df.groupby("NBA").agg({"NBA_W/L%":(np.nanmean)})

    # merging two datasets: NBA and NHL+Cities
    nhl_nba_combined = pd.merge(nba_df, nhl_combined, how='outer', left_index=True, right_index=True)
    nhl_nba_combined = nhl_nba_combined.reset_index()
    nhl_nba_combined = nhl_nba_combined.sort_values(by='MLB')
    nhl_nba_combined = nhl_nba_combined.set_index('MLB')


    ##### SPORT 3: MLB

    # mlb win loss data
    global mlb_df
    # restricting to 2018
    mlb_df = mlb_df[mlb_df['year'] == 2018]
    # subsetting columns
    mlb_df = mlb_df[['team', 'W-L%']]
    mlb_df = mlb_df.rename(columns={'W-L%': 'MLB_W/L%'})
    mlb_df['MLB_W/L%'] = pd.to_numeric(mlb_df['MLB_W/L%'], errors='coerce')
    # extracting team names
    mlb_df['MLB'] = mlb_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    mlb_df['MLB'] = mlb_df['MLB'].str.replace('York|Bay|City|Angeles|Louis|Francisco|Diego', '')
    # trimming leading whitespaces for consistency in grouping
    mlb_df['MLB'] = mlb_df['MLB'].str.lstrip()
    mlb_df['MLB'] = mlb_df['MLB'].str.rstrip()
    # combining metropolitan teams into 1
    mlb_df['MLB'] = mlb_df['MLB'].str.replace('Yankees|Mets', 'YankeesMets')
    mlb_df['MLB'] = mlb_df['MLB'].str.replace('Dodgers|Angels', 'DodgersAngels')
    mlb_df['MLB'] = mlb_df['MLB'].str.replace('Giants|Athletics', 'GiantsAthletics')
    mlb_df['MLB'] = mlb_df['MLB'].str.replace('Cubs|White Sox', 'CubsWhite Sox')
    # setting team names to index, for merge
    mlb_df = mlb_df.groupby("MLB").agg({"MLB_W/L%":(np.nanmean)})

    # merging two datasets: MLB and NBA+NHL+Cities
    mlb_nhl_nba_combined = pd.merge(mlb_df, nhl_nba_combined, how='outer', left_index=True, right_index=True)
    mlb_nhl_nba_combined = mlb_nhl_nba_combined.reset_index()
    mlb_nhl_nba_combined = mlb_nhl_nba_combined.sort_values(by='NFL')
    mlb_nhl_nba_combined = mlb_nhl_nba_combined.set_index('NFL')


    #### SPORT 4: NFL

    # nfl win loss data
    global nfl_df
    # restricting to 2018
    nfl_df = nfl_df[nfl_df['year'] == 2018]
    # subsetting columns
    nfl_df = nfl_df[['team', 'W-L%']]
    nfl_df = nfl_df.rename(columns={'W-L%': 'NFL_W/L%'})
    nfl_df['NFL_W/L%'] = pd.to_numeric(nfl_df['NFL_W/L%'], errors='coerce')
    nfl_df['team'] = nfl_df.team.str.extract('(.*\w)')
    # dropping rows with a NaN for an entry
    nfl_df = nfl_df[nfl_df['NFL_W/L%'].notna()]
    # extracting team names
    nfl_df['NFL'] = nfl_df.team.str.extract('(\s.*)')
    # standardizing strings to include team names, without city
    nfl_df['NFL'] = nfl_df['NFL'].str.replace('England|City|Angeles|York|Bay|Orleans|Francisco', '')
    # trimming leading whitespaces for consistency in grouping
    nfl_df['NFL'] = nfl_df['NFL'].str.lstrip()
    nfl_df['NFL'] = nfl_df['NFL'].str.rstrip()
    # combining metropolitan teams into 1
    nfl_df['NFL'] = nfl_df['NFL'].str.replace('Giants|Jets', 'GiantsJets')
    nfl_df['NFL'] = nfl_df['NFL'].str.replace('Rams|Chargers', 'RamsChargers')
    nfl_df['NFL'] = nfl_df['NFL'].str.replace('49ers|Raiders', '49ersRaiders')
    # setting team names to index, for merge
    nfl_df = nfl_df.groupby("NFL").agg({"NFL_W/L%":(np.nanmean)})

    # merging two datasets: NFL and MLB+NBA+NHL+Cities
    nfl_mlb_nhl_nba_combined = pd.merge(nfl_df, mlb_nhl_nba_combined, how='outer', left_index=True, right_index=True)
    nfl_mlb_nhl_nba_combined = nfl_mlb_nhl_nba_combined.reset_index()

    nfl_mlb_nhl_nba_combined = nfl_mlb_nhl_nba_combined.sort_values(by='Population', ascending=False)
    nfl_mlb_nhl_nba_combined = nfl_mlb_nhl_nba_combined.set_index('Metropolitan area')


    #### COMBINED DATASET COMPUTATIONS

    # subsetting and renaming
    combined_dataset = nfl_mlb_nhl_nba_combined
    combined_dataset = combined_dataset.drop(['NFL', 'MLB', 'NBA', 'NHL'], axis=1)
    combined_dataset = combined_dataset.rename(columns={'NFL_W/L%': 'NFL',
                                                        'NBA_W/L%': 'NBA',
                                                        'NHL_W/L%': 'NHL',
                                                        'MLB_W/L%': 'MLB'})


    # binarizing and subsetting
    combined_dataset['NFL_B'] = np.where(combined_dataset['NFL'].notna(), 1, 0)
    combined_dataset['MLB_B'] = np.where(combined_dataset['MLB'].notna(), 1, 0)
    combined_dataset['NBA_B'] = np.where(combined_dataset['NBA'].notna(), 1, 0)
    combined_dataset['NHL_B'] = np.where(combined_dataset['NHL'].notna(), 1, 0)

    combined_dataset['num_teams'] = combined_dataset[['NFL_B', 'MLB_B', 'NBA_B', 'NHL_B']].sum(axis=1, skipna=True)

    combined_dataset = combined_dataset[combined_dataset['num_teams'] > 1]

    combined_dataset = combined_dataset.sort_values(by='Metropolitan area', ascending=True)
    combined_dataset = combined_dataset.drop(['NFL_B', 'MLB_B', 'NBA_B', 'NHL_B', 'num_teams'], axis=1)


    # t testing
    sports = ['NFL', 'MLB', 'NBA', 'NHL']
    p_values = pd.DataFrame({k:np.nan for k in sports}, index = sports)

    for team1 in sports:
        for team2 in sports:
            df2 = combined_dataset[(combined_dataset[team1].notna()) & (combined_dataset[team2].notna())]
            i = df2[team1]
            j = df2[team2]
            p_values.loc[team1, team2] = abs(stats.ttest_rel(i, j)[1])

    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"

    return p_values
    raise NotImplementedError()


print(sports_team_performance())



































# use plt.show() to display plots
