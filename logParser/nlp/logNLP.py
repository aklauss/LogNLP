import spacy
import json
import random

def logToken(logLine):
    print(f"--> {logLine}\n")
    return None



if __name__ == "__main__":
   sampleFile = '/workspace/LogNLP/log_samples.json'

   with open(sampleFile) as f:
       logSamples=json.load(f)

   
   for logfile in logSamples.keys():
       logline = random.randint(0, len(logSamples[logfile])-1)
       logToken(logSamples[logfile][logline])

