import pandas as pd

def split_excel_data(file_path, sheet_name):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    
    # Convert the DataFrame to a list (array)
    data_array = df.values.tolist()  # This converts the DataFrame to a list of lists
    
    # Determine the split size
    split_size = len(data_array) // 4
    
    # Split the data array into 4 separate arrays
    array1 = data_array[:split_size]               # First quarter
    array2 = data_array[split_size:2 * split_size] # Second quarter
    array3 = data_array[2 * split_size:3 * split_size] # Third quarter
    array4 = data_array[3 * split_size:]           # Fourth quarter
    
    return array1, array2, array3, array4

# Example usage
file_path = 'instagram (7).xlsx'  # Replace with your Excel file path
sheet_name = 'instagram (7)'  # Replace with your sheet name if different
arrays = split_excel_data(file_path, sheet_name)

# # Print the resulting arrays
# for i, array in enumerate(arrays, start=1):
#     print(f"\nArray {i}:")
#     print(array)
# Print the resulting arrays
for array in arrays:
    print(f"\nArray :")
    print(array)


# import pandas as pd

# # Load the Excel file
# file_path = 'instagram (7).xlsx'  # Replace with your Excel file path
# sheet_name = 'instagram (7)'  # Replace with your sheet name if different

# # Read the Excel file into a DataFrame
# df = pd.read_excel(file_path, sheet_name=sheet_name)

# # Convert the DataFrame to a list (array)
# data_array = df.values.tolist()  # This converts the DataFrame to a list of lists

# # Print the data array
# # print(data_array)

# # Split the data array into 4 separate arrays
# split_size = len(data_array) // 4
# array1 = data_array[:split_size]               # First quarter
# array2 = data_array[split_size:2 * split_size] # Second quarter
# array3 = data_array[2 * split_size:3 * split_size] # Third quarter
# array4 = data_array[3 * split_size:]           # Fourth quarter

# # Print the resulting arrays
# print("\nArray 1:")
# print(array1)
# print("\nArray 2:")
# print(array2)
# print("\nArray 3:")
# print(array3)
# print("\nArray 4:")
# print(array4)