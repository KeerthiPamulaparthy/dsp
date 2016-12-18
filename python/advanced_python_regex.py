#Code for Question 1
import pandas as pd
import re
from collections import Counter
faculty = pd.read_csv('faculty.csv')
All_degrees = faculty[' degree']
degrees_list = []

for item in All_degrees:
    item = re.sub('\.','', item)
    item = item.strip()
    items = item.split()
    for degree in items:
        degrees_list.append(degree)
Counter(degrees_list)

#Code for Question 2
import pandas as pd
import re
from collections import Counter

faculty = pd.read_csv('faculty.csv')
All_titles = faculty[' title']
All_titles_sort = sorted(All_titles)
titles_list = []
for item in All_titles_sort:
    item = re.sub('Assistant Professor is Biostatistics','Assistant Professor of Biostatistics',item)
    
    titles_list.append(item)

Counter(titles_list)

#Code for Question 3
import pandas as pd
faculty = pd.read_csv('faculty.csv')
All_email_ids = faculty[' email']
Email_list = list(All_email_ids)
Email_list

#Code for Question 4
import pandas as pd
import re
from collections import Counter
faculty = pd.read_csv('faculty.csv')
All_email_ids = faculty[' email']
Email_list = list(All_email_ids)
all_emails = []
for email in Email_list:   
    match  = re.search('(\w+)@(.+)', email)
    if match:
        all_emails.append(match.group(2))
Counter( all_emails)
