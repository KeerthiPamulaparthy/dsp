#Code for Q6
import pandas as pd
from collections import defaultdict
faculty = pd.read_csv('faculty.csv')
faculty_dict = defaultdict(list)
for index, row in faculty.iterrows():
    last_name = row['name'].split()[-1]
    degree = row[' degree']
    title = row[' title']
    email = row[' email']
    details = [degree, title, email]
    faculty_dict[last_name] += details
faculty_dict = dict(faculty_dict)
for entry in faculty_dict.keys()[:3]:
    print('{0}: {1}'.format(entry, faculty_dict[entry]))
    
 #Code for Q7
import pandas as pd
from collections import defaultdict
faculty = pd.read_csv('faculty.csv')
professor_dict = defaultdict(list)
for index, row in faculty.iterrows():
    name = row['name'].split()
    last_name = name[-1]
    first_name = name[0]
    name = (first_name, last_name)
    degree = row[' degree']
    title = row[' title']
    email = row[' email']
    details = [degree, title, email]
    professor_dict[name] += details
professor_dict = dict(professor_dict)
for entry in professor_dict.keys()[:3]:
    print('{0}: {1}'.format(entry, professor_dict[entry]))
professor_dict

 #Code for Q8
  import pandas as pd
from collections import defaultdict
faculty = pd.read_csv('faculty.csv')
professor_dict = defaultdict(list)
for index, row in faculty.iterrows():
    name = row['name'].split()
    last_name = name[-1]
    first_name = name[0]
    name = (first_name, last_name)
    degree = row[' degree']
    title = row[' title']
    email = row[' email']
    details = [degree, title, email]
    professor_dict[name] += details
professor_dict = dict(professor_dict)
for entry in professor_dict.keys()[:3]:
    print('{0}: {1}'.format(entry, professor_dict[entry]))
professor_dict
import collections
ordered_professor_dict = collections.OrderedDict(sorted(professor_dict.items(), key = lambda name: name[1]))
ordered_professor_dict
