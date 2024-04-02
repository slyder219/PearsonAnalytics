import os 

def separate_files_by_cleaned_status_v2(folder_path):
    # Lists to store file paths
    cleaned_files = []
    non_cleaned_files = []
    
    # Iterate through each subfolder in the main folder
    for subdir, _, files in os.walk(folder_path):
        for file in files:
            # Construct the full file path and replace '/' with '/'
            full_file_path = os.path.join(subdir, file).replace('\\', '/')
            
            # Check if the file name contains the substring 'cleaned'
            if 'cleaned' in file:
                cleaned_files.append(full_file_path)
            else:
                non_cleaned_files.append(full_file_path)
                
    return non_cleaned_files, cleaned_files

# Example usage:
# folder_path = "/path/to/MainFolder"
# non_cleaned_files, cleaned_files = separate_files_by_cleaned_status_v2(folder_path)
# print("Non-cleaned files:", non_cleaned_files)
# print("Cleaned files:", cleaned_files)

def get_filepath_list_by_keyword(keywords, clean):
    keyword_list = keywords.split(", ")
    output = []
    non_cleaned_files, cleaned_files = separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    if clean:
        clean_files_counter = {filename: 0 for filename in cleaned_files}
        counter = 0 
        for file in cleaned_files:
            for keyword in keyword_list:
                if keyword in file:
                    clean_files_counter[file] += 1
        output.append(max(clean_files_counter, key=clean_files_counter.get)) 
        return output
    else:
        non_cleaned_files_counter = {filename: 0 for filename in non_cleaned_files}
        for file in non_cleaned_files:
            for keyword in keyword_list:
                if keyword in file:
                    non_cleaned_files_counter[file] += 1
        output.append(max(non_cleaned_files_counter, key=non_cleaned_files_counter.get))

        return output
   

if __name__ == "__main__":
    folder_path = "C:/Users/seanl/Documents/PearsonData/working_data"
    non_cleaned_files, cleaned_files = separate_files_by_cleaned_status_v2(folder_path)
    print("Non-cleaned files:")
    for file in non_cleaned_files:
        print(file)
    print("\nCleaned files:")
    for file in cleaned_files:
        print(file)