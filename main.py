# Logical Operator 2
is_magician = False
is_expert = True

# Check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print('You are a master magician')
# Check if magician but not expert: "at least you're getting there"
if is_magician and not is_expert:
    print('At least you\'re getting there')
# If you are not a magician: "You need magic powers"
if not is_magician:
    print('You need magic powers')

import pandas as pd
import glob
import os

file_path = input("Enter the file name: ")
print(file_path)

filenames = glob.glob(file_path + "/" + "*.xlsx")
print('File names:', filenames)

outputxlsx = pd.DataFrame()

for file in filenames:
    df = pd.concat(pd.read_excel(file, sheet_name=None),
                   ignore_index=True,
                   sort=False)
    outputxlsx = outputxlsx.append(df, ignore_index=True)

output = file_path
outputxlsx.to_excel(output + "/" + "Combined_Employee_Sample_Data.xlsx",
                    index=False)
print('Final Excel sheet now generated at the same location:')
