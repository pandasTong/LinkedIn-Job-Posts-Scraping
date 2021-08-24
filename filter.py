import pandas as pd

def filter(filename):

	df = pd.read_csv(filename)
	# Remove Senior jobs
	df1 = df[df["Title"].str.contains('Senior|Lead|Sr.|Sr|SENIOR|Director|Manager|Principal')==False]
	# Remove free labor jobs 
	exp = ['2 year', '3 years', '4 years', '5 years', '2 yrs', '3 yrs', '4 yrs', '5 yrs', 
	       '2+ years', '3+ years', '4+ years', '5+ years', '2+ yrs', '3+ yrs', '4+ yrs', '5+ yrs',
	      'three years', 'four years', 'five years']
	df1.loc[:,['TF']] = df1['Detail'].apply(lambda x: 1 if any(i in x for i in exp) else 0)
	df1 = df1[df1['TF'] == 0]
	# Save to excel
	df1.to_excel('filter.xlsx')

filter('xxx.csv')