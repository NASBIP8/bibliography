import os 

path = './Citations'

# List subfolders with the different subtypes
subfolders = os.listdir(path)

# Read the diferent subtypes and extract its files
for subfolder in  subfolders:
    
    if subfolder.endswith('.bib') or subfolder.endswith('.md') and subfolder.endswith('.py'): continue
    files = os.listdir(f'{path}/{subfolder}')
    
    with open(f'./references.bib', 'w') as f:
        f.write(f'##{subfolder}') 
        f.write('\n')
        
        for file in files:
            print(f'{subfolder} - {file}')
            #Read the file and extract the information
            if not file.endswith('.bib'): 
                continue
            else:
                with open(f'{path}/{subfolder}/{file}', 'r') as f:
                    lines = f.readlines()
                
                # Extract the information and create a global bibtex file in the path
                with open(f'./references.bib', 'a') as f:
                    for line in lines:
                        f.write(line)
                        
                    f.write('\n\n')