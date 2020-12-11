######################################
# Assignment 2: Pandas Data Cleaning #
######################################

# libraries
import pandas as pd
# reading in data
df = pd.read_csv('data/NISPUF17.csv')

##############
# Question 1 #
##############

# maternal education
def proportion_of_education():
    # numerator = length of child unique id, for each educ category
    # denominator = length of child unique id, after confirming no nulls in educ
    maternal_education = {"less than high school": len(df[df['EDUC1'] == 1]['SEQNUMC'])/len(df['SEQNUMC']),
                            "high school": len(df[df['EDUC1'] == 2]['SEQNUMC'])/len(df['SEQNUMC']),
                            "more than high school but not college": len(df[df['EDUC1'] == 3]['SEQNUMC'])/len(df['SEQNUMC']),
                            "college": len(df[df['EDUC1'] == 4]['SEQNUMC'])/len(df['SEQNUMC'])}
    return maternal_education
    raise NotImplementedError()

# writing function tests
assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education())==4, "You have not returned a dictionary with 4 items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."

##############
# Question 2 #
##############

# influenza vaccine by breastfeeding
def average_influenza_doses():
    # using vectorization, mean method
    x1= df[(df['CBF_01']==1) & (df['P_NUMFLU'].notna())]['P_NUMFLU'].mean()
    x2= df[(df['CBF_01']==2) & (df['P_NUMFLU'].notna())]['P_NUMFLU'].mean()
    vaccination_tuple = (x1, x2)
    return vaccination_tuple
    raise NotImplementedError()

assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

##############
# Question 3 #
##############

# chicken pox by gender
def chickenpox_by_sex():
    # for males: # (contracted & vaccinated)/(vaccinated & not contracted)
    dfm = df[df['SEX']==1]
    df_cp_m = dfm[(dfm['HAD_CPOX']==1) & (dfm['P_NUMVRC'].notna()) & (dfm['P_NUMVRC']>0)]
    df_ncp_m = dfm[(dfm['HAD_CPOX']==2) & (dfm['P_NUMVRC'].notna()) & (dfm['P_NUMVRC']>0)]
    x1 = len(df_cp_m['SEQNUMC'])/len(df_ncp_m['SEQNUMC'])
    # for females: # (contracted & vaccinated)/(vaccinated & not contracted)
    dff = df[df['SEX']==2]
    df_cp_f = dff[(dff['HAD_CPOX']==1) & (dff['P_NUMVRC'].notna()) & (dff['P_NUMVRC']>0)]
    df_ncp_f = dff[(dff['HAD_CPOX']==2) & (dff['P_NUMVRC'].notna()) & (dff['P_NUMVRC']>0)]
    x2 = len(df_cp_f['SEQNUMC'])/len(df_ncp_f['SEQNUMC'])

    # creating dictionary for chicken pox rates by gender
    cp_by_gender = {"Males": x1,
                      "Females": x2}
    return cp_by_gender
    raise NotImplementedError()

assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."

##############
# Question 4 #
##############

# vaccination vs. contraction
def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    # example
    df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
                    "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

    # stub code for correlation testing
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])

    return(corr)
    raise NotImplementedError()

assert -1<=corr_chickenpox()<= 1, "You must return a float number betewen -1.0 and 1.0"















# use plt.show() to display plots
