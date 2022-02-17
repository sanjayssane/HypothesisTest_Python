# Completely Randomized Design
setwd("F:/Statistics/Datasets")
agr <- read.csv("Yield.csv",stringsAsFactors = T)
av <- aov(Yield ~ Treatments , data = agr)
# OR
av <- aov(agr$Yield ~ agr$Treatments )
anova(av)

TukeyHSD(av)
