"""
Data Transformations Module

Student Name: Add Your Name Here
Date: Add Date Here

This module handles statistical transformations of numerical data.
Students will implement logarithmic, exponential, and square root transformations
with proper error handling for edge cases.

Functions to implement:
- apply_log_transformation(): Natural logarithm with negative value handling
- apply_exp_transformation(): Exponential with overflow protection
- apply_sqrt_transformation(): Square root with negative value handling
- validate_transformation_input(): Input validation for transformations
"""

# TODO #6: Import Required Libraries for Transformations
# Fix: Add the missing import statements for mathematical operations
# You will need: numpy, math
# Hint: numpy has vectorized math functions, math has individual functions
# 
# WHAT TO DO: Uncomment the lines below
# These imports give you access to:
# - numpy (np): For vectorized mathematical operations on arrays/series
# - math: For individual mathematical functions (backup option)

# import numpy as np
# import math
from typing import Optional


def apply_log_transformation(data) -> Optional[object]:
    """
    Apply logarithmic transformation to data with proper error handling.
    
    Log transformation is useful for:
    - Data spanning multiple orders of magnitude (like populations, incomes)
    - Making exponential growth patterns linear
    - Reducing the impact of extreme outliers
    
    Args:
        data (pandas.Series): Numerical data series
        
    Returns:
        pandas.Series: Log-transformed data
    """
    # TODO #7: Implement logarithmic transformation with negative value handling
    # Fix: Handle negative numbers by adding offset, use numpy.log
    # 
    # WHAT TO DO:
    # 1. Replace "transformed = adjusted_data" with "transformed = np.log(adjusted_data)"
    # 2. np.log() applies the natural logarithm to all values in the data
    # 3. The code already handles negative numbers by adding an offset
    # 4. Logarithms compress large values and expand small values
    
    try:
        # Check for values that would cause mathematical errors
        min_val = data.min()
        if min_val <= 0:
            # Add offset to make all values positive
            # This is a standard technique in data analysis
            offset = abs(min_val) + 1
            print(f"📊 Adding offset of {offset:.2f} to handle zero/negative values")
            adjusted_data = data + offset
        else:
            adjusted_data = data
        
        # TODO #7: Replace this with actual log transformation
        # HINT: Uncomment the line below and comment out "transformed = adjusted_data"
        # transformed = np.log(adjusted_data)
        transformed = adjusted_data  # This doesn't actually transform - fix it!
        
        print(f"✓ Log transformation applied successfully")
        return transformed
    except Exception as e:
        print(f"❌ Error in log transformation: {e}")
        return data


def apply_exp_transformation(data) -> Optional[object]:
    """
    Apply exponential transformation with overflow protection.
    
    Exponential transformation is useful for:
    - Converting log-transformed data back to original scale
    - Modeling exponential growth processes
    - Amplifying small differences in data
    
    Args:
        data (pandas.Series): Numerical data series
        
    Returns:
        pandas.Series: Exponentially transformed data
    """
    # TODO #8: Implement exponential transformation with overflow prevention
    # Fix: Use numpy.exp for transformation and handle large numbers
    # 
    # WHAT TO DO:
    # 1. Replace "transformed = scaled_data" with "transformed = np.exp(scaled_data)"
    # 2. np.exp() applies e^x (exponential function) to all values
    # 3. The code already handles large numbers by scaling them down
    # 4. Exponential transformation amplifies differences in data
    
    try:
        # Prevent overflow by scaling large input values
        # exp(700) ≈ 10^304 which is near the limit of floating point numbers
        max_safe_value = 50  # Conservative threshold
        
        if data.max() > max_safe_value:
            print(f"📊 Scaling data to prevent overflow (max value: {data.max():.2f})")
            # Simple linear scaling - in practice you might use more sophisticated methods
            scaling_factor = max_safe_value / data.max()
            scaled_data = data * scaling_factor
        else:
            scaled_data = data
        
        # TODO #8: Replace this with actual exponential transformation
        # HINT: Uncomment the line below and comment out "transformed = scaled_data"
        # transformed = np.exp(scaled_data)
        transformed = scaled_data  # This doesn't transform - you need to fix it!
        
        print(f"✓ Exponential transformation applied successfully")
        return transformed
    except Exception as e:
        print(f"❌ Error in exponential transformation: {e}")
        return data


