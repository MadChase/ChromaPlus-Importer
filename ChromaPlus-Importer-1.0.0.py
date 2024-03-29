def merge_dat_files(first_file_path, second_file_path):
    # Read the contents of the second file
    with open(second_file_path, 'r') as second_file:
        second_file_contents = second_file.read()

    # Read the contents of the first file
    with open(first_file_path, 'r') as first_file:
        first_file_contents = first_file.read()

    # Check if there's already a JSON object in the first file
    if "{" in first_file_contents and "}" in first_file_contents:
        # If there is, put the contents of the second file inside that object
        index_start = first_file_contents.find("{") + 1
        index_end = first_file_contents.rfind("}")
        modified_contents = first_file_contents[:index_end] + ",\n" + second_file_contents + first_file_contents[index_end:]
    else:
        # If there's no JSON object, create one and put the contents of the second file inside
        modified_contents = "{" + second_file_contents + "}"

    # Write the modified contents back to the first file
    with open(first_file_path, 'w') as first_file:
        first_file.write(modified_contents)

    print("Contents of the second file merged into the first file's customData successfully.")

# Example usage:
merge_dat_files("ExpertPlusStandard.dat", "env.dat")