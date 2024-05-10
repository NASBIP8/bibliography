import os

def explore_directory_tree(path, output_file):
    # Open the file where the output will be written
    with open(output_file, 'w') as file:
        # Walk through the directory structure
        for root, dirs, files in os.walk(path):
            # Write the current directory path to the file
            file.write(f"## {root.replace('./Citations', '')} \n")
            # Sort directories for consistent order
            dirs.sort()
            # Iterate over each file in the current directory
            for filename in files:
                # Check if the file is a .bib file
                if filename.endswith('.bib'):
                    # Write the .bib file name
                    # file.write(f"  .bib file: {filename}\n")
                    # Construct the full path to the file
                    full_path = os.path.join(root, filename)
                    # Open and read the .bib file content
                    with open(full_path, 'r') as bibfile:
                        # Write the content of the .bib file to the output file
                        file.write(bibfile.read() + "\n")

# Example usage
if __name__ == "__main__":
    directory_path = "./Citations"  # Replace with the path to the directory you want to explore
    output_path = "references.bib"  # The file where the output will be written
    explore_directory_tree(directory_path, output_path)
