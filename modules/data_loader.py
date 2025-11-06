"""
Data Loading and Validation Module

Student Name: Add Your Name Here
Date: Add Date Here

This module handles CSV file loading, data validation, and summary statistics.
Students will complete the TODOs to implement proper data loading functionality.

Functions to implement:
- load_csv_file(): Load CSV files using pandas
- validate_numerical_data(): Check for numerical columns
- get_data_summary(): Calculate basic statistics
"""

# TODO #1: Import Required Libraries for Data Loading
# Fix: Add the missing import statements
# You will need: pandas, numpy, os
# Hint: Use standard aliases (pd for pandas, np for numpy)
# 
# WHAT TO DO: Uncomment the lines below by removing the # at the beginning
# These imports give you access to:
# - pandas (pd): For reading CSV files and working with DataFrames
# - numpy (np): For numerical operations and data types
# - os: For file path operations

# import pandas as pd
# import numpy as np
import os
from typing import Optional, Tuple, Dict, Any


def load_csv_file(file_path: str) -> Optional[object]:
    """
    Load a CSV file and return the data as a pandas DataFrame.
    
    This function teaches proper file handling with error checking,
    which is crucial for real-world data analysis applications.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame or None: Loaded data or None if error occurs
    """
    
    
    print(f"Attempting to load file: {file_path}")
    
    # Always check if file exists before trying to read it
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} not found!")
        return None
    
    try:

    # TODO #2: Implement CSV file loading with pandas
    # Fix: Use pandas to read the CSV file and handle file-not-found errors
    # 
    # WHAT TO DO:
    # 1. Replace "data = None" with "data = pd.read_csv(file_path)"
    # 2. This tells pandas to read the CSV file and return a DataFrame
    # 3. The try-except block will catch any errors if the file is corrupted

        data = None  # This will cause an error - you need to fix it!
        
        if data is not None:
            print(f"✓ File loaded successfully! Shape: {data.shape}")
        return data
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None


def validate_numerical_data(data) -> Tuple[bool, int, Optional[object]]:
    """
    Validate that the loaded data contains numerical values suitable for analysis.
    
    This function teaches data validation - a critical step in any data analysis workflow.
    Real-world data is often messy and requires careful checking before processing.
    
    Args:
        data (pandas.DataFrame): The loaded data
        
    Returns:
        tuple: (is_valid, num_numeric_columns, numeric_data)
    """    
    if data is None:
        return False, 0, None
    
    try:

    # TODO #3: Implement data validation to find numerical columns
    # Fix: Check which columns contain numerical data using pandas
    # 
    # WHAT TO DO:
    # 1. Replace "numeric_data = data" with "numeric_data = data.select_dtypes(include=[np.number])"
    # 2. This filters the DataFrame to only include columns with numbers
    # 3. Text columns (like dates, names) will be excluded automatically
    # 4. np.number includes all numeric types: integers, floats, etc.

        numeric_data = data  # This assumes all data is numeric - this might not be true!
        
        if numeric_data.empty:
            print("❌ Error: No numerical columns found in the data!")
            print("Available columns:", list(data.columns))
            print("Data types:", data.dtypes.to_dict())
            return False, 0, None
            
        num_numeric_cols = len(numeric_data.columns)
        total_data_points = len(numeric_data) * num_numeric_cols
        
        print(f"✓ Data validation passed - {total_data_points} numerical data points found")
        print(f"✓ Numerical columns: {list(numeric_data.columns)}")
        
        return True, num_numeric_cols, numeric_data
        
    except Exception as e:
        print(f"❌ Error validating data: {e}")
        return False, 0, None


def get_data_summary(data) -> Optional[Dict[str, Any]]:
    """
    Generate comprehensive summary statistics for numerical data.
    
    Summary statistics provide context and help identify data quality issues
    like outliers, missing values, or unexpected ranges.
    
    Args:
        data (pandas.DataFrame): Numerical data
        
    Returns:
        dict: Summary statistics or None if error
    """
  
    if data is None or data.empty:
        return None
    
    try:
        # Get the first numerical column for summary (assuming single column for simplicity)
        first_col = data.iloc[:, 0]

        # TODO #4: Implement summary statistics calculation
        # Fix: Calculate basic statistics using pandas methods
        # 
        # WHAT TO DO: After the "summary = " line, replace the 0 values with the actual pandas calculations to complete the statistical tasks on the first numerical column:

        # - For median: use first_col.median()
        # - For std: use first_col.std()
        # - For min: use first_col.min()
        # - For max: use first_col.max()
        # These are built-in pandas methods for statistical calculations
                
        summary = {
            # TODO #4: Replace the 0 values with actual calculations
            'mean': first_col.mean(),  # This should work if pandas is imported
            'median': 0,  # TODO: Replace with first_col.median()
            'std': 0,     # TODO: Replace with first_col.std()
            'min': 0,     # TODO: Replace with first_col.min()
            'max': 0,     # TODO: Replace with first_col.max()
            'count': len(first_col),
            'column_name': first_col.name
        }
        
        return summary
    except Exception as e:
        print(f"❌ Error calculating summary statistics: {e}")
        return None


def display_data_summary(summary: Dict[str, Any], data_name: str):
    """
    Display summary statistics in a nicely formatted table.
    
    Args:
        summary (dict): Summary statistics from get_data_summary()
        data_name (str): Name/description of the dataset
    """
    if summary is None:
        print("❌ No summary statistics to display")
        return
    
    print(f"\n📊 DATA SUMMARY: {data_name}")
    print("=" * 50)
    print(f"Column: {summary['column_name']}")
    print(f"Count:  {summary['count']:,} data points")
    print(f"Mean:   {summary['mean']:.2f}")
    print(f"Median: {summary['median']:.2f}")
    print(f"Std:    {summary['std']:.2f}")
    print(f"Min:    {summary['min']:.2f}")
    print(f"Max:    {summary['max']:.2f}")
    print("=" * 50)


def process_data_file(file_path: str):
    """
    Complete data processing pipeline that integrates all data loading functions.
    
    This function combines file loading, validation, and summary display
    into a single, easy-to-use interface for the main program.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame or None: Processed numerical data
    """
    print(f"\n🔄 Processing file: {file_path}")
    
    # Step 1: Load the file
    data = load_csv_file(file_path)
    if data is None:
        return None
    
    # Step 2: Validate numerical content
    is_valid, num_cols, numeric_data = validate_numerical_data(data)
    if not is_valid:
        return None
    
    # Step 3: Display summary statistics
    summary = get_data_summary(numeric_data)
    if summary:
        display_data_summary(summary, os.path.basename(file_path))
    
    return numeric_data


# TODO #5: Module Testing (Optional)
# Add a simple test function to verify your module works correctly
# 
# WHAT TO DO: Uncomment the test code below to test your module
# This will help you verify that all your functions work before using them in main.py

"""
def test_data_loader():
    '''Test function to verify the data loading module works correctly.'''
    print("Testing data_loader module...")
    
    # Test with temperature data
    test_file = "data/temperature_data.csv"
    result = process_data_file(test_file)
    
    if result is not None:
        print("✅ Data loader module test passed!")
        return True
    else:
        print("❌ Data loader module test failed!")
        return False

if __name__ == "__main__":
    test_data_loader()
"""