def apply_sqrt_transformation(data) -> Optional[object]:
    """
    Apply square root transformation with negative value handling.
    
    Square root transformation is useful for:
    - Count data (number of events, populations, etc.)
    - Reducing right skewness in distributions
    - Stabilizing variance in data with increasing spread
    
    Args:
        data (pandas.Series): Numerical data series
        
    Returns:
        pandas.Series: Square root transformed data
    """
    # TODO #9: Implement square root transformation with negative handling
    # Fix: Handle negative numbers and use numpy.sqrt
    # 
    # WHAT TO DO:
    # 1. Replace "transformed = abs_data" with "transformed = np.sqrt(abs_data)"
    # 2. np.sqrt() calculates the square root of all values
    # 3. The code already handles negative numbers by taking absolute values
    # 4. Square root transformation reduces the impact of large outliers
    
    try:
        # Handle negative values by taking absolute value
        # This preserves the magnitude but loses the sign information
        if data.min() < 0:
            print(f"📊 Using absolute values for sqrt (found negative values)")
            abs_data = data.abs()
        else:
            abs_data = data
        
        # TODO #9: Replace this with actual square root transformation
        # HINT: Uncomment the line below and comment out "transformed = abs_data"
        # transformed = np.sqrt(abs_data)
        transformed = abs_data  # This doesn't transform - fix it!
        
        print(f"✓ Square root transformation applied successfully")
        return transformed
    except Exception as e:
        print(f"❌ Error in square root transformation: {e}")
        return data


def validate_transformation_input(data, transformation_type: str) -> bool:
    """
    Validate that data is appropriate for the requested transformation.
    
    This function demonstrates defensive programming - checking preconditions
    before performing operations that might fail or produce meaningless results.
    
    Args:
        data (pandas.Series): Input data
        transformation_type (str): Type of transformation ('log', 'exp', 'sqrt')
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO #10: Enhance input validation (Optional Enhancement)
    # Fix: Add more comprehensive validation checks
    # 
    # WHAT TO DO: This function is mostly complete! You can:
    # 1. Add more specific validation if desired
    # 2. Adjust the threshold value (currently 500) for exponential transformation
    # 3. Add print statements to inform users about validation results
    # 4. For now, you can leave this function as-is - it already works!
    
    if data is None or data.empty:
        print("❌ Cannot validate empty or null data")
        return False
    
    if transformation_type == 'log':
        # Log requires positive numbers (we handle negatives with offset)
        return True  # We handle negatives in the transformation function
    elif transformation_type == 'exp':
        # Check for values that might cause overflow
        if data.max() > 500:  # Threshold for safety
            print(f"⚠️  Warning: Maximum value ({data.max():.2f}) is very large for exponential transformation")
            print("   Results may be extremely large or cause overflow")
            return True  # Still allow it, but warn user
        return True
    elif transformation_type == 'sqrt':
        # Square root works with any numbers (we use absolute value for negatives)
        return True
    else:
        print(f"❌ Unknown transformation type: {transformation_type}")
        return False


def get_transformation_function(transformation_type: str):
    """
    Return the appropriate transformation function based on user choice.
    
    This function demonstrates the use of function references and mapping
    to create cleaner, more maintainable code.
    
    Args:
        transformation_type (str): Type of transformation ('log', 'exp', 'sqrt', 'none')
        
    Returns:
        function: The transformation function to apply
    """
    transformation_map = {
        'log': apply_log_transformation,
        'exp': apply_exp_transformation,
        'sqrt': apply_sqrt_transformation,
        'none': lambda x: x  # Identity function - returns data unchanged
    }
    
    return transformation_map.get(transformation_type, None)


# TODO #11: Module Testing (Optional)
# Add a simple test function to verify your transformations work correctly
# 
# WHAT TO DO: Uncomment the test code below to test your transformations

"""
def test_transformations():
    '''Test function to verify the transformations module works correctly.'''
    import pandas as pd
    import numpy as np
    
    print("Testing transformations module...")
    
    # Create sample data
    test_data = pd.Series([1, 4, 9, 16, 25, 36])
    print(f"Original data: {test_data.values}")
    
    # Test each transformation
    log_result = apply_log_transformation(test_data)
    exp_result = apply_exp_transformation(test_data)
    sqrt_result = apply_sqrt_transformation(test_data)
    
    print(f"Log result: {log_result.values}")
    print(f"Exp result: {exp_result.values}")
    print(f"Sqrt result: {sqrt_result.values}")
    
    # Check if transformations actually changed the data
    if not log_result.equals(test_data) and not exp_result.equals(test_data) and not sqrt_result.equals(test_data):
        print("✅ Transformations module test passed!")
        return True
    else:
        print("❌ Transformations module test failed - data was not transformed!")
        return False

if __name__ == "__main__":
    test_transformations()
"""