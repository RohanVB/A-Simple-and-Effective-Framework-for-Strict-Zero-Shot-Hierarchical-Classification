#!/usr/bin/env python
# coding: utf-8


import pickle as pkl

import re
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
    """
    Helper function to remove html tags
    """
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def get_top_one(top_five: List[str]) -> List[str]:
    """
    Input Params: List with top 5 predictions
    Output: List of top 1 predictions only
    Helper function to retain only top one predictions
    """
    return [l[:1] for l in top_five]

def get_top_three(top_five: List[str]) -> List[str]:
    """
    Input Params: List with top 5 predictions
    Output: List of top 3 predictions only
    Helper function to retain only top three predictions
    """
    return [l[:3] for l in top_five]

def calc_hits(predicted_lbls, g_truths):
    """
    Input Params: List of predicted labels and list of ground truth
    Output: accuracy
    Helper function to calculate accuracy
    """
    counter = 0
    incorrect_indices = []
    for n, (i, m) in enumerate(zip(predicted_lbls, g_truths)):
        model_outputs = [x.lower().strip() for x in i]
        ground_truth = m.lower().strip()
        if ground_truth in model_outputs:
            counter += 1
    return counter

def calc_hits_macro_top5(predicted_lbls, g_truths):
    """
    Input Params: List of predicted labels and list of ground truth
    Output: macro f1
    Helper function to calculate macro f1 given list of top 5 predictions
    """
    correct_indices = []
    for n, (i, m) in enumerate(zip(predicted_lbls, g_truths)):
        model_outputs = [x.strip() for x in i]
        ground_truth = m.strip()
        if ground_truth in model_outputs:
            correct_indices.append(ground_truth)
        else:
            correct_indices.append('incorrect')
    return correct_indices

def calc_encodings(flat_list_vals):
    """
    Helper function to used to calculate f1 for top one predictions
    """
    encoded_list = []
    if len(flat_list_vals[0]) == 1:
        flat_clean = [item.strip() for sublist in get_top_one(flat_list_vals) for item in sublist]
    else:
        flat_clean = [item.strip() for item in flat_list_vals]
    for elem in flat_clean:
        if elem in list(labels_dict.keys()):
            encoded_list.append(labels_dict[elem])
        else:
            encoded_list.append(138)
    return encoded_list



with open(PATH_TO_MODEL_RESULTS_BART, 'rb') as p:
    bart = pkl.load(p)  # top 5 results of BART outputs
bart_top1 = [l[:1] for l in bart]  # top 1 results of BART outputs



with open(PATH_TO_MODEL_RESULTS_T0PP, 'rb') as p:
    t0pp = pkl.load(p)
    
t0pp_clean = []
for i in t0pp:
    t0pp_clean.append([cleanhtml(j) for j in i])



import pandas as pd

df = pd.read_csv(PATH_TO_DATASET_SPLIT).dropna()

label_names = [i.strip() for i in list(set(df.category_pchild))]


# # Calculate Accuracy


# Below functions can be wrapped in get_top_one() or get_top_three() to get corresponding predictions

print(calc_hits(bart, df.category_pchild)/len(df.category_pchild)*100)  # BART
print(calc_hits(t0pp_clean, df.category_pchild)/len(df.category_pchild)*100)  # T0pp


# # Calculate Macro F1

labels_dict = {}
for n, i in enumerate(label_names):
    labels_dict[i] = n
    
flat_ground_truths = [item.strip() for item in df.category_pchild.tolist()]

encoded_ground_truths = []
for i in flat_ground_truths:
    if i in list(labels_dict.keys()):
        encoded_ground_truths.append(labels_dict[i])



# Below functions can be wrapped in get_top_one() or get_top_three() to get corresponding predictions

print(f1(calc_encodings(calc_hits_macro_top5(bart, flat_ground_truths)), encoded_ground_truths, average='macro')) # BART
print(f1(calc_encodings(calc_hits_macro_top5(t0pp_clean, flat_ground_truths)), encoded_ground_truths, average='macro')) # T0pp

