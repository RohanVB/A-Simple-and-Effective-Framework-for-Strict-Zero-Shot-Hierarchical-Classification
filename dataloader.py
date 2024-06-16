#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import random


# # WOS Dataset

# ## Note: WOS results in paper area only reported for depth=2.

# In[ ]:


# Data must be downloaded from https://data.mendeley.com/datasets/9rw3vkcfy4/6
# We utilize Meta-data/Data.xlsx

data_path_wos = "Meta-data/Data.xlsx"
df_wos = pd.read_excel(data_path_wos).dropna()


# In[ ]:


freg = df_wos.groupby('area')['area'].transform('count')
prob = freg / freg.sum()
df_sampled = df_wos.sample(n=3000, replace=False, weights=prob.tolist())


# In[ ]:


df_sampled.area.value_counts()


# In[ ]:


import matplotlib.pyplot as plt

plt.bar( [i for i in range(0, len(df_sampled.area.value_counts()))], df_sampled.area.value_counts().tolist())


# In[ ]:


labels = list(set(df_wos.Domain))

unseen_list = random.sample(labels, 2)
seen_list = [value for value in labels if value not in unseen_list]

test_unseen = test[pd.DataFrame(test.Domain.tolist()).isin(unseen_list).any(1).values]
test_unseen.to_csv('test.csv')


# # Amazon Beauty Dataset 

# ## Note: Based on the number of nodes, the categories may have to be modified. The code for "depth=2" is commented out and "depth=3" is utilized below.

# In[ ]:


# this dataset must be downloaded from https://amazon-reviews-2023.github.io/ under the category of All_Beauty

data_path = 'datasets/Beauty'

df_beauty = pd.read_json(data_path + '/beauty_meta', lines=True)


# In[ ]:


df_beauty = df_beauty[['description', 'categories']]
df_beauty.loc[:, 'categories'] = df_beauty.categories.map(lambda x: x[0])

# two_categories = [l[1:3] for l in df_beauty.categories]
three_categories = [l[1:4] for l in df_beauty.categories]
set([l[-1] for l in three_categories])


# In[ ]:


# df_beauty['category_limit'] = two_categories
df_beauty['category_limit'] = three_categories

df_beauty = df_beauty.dropna()
df_beauty['len'] = df_beauty['category_limit'].str.len()

# df_beauty = df_beauty.loc[df_beauty['len'] == 2]
df_beauty = df_beauty.loc[df_beauty['len'] == 3]

df_beauty.loc[:, 'category_parent'] = df_beauty.category_limit.map(lambda x: x[0])
df_beauty.loc[:, 'category_pchild'] = df_beauty.category_limit.map(lambda x: x[1])
df_beauty.loc[:, 'category_child'] = df_beauty.category_limit.map(lambda x: x[2])


# In[ ]:


df_beauty


# In[ ]:


labels = list(set(df_beauty.category_parent))

unseen_list = random.sample(labels, 2)
seen_list = [value for value in labels if value not in unseen_list]

test_unseen = test[pd.DataFrame(test.category_parent.tolist()).isin(unseen_list).any(1).values]

test_unseen.to_csv('test.csv')

