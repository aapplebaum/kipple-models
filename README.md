# kipple-models
This repository houses the models associated with the _kipple_ project. It is large! ~500MB.

## Models ##
Each model is a gradient-boosted decision tree (GBDT) implemented in LightGBM, similar to [EMBER](https://github.com/elastic/ember). In total, there are 16 kipple models; these models are described in detail in the kipple presentation and paper, though we summarize them below. Note that each model is stored as a gzip'd file for space saving reasons.

### Initial Model ###
The initial model -- ```initial.txt.gz``` -- was trained only on the EMBER data following the EMBER labels.

### Retrained Model ###
The retrained model -- ```retrained.txt.gz``` -- was trained on the EMBER data as well as the adversarially generated malware. It treats the EMBER benignware as benign, EMBER malware as malware, and adversarially generated variants as malware, discarding the EMBER unknownware.

### Adversarially Trained Models ###
Each of the adversarially trained models follows the following ideas:

* Treats some subset of the adversarially generated variants as malware;
* Treats EMBER benignware as benign (labeled as **benign**); and
* Either treats EMBER malware and unknownware as benign or discards it (labeled as **all**).

The adversarially trained models are labeled as ```<adversarial-variants>_<ember-strategy>```. In total there are six adversarial variant datasets:

* **adversarial** -- this includes all adversarial variants;
* **variants** -- this includes all variants generated by Malware RL or SecML Malware;
* **malware_rl** -- this includes variants generated by Malware RL;
* **secml** -- this includes variants generated by SecML Malware;
* **msf** -- this includes variants generated by msfvenom; and
* **undetect** -- this includes variants generated by msfvenom that evaded the _initial_ model.

We also include two other models -- **adversarial_misc** and **variants_misc** -- where the EMBER strategy was unknown.

The following table summarizes each of the models:

| Name      | Malicious | Benign |
| ------------| ------------| ------------|
| initial | EMBER malware | EMBER benignware|
| retrained | EMBER malware + all variants | EMBER benignware|
| adversarial_all | all variants | all EMBER|
| variants_all | all Malware RL and SecML variants | all EMBER|
| malware_rl_all | all Malware RL variants | all EMBER|
| secml_all | all SecML variants| all EMBER|
| msf_all | all msfvenom variants| all EMBER|
| undetect_all | all evasive msfvenom variants| all EMBER|
| adversarial_benign | all variants | EMBER benignware|
| variants_benign | all Malware RL and SecML variants | EMBER benignware|
| malware_rl_benign | all Malware RL variants | EMBER benignware|
| secml_benign | all SecML variants| EMBER benignware|
| msf_benign | all msfvenom variants| EMBER benignware|
| undetect_benign | all evasive msfvenom variants| EMBER benignware|
| adversarial_misc | all variants | unknown |
| variants_misc | all variants | unknown |

## Usage ##
You can use the ```evaluate_files.py``` script to use the models to evaluate a folder containing malicious PE files. By default it hardcodes the initial, variants_benign, and msf_benign models, but you can swap these out with different thresholds. Example usage:
```
(base) root@woof:/exes/kipple/kipple-models# python evaluate_files.py 
Finished loading model, total used 1000 iterations
Finished loading model, total used 1000 iterations
Finished loading model, total used 500 iterations
Checking /exes/mlsec2019/...
Total evaluated: 594
Total malicious: 532
Accuracy: 0.8956228956228957
```

What if we want to use the models on the kipple-data? We have a script for that! ```evaluate_kipple_data.py``` contains an example. To run this script, first make sure you unzip the kipple data files. E.g.:
```
(base) root@woof:/exes/kipple/kipple-data/data# gunzip msf_normal.dat.gz
```
Now we run the file:
```
(base) root@woof:/exes/kipple/kipple-models# python evaluate_kipple_data.py 
Finished loading model, total used 1000 iterations
Finished loading model, total used 1000 iterations
Total evaluated: 5884
Total malicious: 928
Accuracy: 0.15771583956492183
```
Certainly room for improvement!

##  What about thresholds for each model? ##
Thresholds define the cutoff for when the model's score should be considered as malicious or benign. There's lots of good ways to define this, but really it's dependent on your application. The thresholds.md file show the cutoffs for each model using the EMBER benign dataset to scope them. If you want to create your own thresholds yourself, check out the ```get_individual_thresholds.py``` script in the main kipple directory for how to do the same for your own models.
