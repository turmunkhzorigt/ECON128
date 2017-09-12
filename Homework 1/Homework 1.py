
# coding: utf-8

# In[1]:

#!pip install brewer2mpl
from numpy import *

get_ipython().magic(u'matplotlib inline')
from urllib import urlopen

#import brewer2mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[2]:

df = pd.read_csv('bank-data.csv',sep=',', error_bad_lines=False) #read file as a dataframe

print len(df) #print number of rows
print list(df) #print 1st ten headers



# In[3]:

#Question 1
print "---Age Summary Statistics---"
df['age'].describe()


# In[4]:

print "---Income Summary Statistics---"
df["income"].describe()


# In[5]:

print "---Children Summary Statistics---"
df["children"].describe()


# In[11]:

print "---Savings Account Summary Statistics---"
save_act_groupby = df.groupby('save_act')
save_act_groupby.head()

for key, value in save_act_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[7]:

print "---Region Summary Statistics---"
region_groupby = df.groupby('region')
region_groupby.head()

for key, value in region_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[8]:

print "---Married Summary Statistics---"
married_groupby = df.groupby('married')
married_groupby.head()

for key, value in married_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[12]:

print "---Current Checking Account Summary Statistics---"
current_act_groupby = df.groupby('current_act')
current_act_groupby.head()

for key, value in current_act_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[13]:

print "---Sex Summary Statistics---"
sex_groupby = df.groupby('sex')
sex_groupby.head()

for key, value in sex_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[15]:

print "---Car Summary Statistics---"
car_groupby = df.groupby('car')
car_groupby.head()

for key, value in car_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[16]:

print "---Mortgage Summary Statistics---"
Mortgage_groupby = df.groupby('mortgage')
Mortgage_groupby.head()

for key, value in Mortgage_groupby:
    print "( key, len(value) ) = (", key, ",", len(value), ")"
    v=value


# In[17]:

#Question 2
#I print separate columns because it gives me an error if I try to print all three of them. The line below doesn't work
#pep_df = pep_groupby['age','income','children'].describe()
pep_groupby = df.groupby('pep')

print("Summary Stats for Age by Pep")
pep_df = pep_groupby['age'].describe()
pep_df.head(20)


# In[18]:

pep_df = pep_groupby['income'].describe()
print("Summary Stats for Income by Pep")
pep_df.head(20)


# In[19]:

pep_df = pep_groupby['children'].describe()
print("Summary Stats for Children by Pep")
pep_df.head(20)


# In[20]:

pep_df = pep_groupby['region'].describe()
print("Summary Stats for Region by Pep")
pep_df.head(20)


# In[21]:

pep_df = pep_groupby['married'].describe()
print("Summary Stats for Married by Pep")
pep_df.head(20)


# In[22]:

pep_df = pep_groupby['car'].describe()
print("Summary Stats for Car by Pep")
pep_df.head(20)


# In[23]:

pep_df = pep_groupby['mortgage'].describe()
print("Summary Stats for Mortgage by Pep")
pep_df.head(20)


# In[24]:

pep_df = pep_groupby['save_act'].describe()
print("Summary Stats for Savings Account by Pep")
pep_df.head(20)


# In[25]:

pep_df = pep_groupby['current_act'].describe()
print("Summary Stats for Current Checking Account by Pep")
pep_df.head(20)


# In[40]:

#Question 3
#Make a new variable that categorizes people into young, mid-age, and old based on age 

age_category = []
Young_Count=0
Mid_Age=0
Old=0

#identify age category of each person, and add it to age_category
for person in df.age:
    if person<=40:
        age_category.append("young")
        Young_Count+=1
    if person>40 & person<=65:
        age_category.append("mid-age")
        Mid_Age+=1
    if person>65:
        age_category.append("old")
        Old+=1
print("People who are young: "+str(Young_Count))
print("People who are mid-age: "+str(Mid_Age))
print("People who are old: "+str(Old))


# In[32]:

len(age_category) #checking length of list matches the dataframe


# In[38]:

#convert the list of age categories into a series and add it into the dataframe
age_series=pd.Series(age_category)
df["age_series"]=age_series
df.head(30)


# In[37]:

age_groupby = df.groupby('age_series')
age_df = age_groupby['age_series'].describe()
print("Summary Stats for Age_Series by Pep")
age_df.head(20)


# In[ ]:

#Question 4

#gives me an invalid syntax error even though it's pretty much the same

# plt.figure(tight_layout=True, figsize=(6,4)
# plt.subplot(121)
# plt.scatter(age,income, color='k')
# plt.xlim(age.min(),age.max())
# plt.ylim(income.min(),income.max())
# plt.xlabel("Age")
# plt.ylabel("Income")
# remove_border()      


# In[ ]:

df.plot.scatter("age","income",c="Green")


# In[ ]:

#Question 5

x = df['income'][~np.isnan(df['income'])]
n, bins, patches = plt.hist(x, 9, normed=1, facecolor='green')
plt.xlabel("Income")
plt.ylabel("Density")
plt.show()


# In[ ]:

x = df['age'][~np.isnan(df['age'])]
n, bins, patches = plt.hist(x, 30, normed=1, facecolor='green')
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



