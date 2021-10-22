from math import sqrt
import pandas as pd
from scipy import stats

PlantGrowth = pd.read_csv("PlantGrowth.csv")

# Critical Value Approach
PlantGrowth['weight'].describe()
critical_value = stats.t.ppf(q=0.025,df=29)
critical_value

t_stat = (PlantGrowth['weight'].mean()-6)/(PlantGrowth['weight'].std()/sqrt(30))

# P-Value Approach
p_value = 2*stats.t.cdf(x=t_stat,df=29)
p_value

stats.ttest_1samp(PlantGrowth['weight'],popmean=6.0)

p_val = stats.ttest_1samp(PlantGrowth['weight'],popmean=6.0)[1]
one_tailed_p_value = p_val/2
one_tailed_p_value
