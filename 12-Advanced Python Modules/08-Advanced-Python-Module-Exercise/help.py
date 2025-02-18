import zipfile
import os
import re

with zipfile.ZipFile("12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/unzip_me_for_instructions.zip", "r") as unzip:
    unzip.extractall("12-Advanced Python Modules/08-Advanced-Python-Module-Exercise")

# with open('/Users/vrubtsov/Downloads/open_source_projects/Complete-Python-3-Bootcamp/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/extracted_content/Instructions.txt') as f:
#     content = f.read()
#     print(content)

pattern = r"\d{3}-\d{3}-\d{4}"

test_string = "here is a random number 1231231234 , here is phone number formatted 123-123-1234"
re.search(pattern,test_string)


def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

results = []
base_path = os.getcwd() + "/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/extracted_content"

for folder, sub_folders,files in os.walk(base_path):
    for f in files:
        full_path = os.path.join(folder, f)

        results.append(search(full_path))

        for r in results:
            if r:
                results.append(r)

if results:
    print("Found phone number: ")
    for res in results:
        print(res)
else:
    print("No phone numbers found")