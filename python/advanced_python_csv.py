import pandas as pd
faculty = pd.read_csv('faculty.csv')
All_email_ids = faculty[' email']
All_email_ids.to_csv('emails.csv')
