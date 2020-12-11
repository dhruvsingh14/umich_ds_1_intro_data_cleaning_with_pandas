######################################
# Assignment 3: Merging and Querying #
######################################
# libraries
import pandas as pd
import numpy as np

# to suppress warning messages
import warnings
warnings.filterwarnings('ignore')

##############
# Question 1 #
##############
# creating full inner merge globally
## Dataset 1: Energy
Energy = pd.read_excel('data/Energy Indicators.xls',
                        usecols = "C:F",
                        skiprows = 17,
                        skipfooter = 38,
                        header=0)
# renaming
Energy = Energy.rename(columns={'Unnamed: 2': 'Country',
                                'Petajoules': 'Energy Supply',
                                'Gigajoules': 'Energy Supply per Capita',
                                '%': '% Renewable'})
# converting type, removing null
Energy['Energy Supply'] = pd.to_numeric(Energy['Energy Supply'], errors = 'coerce')
Energy['Energy Supply per Capita'] = pd.to_numeric(Energy['Energy Supply per Capita'], errors = 'coerce')
# converting units petajoules to gigajoules
Energy['Energy Supply'] = Energy['Energy Supply']*1000000
# removing numeric characters from country names
Energy['Country'] = Energy['Country'].str.replace('\d+', '')
# replacing country names
Energy['Country'] = Energy['Country'].replace(["Republic of Korea",
                "United States of America",
                "United Kingdom of Great Britain and Northern Ireland",
                "China, Hong Kong Special Administrative Region"],
                ["South Korea",
                "United States",
                "United Kingdom",
                "Hong Kong"])
# removing parentheses
Energy['Country'] = Energy['Country'].str.replace('\s\(.*', '')
# setting index for merge
Energy = Energy.set_index('Country')

## Dataset 2: GDP
GDP = pd.read_csv('data/world_bank.csv',
                    skiprows = 4,
                    header=0)
# replacing country names
GDP['Country Name'] = GDP['Country Name'].replace(["Korea, Rep.",
                "Iran, Islamic Rep.",
                "Hong Kong SAR, China"],
                ["South Korea",
                "Iran",
                "Hong Kong"])
# renaming column
GDP = GDP.rename(columns={'Country Name': 'Country'})
# setting index for merge
GDP = GDP.set_index('Country')

## Dataset 3: Energy Journals
ScimEn = pd.read_excel('data/scimagojr-3.xlsx',
                        header=0)
ScimEn = ScimEn.set_index('Country')

## Merge: Inner
m1 = pd.merge(ScimEn, Energy, how='inner', left_index=True, right_index=True)
m2 = pd.merge(m1, GDP, how='inner', left_index=True, right_index=True)

# subsetting merge
def answer_one():
    years = list(map(str, range(1960, 2006)))
    # dropping 46 year columns before 2006
    m2_sub = m2.drop(years, axis=1)
    # dropping 3 unused gdp columns
    m2_sub = m2_sub.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
    # keeping only ranks 1 to 15
    m2_sub = m2_sub[m2_sub['Rank'] < 16]
    # sorting
    m2_sub = m2_sub.sort_values(by='Rank')
    return(m2_sub)
    raise NotImplementedError()
# checking object type, and shape
assert type(answer_one()) == pd.DataFrame, "Q1: You should return a DataFrame!"
assert answer_one().shape == (15, 20), "Q1: You DataFrame should have 20 columns and 15 entries!"

##############
# Question 2 #
##############
# calculating rows lost in inner merge
def answer_two():
    # full outer join
    union1 = pd.merge(ScimEn, Energy, how='outer', left_index=True, right_index=True)
    union2 = pd.merge(m1, GDP, how='outer', left_index=True, right_index=True)
    years = list(map(str, range(1960, 2006)))
    union2 = union2.drop(years, axis=1)
    union2 = union2.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
    # calculating difference
    return(union2.shape[0] - m2.shape[0])
    raise NotImplementedError()
# testing object type
assert type(answer_two()) == int, "Q2: You should return an int number!"

##############
# Question 3 #
##############
# avg GDP
def answer_three():
    # list of columns to average over
    years = list(map(str, range(2006, 2016)))
    # mean gdp calculation
    avg_gdp = answer_one()
    avg_gdp['mean'] = avg_gdp.mean(axis=1)
    avg_gdp = avg_gdp.sort_values(by='mean', ascending=False)
    # returning series
    return(avg_gdp['mean'])
    raise NotImplementedError()

