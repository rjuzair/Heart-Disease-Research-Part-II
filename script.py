# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

sns.boxplot(data = heart, x = 'heart_disease', y = 'thalach')
plt.show()

thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

#print(np.mean(thalach_hd))

mean_diff = np.mean(thalach_no_hd) - np.mean(thalach_hd)
print('`thalach` mean difference: ' +str(mean_diff))

median_diff = np.median(thalach_no_hd) - np.median(thalach_hd)
print('`thalach` median difference: ' +str(median_diff))

#5 - 6
tstat, pval = stats.ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
#pval rejects our null hypothesis

#7
plt.clf()
sns.boxplot(data = heart, x = 'heart_disease', y = 'age')
plt.title('Age and Heart Disease')
plt.show()
age_hd = heart.age[heart.heart_disease == 'presence']
age_no_hd = heart.age[heart.heart_disease == 'absence']
#print(np.mean(age_hd))
#print(np.mean(age_no_hd))
tstat, pval = stats.ttest_ind(age_hd, age_no_hd)
print(pval)

#8
plt.clf()
sns.boxplot(data = heart, x = 'cp', y = 'thalach')
plt.title('Max heart rate and type of chest pain')
plt.show()

#9
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

#10
f_stat, pval = stats.f_oneway(thalach_typical, thalach_atypical, thalach_asymptom, thalach_nonangin)
print(pval)

#11
results = pairwise_tukeyhsd(endog = heart.thalach,
groups = heart.cp)
print(results)

#12
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

chi2, pval, dof, expected = stats.chi2_contingency(Xtab)
print(pval)
