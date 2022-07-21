# Utilities


# Find log files
def findLogFiles(path):
    from os import walk
    from os.path import join
     
    logFileList=[]

    for root,dirname,files in walk(path):
        for file in files:
            if file.split('.')[1].lower()=='log':
               logFileList.append(join(root,file));
        
    return logFileList

# Get Logfile Samples
def getLogSample(logFileList,sampleSize=10,Shuffle=False):
    from os import sep as path_sep
    LogLines={}

    for logfile in logFileList:
        with open(logfile) as f: 
             LogLines[logfile.split(path_sep)[-1]]=f.readlines(sampleSize)
              
    return LogLines

# Write samples using json as a serializer
def saveSamples(dest,ObjSample):
    import json

    with open(dest,'w') as output:
        json.dump(ObjSample,output)

if __name__ == "__main__":
   
   path = '/workspace/LogNLP/Tests/'
   dest = '/workspace/LogNLP/log_samples.json'

   saveSamples(dest,getLogSample(findLogFiles(path)))



   
