main：
Main program, including data reading, cleaning, combination, construction of feature data set, segmentation training set and test set, model training and running, model results saving and so on.

data_config：
This code is a dictionary, mainly used to call all parameters of a model, used in the main program.

data_process：
The functions in this code are mainly used for reading data, reading and cleaning the data in the data file, including the cleaning and reading of the synergistic data, cell line characteristics and drug characteristics. Through this code, you can get a dictionary that contains all the cell line characteristics, and a dictionary that contains all the drug characteristics, which is convenient to retrieve the corresponding characteristics in the next step.

feat_selection：
The code is mainly to retrieve and screen the data feature dictionary read by the previous code, including the screening of drug characteristics and cell line characteristics, in order to obtain the required feature data set.

model_new：
This code is a model package that contains the models used by the main program and is called in the main program.


For the above code, just run the main program.The operation method of the main program is：
sys.argv=['CatBOOST_2022',1]

In jupyternotbook, run the main program by passing arguments using sys.argv.

Datasets:
1. cell_line_data（NCI-60）：
This folder contains cell line characteristic data such as gene expression profiles, gene mutations, proteins, etc.

2. drug_data：
This folder contains drug signature data such as Morgan molecular fingerprints, drug targets, etc.

3. synergy_data（NCI_ALMANAC）：
The folder contains the drug-drug synergy dataset (master dataset, containing 130,000 samples), monotherapy information, and more.

4.idx：
This file stores the index of the 5-fold hierarchical cross-fold validation for each fold validation set and test set.
