import pandas as pd

from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
######################Example 1#################################
agr = pd.read_csv("Yield.csv")
agrYield = ols('Yield ~ Treatments', data=agr).fit()
table = anova_lm(agrYield, typ=2)
print(table)

######## Post Hoc Tukey HSD ################
from statsmodels.stats.multicomp import pairwise_tukeyhsd

compare = pairwise_tukeyhsd(agr.Yield, agr.Treatments, alpha=0.05)
# =============================================================================
# compare._results_table.data
# compare.confint
# compare.reject
# =============================================================================

dd = pd.DataFrame(compare._results_table.data[1:],
                  columns=compare._results_table.data[0])
dd

# Also 
# =============================================================================
# from statsmodels.stats.multicomp import MultiComparison
# compare = MultiComparison(agr.Yield, agr.Treatments)
# results = compare.tukeyhsd()
# results.plot_simultaneous()
# =============================================================================


# =============================================================================
# 
# ######################Example 2#################################
# anorexia = pd.read_csv("G:/Statistics (Python)/Datasets/anorexia.csv")
# anoPost = ols('Postwt ~ Treat', data=anorexia).fit()
# table = anova_lm(anoPost, typ=2)
# print(table)
# 
# ######## Post Hoc Tukey HSD ################
# from statsmodels.stats.multicomp import pairwise_tukeyhsd
# 
# compare = pairwise_tukeyhsd(anorexia.Postwt, anorexia.Treat, alpha=0.05)
# compare._results_table.data
# compare.confint
# compare.reject
# 
# dd = pd.DataFrame(compare._results_table.data[1:],
#                   columns=compare._results_table.data[0])
# dd
# =============================================================================
