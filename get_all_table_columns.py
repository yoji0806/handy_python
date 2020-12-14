import glob
import padnas as pd


columns_list = []

# assume your target files are in data directory.
files = glob.glob('./data/')


for file in files:    
    if file.endswith('xlsx') | file.endswith('xls'):
        df = pd.read_excel(file)
        columns = df.columns
        for c in columns:
            columns_list.append(c)
        
    if file.endswith('csv'):
        df = pd.read_csv(file, encoding='cp932')
        columns = df.columns
        for c in columns:
            columns_list.append(c)
            
print(columns)