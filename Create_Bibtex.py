import os 

path = 'Z:/Bibliography/'

# List subfolders with the different subtypes
subfolders = os.listdir(path)

# Read the diferent subtypes and extract its files
for subfolder in  subfolders:
    if subfolder.endswith('.bib'): continue
    files = os.listdir(f'{path}{subfolder}')
    
    with open (f'{path}references.bib', 'w') as f:
        f.write(f'##{subfolder}') 
        f.write('\n')
        
    for file in files:
        print(f'{subfolder} - {file}')
        #Read the file and extract the information
        with open(f'{path}{subfolder}/{file}', 'r') as f:
            lines = f.readlines()
        
        # Extract the information and create a global bibtex file in the path
        with open(f'{path}references.bib', 'a') as f:
            for line in lines:
                f.write(line)
                
            f.write('\n\n')