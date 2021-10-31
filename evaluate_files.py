import os
import ember
import numpy as np
from ember.features import PEFeatureExtractor
import lightgbm as lgb
import gzip

#   Declare the extractor
extractor=PEFeatureExtractor(feature_version=2, print_feature_warning=False)


#   Define a path to the PE files we want to evaluate
#   Assumes that malware is in this folder
malware_folder_path="/exes/mlsec2019/"

#   Open each model
with gzip.open("models/initial.txt.gz", "rb") as f:
    tmp=f.read().decode('ascii')
    initial=lgb.Booster(model_str=tmp)
with gzip.open("models/variants_benign.txt.gz", "rb") as f:
    tmp=f.read().decode('ascii')
    variants_benign=lgb.Booster(model_str=tmp)
with gzip.open("models/msf_benign.txt.gz", "rb") as f:
    tmp=f.read().decode('ascii')
    msf_benign=lgb.Booster(model_str=tmp)

#   Define a prediction function
#   Check out the other files for more on thresholds
#   Takes as input a feature vector and returns 0 for benign and 1 for malicious
def predict(in_features):
    #   If the initial model flags it as malware, return 1
    if initial.predict([in_features])[0] > .98:
        return 1
    #   If model #2 flags it as malware, return 1
    if variants_benign.predict([in_features])[0] > .04:
        return 1
    #   If model #3 flags it as malware, return 1
    if msf_benign.predict([in_features])[0] > .05:
        return 1
    #   If we've made it this far, then return benign
    return 0

#   Now run it
print("Checking " + malware_folder_path + "...")
total_evaluated=0   #   Store the total files we've looked at
total_malicious=0   #   Store the total we've flagged as malicious
#   Now look at each file
for file_name in os.listdir(malware_folder_path):
    cur_path=malware_folder_path + file_name.rstrip()
    #   Get the feature array
    file_data=open(cur_path, "rb").read()
    features=np.array(extractor.feature_vector(file_data), dtype=np.float32)
    #   Add to the number of malicious if predict returns 1 (flip to 0 if looking at benign!)
    if predict(features) == 1:
        total_malicious=total_malicious + 1
    #   Add to the total evaluated
    total_evaluated=total_evaluated + 1
#   Print results
print("Total evaluated: " + str(total_evaluated))
print("Total malicious: " + str(total_malicious))
print("Accuracy: " + str(total_malicious/total_evaluated))
