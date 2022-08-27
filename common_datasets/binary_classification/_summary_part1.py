"""
This module contains the summary of all binary classification problems, part 1
"""

summary_part1 = [{'name': 'hypothyroid',
  'phenotype': 'hypothyroid',
  'citation_key': 'krnn',
  'n_col': 216,
  'n_col_orig': 216,
  'n_col_non_unique_orig': 212,
  'n': 13086,
  'DESCR': 'hypothyroid',
  'n_minority': 805,
  'imbalance_ratio': 15.255900621118013,
  'data_loader': 'load_sylva'},
 {'name': 'vehicle0',
  'phenotype': 'vehicle',
  'citation_key': 'keel',
  'n_col': 18,
  'n_col_orig': 18,
  'n_col_non_unique_orig': 18,
  'n': 846,
  'DESCR': 'vehicle0',
  'n_minority': 199,
  'imbalance_ratio': 3.251256281407035,
  'data_loader': 'load_vehicle0'},
 {'name': 'vehicle1',
  'phenotype': 'vehicle',
  'citation_key': 'keel',
  'n_col': 18,
  'n_col_orig': 18,
  'n_col_non_unique_orig': 18,
  'n': 846,
  'DESCR': 'vehicle1',
  'n_minority': 217,
  'imbalance_ratio': 2.8986175115207375,
  'data_loader': 'load_vehicle1'},
 {'name': 'vehicle2',
  'phenotype': 'vehicle',
  'citation_key': 'keel',
  'n_col': 18,
  'n_col_orig': 18,
  'n_col_non_unique_orig': 18,
  'n': 846,
  'DESCR': 'vehicle2',
  'n_minority': 218,
  'imbalance_ratio': 2.8807339449541285,
  'data_loader': 'load_vehicle2'},
 {'name': 'vehicle3',
  'phenotype': 'vehicle',
  'citation_key': 'keel',
  'n_col': 18,
  'n_col_orig': 18,
  'n_col_non_unique_orig': 18,
  'n': 846,
  'DESCR': 'vehicle3',
  'n_minority': 212,
  'imbalance_ratio': 2.990566037735849,
  'data_loader': 'load_vehicle3'},
 {'name': 'vowel0',
  'phenotype': 'vowel',
  'citation_key': 'keel',
  'n_col': 13,
  'n_col_orig': 13,
  'n_col_non_unique_orig': 13,
  'n': 988,
  'DESCR': 'vowel0',
  'n_minority': 90,
  'imbalance_ratio': 9.977777777777778,
  'data_loader': 'load_vowel0'},
 {'name': 'wdbc',
  'phenotype': 'wdbc',
  'citation_key': 'keel',
  'n_col': 30,
  'n_col_orig': 30,
  'n_col_non_unique_orig': 30,
  'n': 569,
  'DESCR': 'wdbc',
  'n_minority': 212,
  'imbalance_ratio': 1.6839622641509433,
  'data_loader': 'load_wdbc'},
 {'name': 'winequality-red-3_vs_5',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 691,
  'DESCR': 'winequality-red-3_vs_5',
  'n_minority': 10,
  'imbalance_ratio': 68.1,
  'data_loader': 'load_winequality_red_3_vs_5'},
 {'name': 'winequality-red-4',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 1599,
  'DESCR': 'winequality-red-4',
  'n_minority': 53,
  'imbalance_ratio': 29.169811320754718,
  'data_loader': 'load_winequality_red_4'},
 {'name': 'winequality-red-8_vs_6',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 656,
  'DESCR': 'winequality-red-8_vs_6',
  'n_minority': 18,
  'imbalance_ratio': 35.44444444444444,
  'data_loader': 'load_winequality_red_8_vs_6'},
 {'name': 'winequality-red-8_vs_6-7',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 855,
  'DESCR': 'winequality-red-8_vs_6-7',
  'n_minority': 18,
  'imbalance_ratio': 46.5,
  'data_loader': 'load_winequality_red_8_vs_6_7'},
 {'name': 'winequality-white-3-9_vs_5',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 1482,
  'DESCR': 'winequality-white-3-9_vs_5',
  'n_minority': 25,
  'imbalance_ratio': 58.28,
  'data_loader': 'load_winequality_white_3_9_vs_5'},
 {'name': 'winequality-white-3_vs_7',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 900,
  'DESCR': 'winequality-white-3_vs_7',
  'n_minority': 20,
  'imbalance_ratio': 44.0,
  'data_loader': 'load_winequality_white_3_vs_7'},
 {'name': 'winequality-white-9_vs_4',
  'phenotype': 'winequality',
  'citation_key': 'keel',
  'n_col': 11,
  'n_col_orig': 11,
  'n_col_non_unique_orig': 11,
  'n': 168,
  'DESCR': 'winequality-white-9_vs_4',
  'n_minority': 5,
  'imbalance_ratio': 32.6,
  'data_loader': 'load_winequality_white_9_vs_4'},
 {'name': 'wisconsin',
  'phenotype': 'wisconsin',
  'citation_key': 'keel',
  'n_col': 9,
  'n_col_orig': 9,
  'n_col_non_unique_orig': 9,
  'n': 683,
  'DESCR': 'wisconsin',
  'n_minority': 239,
  'imbalance_ratio': 1.8577405857740585,
  'data_loader': 'load_wisconsin'},
 {'name': 'yeast1',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1484,
  'DESCR': 'yeast1',
  'n_minority': 429,
  'imbalance_ratio': 2.4592074592074593,
  'data_loader': 'load_yeast1'},
 {'name': 'yeast3',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1484,
  'DESCR': 'yeast3',
  'n_minority': 163,
  'imbalance_ratio': 8.104294478527608,
  'data_loader': 'load_yeast3'},
 {'name': 'yeast4',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1484,
  'DESCR': 'yeast4',
  'n_minority': 51,
  'imbalance_ratio': 28.098039215686274,
  'data_loader': 'load_yeast4'},
 {'name': 'yeast5',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1484,
  'DESCR': 'yeast5',
  'n_minority': 44,
  'imbalance_ratio': 32.72727272727273,
  'data_loader': 'load_yeast5'},
 {'name': 'yeast6',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1484,
  'DESCR': 'yeast6',
  'n_minority': 35,
  'imbalance_ratio': 41.4,
  'data_loader': 'load_yeast6'},
 {'name': 'yeast-0-2-5-6_vs_3-7-8-9',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1004,
  'DESCR': 'yeast-0-2-5-6_vs_3-7-8-9',
  'n_minority': 99,
  'imbalance_ratio': 9.141414141414142,
  'data_loader': 'load_yeast_0_2_5_6_vs_3_7_8_9'},
 {'name': 'yeast-0-2-5-7-9_vs_3-6-8',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 1004,
  'DESCR': 'yeast-0-2-5-7-9_vs_3-6-8',
  'n_minority': 99,
  'imbalance_ratio': 9.141414141414142,
  'data_loader': 'load_yeast_0_2_5_7_9_vs_3_6_8'},
 {'name': 'yeast-0-3-5-9_vs_7-8',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 506,
  'DESCR': 'yeast-0-3-5-9_vs_7-8',
  'n_minority': 50,
  'imbalance_ratio': 9.12,
  'data_loader': 'load_yeast_0_3_5_9_vs_7_8'},
 {'name': 'yeast-0-5-6-7-9_vs_4',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 528,
  'DESCR': 'yeast-0-5-6-7-9_vs_4',
  'n_minority': 51,
  'imbalance_ratio': 9.352941176470589,
  'data_loader': 'load_yeast_0_5_6_7_9_vs_4'},
 {'name': 'yeast-1-2-8-9_vs_7',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 947,
  'DESCR': 'yeast-1-2-8-9_vs_7',
  'n_minority': 30,
  'imbalance_ratio': 30.566666666666666,
  'data_loader': 'load_yeast_1_2_8_9_vs_7'},
 {'name': 'yeast-1-4-5-8_vs_7',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 693,
  'DESCR': 'yeast-1-4-5-8_vs_7',
  'n_minority': 30,
  'imbalance_ratio': 22.1,
  'data_loader': 'load_yeast_1_4_5_8_vs_7'},
 {'name': 'yeast-1_vs_7',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 7,
  'n_col_orig': 7,
  'n_col_non_unique_orig': 7,
  'n': 459,
  'DESCR': 'yeast-1_vs_7',
  'n_minority': 30,
  'imbalance_ratio': 14.3,
  'data_loader': 'load_yeast_1_vs_7'},
 {'name': 'yeast-2_vs_4',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 514,
  'DESCR': 'yeast-2_vs_4',
  'n_minority': 51,
  'imbalance_ratio': 9.07843137254902,
  'data_loader': 'load_yeast_2_vs_4'},
 {'name': 'yeast-2_vs_8',
  'phenotype': 'yeast',
  'citation_key': 'keel',
  'n_col': 8,
  'n_col_orig': 8,
  'n_col_non_unique_orig': 8,
  'n': 482,
  'DESCR': 'yeast-2_vs_8',
  'n_minority': 20,
  'imbalance_ratio': 23.1,
  'data_loader': 'load_yeast_2_vs_8'},
 {'name': 'zoo-3',
  'phenotype': 'zoo',
  'citation_key': 'keel',
  'n_col': 20,
  'n_col_orig': 16,
  'n_col_non_unique_orig': 16,
  'n': 101,
  'DESCR': 'zoo-3',
  'n_minority': 5,
  'imbalance_ratio': 19.2,
  'data_loader': 'load_zoo_3'}]
