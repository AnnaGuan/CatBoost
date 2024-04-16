import numpy as np
import pandas as pd
import os,random,json
from data_process import *
from data_config import *



def filter_drug(original_list,filter_drug_type):
    if filter_drug_type == 'target':
        drug_target=pd.read_csv('..\data\drug_data\drug_targets.csv',low_memory=False)
        drug_list_with_target=drug_target['nsc_id'].unique().tolist()
        select_drug=list(set(original_list) & set(drug_list_with_target))
        return select_drug
    elif filter_drug_type == None:
        select_drug=original_list
        return select_drug

def filter_cell(original_list,filter_cell_type,available_cancer_specific_cell_list):
    if filter_cell_type == 'all':
        select_cells=original_list
    elif filter_cell_type == 'TNBC':
        select_cells =available_cancer_specific_cell_list['TNBC']
    else:
        select_cells = [filter_cell_type]

    return select_cells


def filter_cell_features(cell_data_dicts,selected_cells, cell_feats, cell_feat_filter, integrate):

    def filter_by_variance():
        if len(cell_feats) > 1:
            temp=cell_data_dicts['exp']
        else:
            temp=cell_data_dicts[cell_feats[0]]
        var_df=temp.var(axis=1)
        select_genes=list(var_df.sort_values(ascending=False).iloc[:1000].index)
        return select_genes

    def filter_by_cancer_genes():
        kgg_genes_list=pd.read_csv('..\data\pathway_data\kegg_gene_list.csv')
        select_genes=kgg_genes_list[kgg_genes_list['pathway']=='hsa05200']['eg'].values.tolist()

        return select_genes

    def filter_by_targets_genes():
        drug_targets=pd.read_csv('..\data\drug_data\drug_targets.csv')
        select_genes=drug_targets['entrez'].unique().tolist()

        return select_genes

    function_mapping={'variance':'filter_by_variance', 'cancer':'filter_by_cancer_genes',
                        'target':'filter_by_target_genes'}
    if cell_feat_filter is not None:
        select_genes=locals()[function_mapping[cell_feat_filter]]()
    else:
        select_genes=list(cell_data_dicts['exp'].index)

    if len(cell_feats)==1:#cell_feats=['exp']
        feats=cell_data_dicts[cell_feats[0]]
        selected_cols=list(set(selected_cells) & set(list(feats.columns)))#selected_cells=cell_list
        if cell_feats[0] != 'mir':
            selected_rows=list(set(select_genes) & set(list(feats.index)))
        else:
            selected_rows=list(feats.index)
        feats=feats.loc[selected_rows,selected_cols]
        feats.dropna(axis=0,how='any',inplace=True)
    else:
        feats_list={}
        for feats_type in cell_feats:
            values=cell_data_dicts[feats_type]
            selected_cols=list(set(list(values.columns)) & set(selected_cells))
            if feats_type != 'mir':
                selected_rows=list(set(select_genes) & set(list(values.index)))
            else:
                selected_rows=list(values.index)
            sel_feats=values.loc[selected_rows,selected_cols]
            sel_feats.dropna(axis=0,how='any',inplace=True)
            feats_list[feats_type]=sel_feats

        if integrate == True:
            feats=pd.concat(list(feats_list.values()))
        else:
            feats=feats_list

    return feats,selected_cols
















#print(filter_cell(original_list,'TNBC',available_cancer_specific_cell_list['NCI_60']))


