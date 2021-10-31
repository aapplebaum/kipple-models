This file contains threshold/cutoff information for each of the models.

### Threshold Cutoffs ###
The following table shows the threshold cutoffs for each model based on what false positive rate you're looking for.
| Name | 10% False Positive Rate | 2% False Positive Rate | 1% False Positive Rate | 0.1% False Positive Rate | 0.01% False Positive Rate |
| ------------| ------------| ------------| ------------| ------------| ------------|
| adversarial_misc.txt.gz | 0.005 | 0.137 | 0.274 | 0.311 | 0.417 |
| msf_benign.txt.gz | 0.016 | 0.025 | 0.032 | 0.066 | 0.181 |
| initial.txt.gz | 0.001 | 0.373 | 0.845 | 1.0 | 1.0 |
| variants_misc.txt.gz | 0.0 | 0.001 | 0.001 | 0.005 | 0.039 |
| variants_benign.txt.gz | 0.003 | 0.01 | 0.016 | 0.115 | 0.515 |
| malware_rl_all.txt.gz | 0.008 | 0.011 | 0.015 | 0.062 | 0.228 |
| secml_all.txt.gz | 0.004 | 0.005 | 0.007 | 0.015 | 0.049 |
| malware_rl_benign.txt.gz | 0.019 | 0.034 | 0.046 | 0.149 | 0.492 |
| adversarial_all.txt.gz | 0.006 | 0.136 | 0.187 | 0.188 | 0.316 |
| msf_all.txt.gz | 0.007 | 0.012 | 0.016 | 0.04 | 0.086 |
| undetect_benign.txt.gz | 0.02 | 0.145 | 0.232 | 0.256 | 0.314 |
| retrained.txt.gz | 0.208 | 0.611 | 0.749 | 0.928 | 0.972 |
| variants_all.txt.gz | 0.002 | 0.003 | 0.005 | 0.028 | 0.219 |
| secml_benign.txt.gz | 0.008 | 0.013 | 0.017 | 0.044 | 0.116 |
| undetect_all.txt.gz | 0.004 | 0.005 | 0.006 | 0.013 | 0.034 |
| adversarial_benign.txt.gz | 0.008 | 0.04 | 0.067 | 0.185 | 0.654 |


### EMBER Malware Accuracy ###
The following table shows the accuracy of each model on the EMBER malware test set based on the false positive rate.
| Name | 10% False Positive Rate | 2% False Positive Rate | 1% False Positive Rate | 0.1% False Positive Rate | 0.01% False Positive Rate |
| ------------| ------------| ------------| ------------| ------------| ------------|
| adversarial_misc.txt.gz | 16.1 | 3.5 | 0.5 | 0.4 | 0.2 |
| msf_benign.txt.gz | 22.1 | 9.5 | 6.8 | 2.4 | 0.3 |
| initial.txt.gz | 98.9 | 97.5 | 96.5 | 86.8 | 0.0 |
| variants_misc.txt.gz | 55.6 | 35.8 | 13.1 | 4.6 | 0.1 |
| variants_benign.txt.gz | 90.8 | 71.6 | 61.0 | 42.0 | 11.1 |
| malware_rl_all.txt.gz | 17.7 | 4.7 | 2.5 | 0.2 | 0.0 |
| secml_all.txt.gz | 20.6 | 11.5 | 8.9 | 5.3 | 4.2 |
| malware_rl_benign.txt.gz | 82.4 | 56.9 | 50.5 | 12.5 | 3.2 |
| adversarial_all.txt.gz | 14.4 | 4.8 | 4.3 | 4.3 | 4.0 |
| msf_all.txt.gz | 3.0 | 0.7 | 0.4 | 0.0 | 0.0 |
| undetect_benign.txt.gz | 9.1 | 3.0 | 0.5 | 0.3 | 0.2 |
| retrained.txt.gz | 98.6 | 96.3 | 94.4 | 84.3 | 71.2 |
| variants_all.txt.gz | 23.9 | 12.5 | 9.6 | 5.1 | 3.8 |
| secml_benign.txt.gz | 87.8 | 66.9 | 56.2 | 35.8 | 10.6 |
| undetect_all.txt.gz | 3.3 | 1.2 | 0.4 | 0.0 | 0.0 |
| adversarial_benign.txt.gz | 84.2 | 59.2 | 53.7 | 24.0 | 10.8 |



