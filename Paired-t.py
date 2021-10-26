import pandas as pd
from scipy import stats

anorexia = pd.read_csv("anorexia.csv")

anoCont = anorexia[anorexia.Treat == "Cont"]
anoCont.head()

stats.ttest_rel(anoCont["Prewt"],anoCont["Postwt"])

anoFT = anorexia[anorexia.Treat == "FT"]
anoFT.head()

stats.ttest_rel(anoFT.Prewt,anoFT.Postwt)

pvalue2tailed = stats.ttest_rel(anoFT.Prewt,anoFT.Postwt)[1]
pvalue1tailed = stats.ttest_rel(anoFT.Prewt,anoFT.Postwt)[1]/2