# testing object type
assert type(answer_three()) == pd.Series, "Q3: You should return a series!"

##############
# Question 4 #
##############
# uk gdp change past 10 years
def answer_four():
    # calculating 6th largest avg gdp
    index_label = answer_three().index.values
    sixth_gdp = index_label[5]
    # indexing using above automation
    uk_change = ((answer_one().loc[sixth_gdp]['2015']-answer_one().loc[sixth_gdp]['2006'])/(answer_one().loc[sixth_gdp]['2006']))*100
    return(uk_change)
    raise NotImplementedError()

##############
# Question 5 #
##############
# mean energy supply per capita
def answer_five():
    return(answer_one()['Energy Supply per Capita'].mean())
    raise NotImplementedError()

##############
# Question 6 #
##############
# highest % renewable country: brazil
def answer_six():
    # highest % renewable country: brazil
    highest_renewable = answer_one().sort_values(by='% Renewable', ascending = False)
    highest_renewable = highest_renewable[['% Renewable']]
    # releasing index to fetch tuple
    highest_renewable = highest_renewable.reset_index()
    highest_renewable = highest_renewable.head(1)
    # creating tuple by calling values
    renew_tuple = (highest_renewable.iloc[0]['Country'],highest_renewable.iloc[0]['% Renewable'])
    return(renew_tuple)
    raise NotImplementedError()

# testing object type
assert type(answer_six()) == tuple, "Q6: You should return a tuple!"
assert type(answer_six()[0]) == str, "Q6: The first element in your result should be the name of the country!"

##############
# Question 7 #
##############
# citations ratio
def answer_seven():
    # citations ratio
    citations_ratio = answer_one()[['Self-citations','Citations']]
    citations_ratio['self_citations %'] = answer_one()['Self-citations']/answer_one()['Citations']
    # sorting by citations ratio
    citations_ratio = citations_ratio.sort_values(by='self_citations %', ascending = False)
    # releasing index to fetch tuple
    citations_ratio = citations_ratio.reset_index()
    citations_ratio = citations_ratio.head(1)
    # creating tuple by calling values
    citations_tuple = (citations_ratio.iloc[0]['Country'],citations_ratio.iloc[0]['self_citations %'])
    return(citations_tuple)
    raise NotImplementedError()

# testing object type
assert type(answer_seven()) == tuple, "Q7: You should return a tuple!"
assert type(answer_seven()[0]) == str, "Q7: The first element in your result should be the name of the country!"

##############
# Question 8 #
##############
# population estimate
def answer_eight():
    # popestimate
    population_estimate = answer_one()[['Energy Supply', 'Energy Supply per Capita']]
    population_estimate['popestimate'] = population_estimate['Energy Supply']/population_estimate['Energy Supply per Capita']
    # sorting by popestimate
    population_estimate = population_estimate.sort_values(by='popestimate', ascending = False)
    # resetting index
    population_estimate = population_estimate.reset_index()
    # returning 3rd most populous
    third_most_populous = population_estimate.iloc[2]['Country']
    return(third_most_populous)
    raise NotImplementedError()

# testing object type
assert type(answer_eight()) == str, "Q8: You should return the name of the country!"

##############
# Question 9 #
##############
# citable documents per person
def answer_nine():
    # recalculating popestimate
    citable_per_capita = answer_one()[['Citable documents', 'Energy Supply', 'Energy Supply per Capita']]
    citable_per_capita['popestimate'] = citable_per_capita['Energy Supply']/citable_per_capita['Energy Supply per Capita']
    # calculating citable docs per capita
    citable_per_capita['citable_docs_pc'] = citable_per_capita['Citable documents']/citable_per_capita['popestimate']
    citable_per_capita = citable_per_capita[['citable_docs_pc', 'Energy Supply per Capita']]
    return(citable_per_capita['citable_docs_pc'].corr(citable_per_capita['Energy Supply per Capita']))
    raise NotImplementedError()

def plot9():
    import matplotlib.pyplot as plt
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y = 'Energy Supply per Capita', kind='scatter',
                xlim=[0, 0.0006])
    plt.show()
# testing object type
assert answer_nine() >= -1. and answer_nine() <= 1., "Q9: A valid correlation should be between -1 to 1!"

