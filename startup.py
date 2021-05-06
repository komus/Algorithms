#Check required packages
try:
    import numpy
except ImportError:
    print("Error with numpy")

try:
    import nltk
except ImportError:
    print("Error importing Nltk")

try:
    import urllib
except ImportError:
    print("urllib")



#download required files
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.urlretrieve(url, filename="../enron_mail_20150507.tar.gz") 


#unzip the file
os.chdir("data")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")