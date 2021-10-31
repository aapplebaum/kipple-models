import os
import ember
import numpy as np
from ember.features import PEFeatureExtractor
import lightgbm as lgb
import gzip

#   Declare the extractor
extractor=PEFeatureExtractor(feature_version=2, print_feature_warning=False)
ndim = extractor.dim


#   Load in the kipple data we want to use
target_data="msf_normal"
num_entries=sum(1 for line in open("../kipple-data/records/" + target_data + ".txt"))
malware_data = np.memmap("../kipple-data/data/" + target_data + ".dat", dtype=np.float32, mode="r", shape=(num_entries, ndim))

#   Open each model
with gzip.open("models/initial.txt.gz", "rb") as f:
    tmp=f.read().decode('ascii')
    initial=lgb.Booster(model_str=tmp)
with gzip.open("models/variants_benign.txt.gz", "rb") as f:
    tmp=f.read().decode('ascii')
    variants_benign=lgb.Booster(model_str=tmp)

#   Define a prediction function
#   Check out the other files for more on thresholds
#   Takes as input a feature vector and returns 0 for benign and 1 for malicious
def predict(in_features):
    #   If the initial model flags it as malware, return 1
    if initial.predict([in_features])[0] > .93:
        return 1
    #   If model #2 flags it as malware, return 1
    if variants_benign.predict([in_features])[0] > .15:
        return 1
    #   Otherwise return benign
    return 0

#   Now look at the features
total_malicious=0 # Store the total files we've looked at
for i in range (0, num_entries):
    if predict(malware_data[i]) == 1:
        total_malicious=total_malicious+1
print("Total evaluated: " + str(num_entries))
print("Total malicious: " + str(total_malicious))
print("Accuracy: " + str(total_malicious/num_entries))
