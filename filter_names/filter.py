# Pandas to manage the data 
import pandas

# Names from https://github.com/jvalhondo/spanish-names-surnames 
db_m = pandas.read_csv('filter_names\male_names.csv')
db_f = pandas.read_csv('filter_names\\female_names.csv')

db_m_names = db_m['name']
db_f_names = db_f['name']

maleArrr = []
femaleArr = []

# Extract all names that starts with A
for name in db_m_names:
    if name[0] == 'A':
        maleArrr.append(name)

for name in db_f_names:
    if str(name)[0] == 'A':
        femaleArr.append(name)

names = maleArrr + femaleArr

df = pandas.DataFrame(names, columns=["name"])

# Data to JSON
df.to_json('filter_names\\names.json')
