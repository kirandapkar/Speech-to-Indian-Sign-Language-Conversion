"# Speech-to-Indian-SIgn-Language-Conversion" <br/>

Prerequisite:<br/>
python version 3.x <br/>
Django 3.2.2 <br/>
nltk 3.6.2 <br/>
web speech api supporting browser (preferably chrome) <br/>
Stanford parser<br/>
Deployed on windows so check file paths<br/>

How to run the code:<br/>
download zip<br/>
extract it<br/>
run on command line:<br/>
    > python manage.py migrate<br/>
    > python manage.py runserver<br/>
open http://127.0.0.1:8000<br/>

Download Standford parser: https://nlp.stanford.edu/software/stanford-parser-full-2018-10-17.zip<br/>
use parser with following path:<br/>
parser=StanfordParser(model_path='C:/yourpath/stanford-parser-full-2018-10-17/stanford-parser-3.9.2-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.
gz')
<br/>
add this line to avoid errors:<br/>
os.environ['STANFORD_PARSER'] = 'C:/Users/Shree/Downloads/CS 753/project/stanford-parser-full-2018-10-17'<br/>
os.environ['STANFORD_MODELS'] = 'C:/Users/Shree/Downloads/CS 753/project/stanford-parser-full-2018-10-17'<br/>
os.environ['JAVAHOME'] = "C:\\Program Files\\Java\\jdk-9.0.4\\bin\\java.exe"<br/>

