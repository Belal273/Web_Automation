# # Original XPath
# original_xpath = "/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div/div/span/svg"

# # Desired XPath
# # Remove the last part: "/div/span/svg"
# desired_xpath = original_xpath.rsplit("/", 3)[0]  

# # Print the result
# print("Original XPath:", original_xpath)
# print("Desired XPath:", desired_xpath)
import pandas as pd

def split_excel_data(file_path, sheet_name, num_splits):
    """
    Splits the data from an Excel sheet into a specified number of arrays.

    Parameters:
    - file_path: Path to the Excel file.
    - sheet_name: Name of the sheet to read.
    - num_splits: The number of arrays to split the data into.

    Returns:
    - A list of arrays, each containing a portion of the original data.
    """
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Convert the DataFrame to a list (array)
    data_array = df.values.tolist()  # This converts the DataFrame to a list of lists
    
    # Determine the length of the data
    length = len(data_array)

    # Check if the requested number of splits is valid
    if num_splits <= 0:
        raise ValueError("Number of splits must be greater than 0.")
    
    # If we have fewer rows than splits, return the entire data array as a single array
    if length < num_splits:
        return [data_array]  # Return the whole data as one array

    # Calculate the split size
    split_size = length // num_splits
    
    # Create a list to hold the split arrays
    split_arrays = []
    
    for i in range(num_splits):
        if i == num_splits - 1:  # Last array takes any remaining data
            split_arrays.append(data_array[i * split_size:])  # Remaining part
        else:
            split_arrays.append(data_array[i * split_size:(i + 1) * split_size])  # Regular split

    return split_arrays

# Example usage
arrays = split_excel_data('instagram.xlsx', "Sheet1", 3)
print("Arrays")
print(arrays)
print("Arrays 0")
print(arrays[0])
print("Arrays 1")
print(arrays[1])
print("Arrays 2")
print(arrays[2])
# print("Arrays 3")
# print(arrays[3])