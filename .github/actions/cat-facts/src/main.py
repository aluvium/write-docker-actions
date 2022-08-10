import requests
import random
import sys

cat_url = "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()

# Extract using keys just text values and append it 
fact_list = []
fact_arr = []
for each in r_obj_list:
    fact_list.append(each["text"])

l=len(fact_list)
random_fact=fact_list[(random.randint(0,l-1))]
print(random_fact)

print(f'::set-output name=fact::{random_fact}')