###############
# Question 10 #
###############
# median % renewable binary column
def answer_ten():
    # calling % renewable
    highest_renewable = answer_one()[['Rank', '% Renewable']]
    # storing median
    renewable_median = highest_renewable['% Renewable'].median()
    # creating binary column
    highest_renewable['HighRenew'] = np.where(highest_renewable['% Renewable'] > renewable_median, 1, 0)
    highest_renewable = highest_renewable.sort_values(by='Rank', ascending=True)
    return(highest_renewable['HighRenew'])
    raise NotImplementedError()
# testing object type
assert type(answer_ten()) == pd.Series, "Q10: You should return a series!"

###############
# Question 11 #
###############
# provided dictionary for grouping continents
ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
ContinentDf = pd.DataFrame(list(ContinentDict.items()),columns = ['Country', 'Continent'])
# setting country name as index for merge
ContinentDf = ContinentDf.set_index('Country')

# creating combined dataset, grouping by continent
def answer_eleven():
    # recalculating popestimate
    population_estimate = answer_one()[['Energy Supply', 'Energy Supply per Capita']]
    population_estimate['popestimate'] = population_estimate['Energy Supply']/population_estimate['Energy Supply per Capita']
    # sorting
    population_estimate = population_estimate.sort_values(by='popestimate', ascending = False)
    # merging
    cont_df = pd.merge(ContinentDf, population_estimate, how='inner', left_index=True, right_index=True)
    # grouping by continent and aggregating
    cont_df = cont_df.reset_index()
    # pandas automatically converts group by columns to index
    cont_df = cont_df.groupby("Continent").agg({"popestimate":('count', np.nansum, np.nanmean,np.nanstd)})
    # dropping nested header, top row
    cont_df.columns = cont_df.columns.droplevel(0)
    cont_df = cont_df.rename(columns={'count': 'size',
                                      'nansum': 'sum',
                                      'nanmean': 'mean',
                                      'nanstd': 'std'})
    return(cont_df)
    raise NotImplementedError()
# testing object type and shape
assert type(answer_eleven()) == pd.DataFrame, "Q11: You should return a DataFrame!"
assert answer_eleven().shape[0] == 5, "Q11: Wrong row numbers!"
assert answer_eleven().shape[1] == 4, "Q11: Wrong column numbers!"

###############
# Question 12 #
###############
# multi index
def answer_twelve():
    # % renewable
    perc_renewable = answer_one().sort_values(by='% Renewable', ascending = False)
    perc_renewable = perc_renewable['% Renewable']
    # 5 bins means 6 cuts
    perc_renewable = pd.cut(perc_renewable,5)
    # converting series to dataframe
    perc_renewable = perc_renewable.to_frame()
    # merging
    multi_index = pd.merge(ContinentDf, perc_renewable, how='inner', left_index=True, right_index=True)
    # resetting index
    multi_index = multi_index.reset_index()
    multi_index = multi_index.groupby(["Continent", "% Renewable"]).agg({"Country":('count')})
    multi_index = multi_index[multi_index.Country > 0]

    return(multi_index['Country'])
    raise NotImplementedError()
# testing object type and length
assert type(answer_twelve()) == pd.Series, "Q12: You should return a Series!"
assert len(answer_twelve()) == 9, "Q12: Wrong result numbers!"

###############
# Question 13 #
###############
# formatting thousands separator
def answer_thirteen():
    # recalculating popestimate
    population_estimate = answer_one()[['Energy Supply', 'Energy Supply per Capita']]
    population_estimate['PopEst'] = population_estimate['Energy Supply']/population_estimate['Energy Supply per Capita']
    # sorting by popestimate
    population_estimate = population_estimate.sort_values(by='PopEst', ascending = False)
    population_estimate.drop(columns=['Energy Supply', 'Energy Supply per Capita'], inplace=True)
    # adding thousands separators
    population_estimate['PopEst'] =  population_estimate.PopEst.apply(lambda x : "{:,}".format(x))
    return(population_estimate['PopEst'])
    raise NotImplementedError()
# testing object type and length
assert type(answer_thirteen()) == pd.Series, "Q13: You should return a Series!"
assert len(answer_thirteen()) == 15, "Q13: Wrong result numbers!"

# copying code for this optional section
# included in assignment notebook
def plot_optional():
    import matplotlib.pyplot as plt
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
    This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
    2014 GDP, and the color corresponds to the continent.")
    plt.show()

























# use plt.show() to display plots
