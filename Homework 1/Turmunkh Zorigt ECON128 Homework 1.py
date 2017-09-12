
# coding: utf-8

# In[4]:

#!pip install brewer2mpl
from numpy import *

get_ipython().magic(u'matplotlib inline')
from urllib import urlopen

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:

df = pd.read_csv('bank-data.csv',sep=',', error_bad_lines=False) #read file as a dataframe

print len(df) #print number of rows
print list(df) #print 1st ten headers



# In[6]:

#Question 1
print "---Age Summary Statistics---"
df['age'].describe()


# In[7]:

print "---Income Summary Statistics---"
df["income"].describe()


# In[8]:

print "---Children Summary Statistics---"
df["children"].describe()


# In[9]:

print "---Savings Account Summary Statistics---"

def printCategories(category):
    cat_groupby = df.groupby(category)
    cat_groupby.head()
    for key, value in cat_groupby:
        print "( key, len(value) ) = (", key, ",", len(value), ")"
        v=value
        
printCategories(df['save_act'])


# In[10]:

print "---Region Summary Statistics---"
printCategories(df['region'])


# In[11]:

print "---Married Summary Statistics---"
printCategories(df['married'])


# In[12]:

print "---Current Checking Account Summary Statistics---"
printCategories(df['current_act'])


# In[13]:

print "---Sex Summary Statistics---"
printCategories(df['sex'])


# In[14]:

print "---Car Summary Statistics---"
printCategories(df['car'])


# In[15]:

print "---Mortgage Summary Statistics---"
printCategories(df['mortgage'])


# In[16]:

print"---PEP Summary Stats"
printCategories(df['pep'])


# In[17]:

#Question 2
pep_groupby = df.groupby('pep') #collapse data based on pep
print("Summary Stats for Age, Children, & Income by Pep")
print pep_groupby.describe()

print """\n There are many difference between people have PEP and those who do not. On average and at the 
25%, 50%, and 75% percentiles people with PEP have higher incomes and are usually older. Additionally, people 
with PEP have fewer children on average. Wealthier people may have more resources to have the ability
to purchase the PEP, which consequently is correlated with higher incomes, fewer children, and being older.
"""


# In[18]:

pep_df = pep_groupby['region'].describe()
print("Summary Stats for Region by Pep")
pep_df.head(20)


# In[19]:

pep_df = pep_groupby['married'].describe()
print("Summary Stats for Married by Pep")
pep_df.head(20)


# In[20]:

pep_df = pep_groupby['car'].describe()
print("Summary Stats for Car by Pep")
pep_df.head(20)


# In[21]:

pep_df = pep_groupby['mortgage'].describe()
print("Summary Stats for Mortgage by Pep")
pep_df.head(20)


# In[22]:

pep_df = pep_groupby['save_act'].describe()
print("Summary Stats for Savings Account by Pep")
pep_df.head(20)


# In[23]:

pep_df = pep_groupby['current_act'].describe()
print("Summary Stats for Current Checking Account by Pep")
pep_df.head(20)


# In[24]:

pep_df = pep_groupby['sex'].describe()
print("Summary Stats for Sex by Pep")
pep_df.head(20)


# In[27]:

#Question 3
#Make a new variable that categorizes people into young, mid-age, and old based on age 

age_category = []
Young_Count=0
Mid_Age=0
Old=0

#identify age category of each person, and add it to age_category
for person in df.age:
    if person<=35:
        age_category.append("young")
        Young_Count+=1
    elif person>35 and person<=65:
        age_category.append("mid-age")
        Mid_Age+=1
    else:
        age_category.append("old")
        Old+=1
print("People who are young: "+str(Young_Count))
print("People who are mid-age: "+str(Mid_Age))
print("People who are old: "+str(Old))
print("The age group with the most people are middle age, followed by young, and then old. There are very few peoplewho are old with the PEP, maybe because they have already have a plan with a different company. More middle-aged people have the PEP than people who are young, maybe because they have more income.")


# In[28]:

len(age_category) #checking length of list matches the dataframe


# In[29]:

#convert the list of age categories into a series and add it into the dataframe

age_series=pd.Series(age_category)
df["age_series"]=age_series
df.head()


# In[30]:

age_groupby = df.groupby('age_series')
age_df = age_groupby['age_series'].describe()
print("Summary Stats for Age_Series by Pep")
age_df.head(20)


# In[31]:

#Question 4
df.plot.scatter("age","income",c="Green")

print("""There generally appears to be a positive correlation between age and income. Specifically, the correlation  
coefficient is %d. This makes sense due to people getting raises, gaining experience, etc.""") %(np.correlate(df["age"],df["income"]))


# In[32]:

#Question 5
x = df['income'][~np.isnan(df['income'])] #remove NAN from array
n, bins, patches = plt.hist(x, 9, normed=1, facecolor='green') #create density histogram of income with 9 bins
plt.xlabel("Income")
plt.ylabel("Density")
plt.show()


# In[33]:

x = df['age'][~np.isnan(df['age'])] #remove NAN from array
n, bins, patches = plt.hist(x, 30, normed=1, facecolor='green') #create a density histogram of age with 30 bins
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

