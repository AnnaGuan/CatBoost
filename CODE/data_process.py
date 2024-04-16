from typing import List, Any
import os
import numpy as np
import pandas as pd
import json

def input_synergy_data(dataset):
    function_mapping={'NCI_ALMANAC':'input_data_1', 'ONeil':'input_data_2'}
    def input_data_1():
        data_1 = pd.read_csv(r'../data/synergy_data/NCI_ALMANAC/ComboDrugGrowth_Nov2017.csv',low_memory=False)
        data_2=data_1.groupby(['SCREENER','NSC1','NSC2','CELLNAME']).agg({"SCORE":'mean',"STUDY":'count'}).reset_index().rename(columns={'SCORE':'MEAN_SCORE','STUDY':'count'}).astype({'NSC1':'int32','NSC2':'int32'})
        data_2=data_2.dropna()
        data_2=data_2[data_2['SCREENER'] != '1A']
        data_2=data_2[['NSC1','NSC2','CELLNAME','MEAN_SCORE']].rename(columns={'NSC1':'drug1','NSC2':'drug2','CELLNAME':'cell','MEAN_SCORE':'score'})
        data_2=data_2.replace('MDA-MB-231/ATCC', 'MDA-MB-231')
        return data_2

    def input_data_2():
        pass

    data=locals()[function_mapping[dataset]]()
    return data

def input_cellline_data(dataset):
    function_mapping={'NCI_60':'input_cellline_60', 'CCLE':'input_cellline_ccle'}
    def input_cellline_60():
        def input_cellline_1(postfix):
            data=pd.read_table(r'..\data\cell_line_data\NCI-60\data_NCI-60_%s.txt'%postfix,low_memory=False)
            if postfix != 'mir':
                data.drop(columns=['Probe id','Gene name','Chromosome','Start','End','Cytoband','RefSeq(mRNA)','RefSeq(protein)'],inplace=True)
            else:
                data.drop(columns=['Probe id','Gene name','Chromosome','Start','End',
                                            'Cytoband','RefSeq(mRNA)','RefSeq(protein)','MirBase Name',"Entrez gene id"],inplace=True)

            if postfix != 'mir':
                data.set_index('Entrez gene id',inplace=True)#set_index：列索引转化为行索引
            else:
                data.set_index('miRNA Accession #',inplace=True)

            '''
            list_1=list(data.columns)
            list_2=[]
            for i in range(len(list_1)):
                if i == 0:
                    list_2.append(list_1[i])
                else:
                    list_2.append(list_1[i].split(':')[1])
            '''
            data.columns=list(map(lambda x:x.split(':')[1],list(data.columns)))
            return data
        data_dict={}
        for i in ['exp', 'cop', 'mut', 'met', 'pro', 'mir']:
            data_dict[i]=input_cellline_1(i)

        return data_dict

    def input_cellline_ccle():
        pass

    data = locals()[function_mapping[dataset]]()

    return  data

def input_drug_data():
    drug_dicts={}
    with open('..\data\drug_data\drug_fingerprint_morgan_3_256.json')as f:
        fingerprint=json.load(f)
    fingerprint=pd.DataFrame(fingerprint)
    fingerprint.columns=fingerprint.columns.astype(int)
    drug_dicts['morgan_fingerprint'] = fingerprint

    drug_target=pd.read_csv('..\data\drug_data\drug_targets.csv')
    drug_mapping=dict(zip(drug_target['nsc_id'].unique().tolist(),range(len(drug_target['nsc_id'].unique().tolist()))))
    gene_mapping=dict(zip(drug_target['GeneSymbol'].unique().tolist(),range(len(drug_target['GeneSymbol'].unique().tolist()))))
    encoding=np.zeros((len(drug_target['nsc_id']),len(drug_target['GeneSymbol'])))
    for _, row in drug_target.iterrows():
        encoding[drug_mapping[row['nsc_id']], gene_mapping[row['GeneSymbol']]] = 1
    target_feat = {}
    for dug, row_id in drug_mapping.items():
        target_feat[int(dug)] = encoding[row_id].tolist()
    drug_dicts['drug_target']=pd.DataFrame(target_feat)

    with open(r'..\data\synergy_data\NCI_ALMANAC\monotherapy_dict.json')as f:
        monetherapy=json.load(f)
    monetherapy=pd.DataFrame(monetherapy)
    monetherapy.columns=monetherapy.columns.astype(int)
    drug_dicts['monetherapy']=monetherapy
    return  drug_dicts



def mapping_ids():
    pass
