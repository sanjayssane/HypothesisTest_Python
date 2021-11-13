import pandas as pd
from scipy import stats

co2 = pd.read_csv("CO2.csv")
co2_chill = co2[co2.Treatment == "chilled"]
co2_nonchill = co2[co2.Treatment == "nonchilled"]

uptake_chill = co2_chill.uptake
uptake_nonchill = co2_nonchill.uptake
stats.bartlett(uptake_chill,uptake_nonchill)

stats.ttest_ind(uptake_chill,uptake_nonchill,equal_var=True)

pvalue2tailed = stats.ttest_ind(uptake_chill,uptake_nonchill,equal_var=False)[1]
pvalue1tailed = stats.ttest_ind(uptake_chill,uptake_nonchill,equal_var=False)[1]/2
pvalue1tailed