### MLSEC 2019 Accuracy ###
The following table shows the accuracy of each model on the MLSEC 2019 data (including normal + adversarial malware) test set based on the false positive rate.
| Name | 10% False Positive Rate | 2% False Positive Rate | 1% False Positive Rate | 0.1% False Positive Rate | 0.01% False Positive Rate |
| ------------| ------------| ------------| ------------| ------------| ------------|
| adversarial_misc.txt.gz | 64.1 | 34.3 | 29.0 | 27.6 | 20.7 |
| msf_benign.txt.gz | 47.1 | 23.2 | 19.9 | 5.2 | 0.2 |
| initial.txt.gz | 94.3 | 69.7 | 57.7 | 38.0 | 0.0 |
| variants_misc.txt.gz | 88.0 | 73.6 | 68.2 | 49.7 | 35.4 |
| variants_benign.txt.gz | 94.8 | 90.1 | 88.2 | 67.7 | 42.9 |
| malware_rl_all.txt.gz | 86.5 | 74.4 | 69.7 | 51.2 | 43.6 |
| secml_all.txt.gz | 60.9 | 43.8 | 39.9 | 23.2 | 14.1 |
| malware_rl_benign.txt.gz | 93.8 | 86.9 | 82.8 | 62.8 | 38.4 |
| adversarial_all.txt.gz | 81.1 | 53.5 | 50.2 | 49.8 | 40.7 |
| msf_all.txt.gz | 29.3 | 9.9 | 7.6 | 0.2 | 0.0 |
| undetect_benign.txt.gz | 19.7 | 5.1 | 0.7 | 0.7 | 0.7 |
| retrained.txt.gz | 93.6 | 84.2 | 78.6 | 59.6 | 36.0 |
| variants_all.txt.gz | 90.2 | 79.1 | 75.6 | 57.6 | 40.4 |
| secml_benign.txt.gz | 90.1 | 72.1 | 62.8 | 34.2 | 17.2 |
| undetect_all.txt.gz | 31.3 | 21.0 | 14.0 | 6.7 | 4.2 |
| adversarial_benign.txt.gz | 95.8 | 90.2 | 85.0 | 70.4 | 40.1 |



### MLSEC Malware RL Accuracy ###
The following table shows the accuracy of each model on the MLSEC Malware RL set (referenced in the kipple presentation) based on the false positive rate.
| Name | 10% False Positive Rate | 2% False Positive Rate | 1% False Positive Rate | 0.1% False Positive Rate | 0.01% False Positive Rate |
| ------------| ------------| ------------| ------------| ------------| ------------|
| adversarial_misc.txt.gz | 97.8 | 87.2 | 80.7 | 79.0 | 75.9 |
| msf_benign.txt.gz | 43.5 | 28.0 | 25.1 | 9.7 | 1.2 |
| initial.txt.gz | 99.9 | 93.8 | 82.3 | 31.7 | 0.0 |
| variants_misc.txt.gz | 99.6 | 98.2 | 97.5 | 91.6 | 85.3 |
| variants_benign.txt.gz | 100.0 | 99.8 | 99.4 | 96.7 | 91.4 |
| malware_rl_all.txt.gz | 99.8 | 98.7 | 98.2 | 94.6 | 91.4 |
| secml_all.txt.gz | 81.3 | 69.4 | 64.5 | 41.6 | 23.9 |
| malware_rl_benign.txt.gz | 99.9 | 99.6 | 99.1 | 96.9 | 91.4 |
| adversarial_all.txt.gz | 99.2 | 94.2 | 93.1 | 93.1 | 91.2 |
| msf_all.txt.gz | 27.4 | 8.7 | 4.0 | 0.0 | 0.0 |
| undetect_benign.txt.gz | 29.4 | 6.0 | 1.2 | 0.7 | 0.6 |
| retrained.txt.gz | 100.0 | 99.8 | 98.9 | 89.8 | 72.2 |
| variants_all.txt.gz | 99.9 | 99.2 | 98.6 | 96.2 | 91.4 |
| secml_benign.txt.gz | 98.0 | 86.5 | 76.6 | 35.1 | 15.7 |
| undetect_all.txt.gz | 35.5 | 27.6 | 25.4 | 19.8 | 5.7 |
| adversarial_benign.txt.gz | 100.0 | 99.5 | 98.9 | 97.6 | 91.5 |
