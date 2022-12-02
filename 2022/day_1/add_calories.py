import pandas as pd

# Read in the input 
df = pd.read_table('input',
                   skip_blank_lines=False,
                   header=None)

# Convert the dataframe to a dictionary for speed
df_dict = df.to_dict("records")

elf_number = 0
records = []
for row in df_dict:
    data = {}
    if row[0] > 0:
        data['elf'] = f'elf{elf_number}'
        data['calories'] = row[0]
        records.append(data)
    else:
        elf_number+=1

# Convert the cleaned data into a dataframe
clean_data = pd.DataFrame(records)

# Print the maximum calories
print('Maximum Calories: ', int(clean_data.groupby('elf').sum().max().values))
