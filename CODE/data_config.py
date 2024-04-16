import sys, os, json


# 'drug_integrate': whether or not integrating all drug features when constructing input data
# 'drug_indep': whether or not summing features of drug1 and drug2 (False: sum)
method_config_dict = {
    'deepsynergy_preuer_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',
        'drug_feats': ['morgan_fingerprint'],
        'cell_feats': ['exp'],
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'NN',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'XGBOOST_janizek_2018':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',
        'drug_feats': ['morgan_fingerprint'],
        'cell_feats': ['exp'],
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'XGBOOST',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'Logit_li_2020':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',
        'drug_feats': ['drug_target'],
        'cell_feats': ['exp'],
        'cell_feat_filter': 'variance',
        'drug_feat_filter': 'target',
        'model_name': 'LR',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    },

    'CatBOOST_2022':{
        'synergy_data': 'NCI_ALMANAC',
        'cell_data': 'NCI_60',
        'cell_list': 'all',
        'drug_feats': ['morgan_fingerprint','drug_target','monetherapy'],
        'cell_feats': ['exp'],
        'cell_feat_filter': 'cancer',
        'drug_feat_filter': 'target',
        'model_name': 'CatBoost',
        'cell_integrate': True,
        'drug_integrate': True,
        'drug_indep': False
    }
}


