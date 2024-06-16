#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
The following code can be used with any data from dataloaders.py
Uncommented code is for BART
Commented code is for T0pp
For using T0pp-BART, BART-T0pp, the outputs must be nested from each prior model and included in the prompt template.

Here is an example of what that may look like:

input_list = []
for i, j in zip(df_test.Abstract.tolist(), bart_top):
    input_list.append('Here is some text that entails "{}":{}. What area is this text related to?'.format(', '.join(j),, i))

"""


# In[ ]:


import os
import json
import ast

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import torch
torch.cuda.device_count()

from transformers import pipeline

import pickle as pkl
from tqdm import tqdm as tqdm
import pandas as pd


# In[ ]:


torch.cuda.is_available()
torch.cuda.device_count()


# In[ ]:


df_test = pd.read_csv('test.csv').dropna()


# In[ ]:


label_names = [i.strip() for i in list(set(df_test.area))]
parent_label_names = [i.strip() for i in list(set(df_test.Domain))]
all_labels = parent_label_names + label_names


# In[ ]:


max_memory_mapping = {0: "24GB"}

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli", device_map="auto", load_in_8bit=True, max_memory=max_memory_mapping, device=0)


# In[ ]:


cls_output = classifier(df_test.Abstract.tolist(), label_names, multi_label=True)


# ## Uncomment lines below for T0pp

# In[ ]:


# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# import torch

# model_name = "bigscience/T0pp"

# model = AutoModelForSeq2SeqLM.from_pretrained(model_name, device_map="auto", load_in_8bit=True)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# print("Model and tokenizer loaded")

# input_list = []
# for i in zip(df_test.Abstract.tolist()):
#     input_list.append('Here is some text: {}. What area is this text related to?'.format(i))


# In[ ]:


predicted_labels = []
for i in cls_output:
    predicted_labels.append(i['labels'][:5])


# In[ ]:


with open('bart.pkl', 'wb') as p:
    pkl.dump(predicted_labels, p)

