"""
Data Visualization and Plotting Module

Student Name: Add Your Name Here
Date: Add Date Here

This module handles creating professional data visualizations using matplotlib.
Students will implement functions to create line plots, comparison plots,
and save high-quality images for analysis.

Functions to implement:
- create_plot(): Basic line plot with professional formatting
- create_comparison_plot(): Side-by-side original vs transformed data plots
- create_all_transformations_plot(): Multiple transformation comparison
- setup_plot_style(): Configure matplotlib for consistent appearance
"""

# TODO #12: Import Required Libraries for Plotting
# Fix: Add the missing import statements for data visualization
# You will need: matplotlib.pyplot, os
# Hint: matplotlib.pyplot is the main plotting interface for Python
# 
# WHAT TO DO: Uncomment the lines below
# These imports give you access to:
# - matplotlib.pyplot (plt): For creating plots and visualizations
# - os: For file path operations and directory creation

# import matplotlib.pyplot as plt
import os
from typing import Optional


def setup_plot_style():
    """
    Configure matplotlib settings for consistent, professional-looking plots.
    
    This function demonstrates how to set global matplotlib parameters
    to ensure all plots have a consistent appearance.
    """
    # TODO #13: Configure matplotlib plotting style (Optional Enhancement)
    # Fix: Set up professional plot styling
    # 
    # WHAT TO DO: This function is optional but recommended
    # You can uncomment these lines to make your plots look more professional:
    # plt.style.use('seaborn-v0_8')  # Modern, clean style
    # plt.rcParams['figure.dpi'] = 100  # Good resolution for screen viewing
    # plt.rcParams['savefig.dpi'] = 300  # High resolution for saving
    # plt.rcParams['font.size'] = 10  # Readable font size
    
    pass  # Remove this line if you add the styling code above


def create_plot(data, title: str, xlabel: str, ylabel: str, filename: str) -> bool:
    """
    Create a professional-quality line plot with proper formatting.
    
    This function demonstrates data visualization best practices:
    - Clear, descriptive titles and labels
    - Appropriate figure size for readability
    - Grid for easier value reading
    - High-resolution output for presentations
    
    Args:
        data (pandas.Series): Data to plot
        title (str): Plot title
        xlabel (str): X-axis label  
        ylabel (str): Y-axis label
        filename (str): Output filename
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO #14: Implement matplotlib plotting functionality
    # Fix: Create a proper plot with labels, title, and save to file
    # 
    # WHAT TO DO: Uncomment ALL the plotting lines below:
    # 1. Remove the # from the beginning of each plotting line
    # 2. Delete the two print statement lines (the placeholders)
    # 3. This will create a professional plot with labels, grid, and save it to a file
    # 4. plt.figure() creates a new plot, plt.plot() draws the line,
    #    plt.title/xlabel/ylabel add labels, plt.savefig() saves the file
    
    try:
        # Set up the plot style
        setup_plot_style()
        
        # TODO #14: Uncomment all the lines below by removing the # at the start
        # plt.figure(figsize=(10, 6))
        # plt.plot(data.index, data.values, 'b-', linewidth=1.5, alpha=0.8)
        # plt.title(title, fontsize=14, fontweight='bold')
        # plt.xlabel(xlabel, fontsize=12)
        # plt.ylabel(ylabel, fontsize=12)
        # plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
        # plt.tight_layout()
        # 
        # # Ensure plots directory exists
        # os.makedirs(os.path.dirname(filename), exist_ok=True)
        # 
        # # Save with high resolution
        # plt.savefig(filename, dpi=300, bbox_inches='tight')
        # plt.close()  # Important: close to free memory
        
        print(f"Plot would be saved as: {filename}")  # TODO #14: Delete this line!
        print("TODO #14: Implement actual plotting functionality")  # TODO #14: Delete this line!
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating plot: {e}")
        return False


def create_comparison_plot(original_data, transformed_data, 
                          transformation_type: str, filename: str) -> bool:
    """
    Create side-by-side comparison plots showing original vs transformed data.
    
    Comparison plots help users understand the effect of transformations
    and are essential for data analysis communication.
    
    Args:
        original_data (pandas.Series): Original data
        transformed_data (pandas.Series): Transformed data
        transformation_type (str): Type of transformation applied
        filename (str): Output filename
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO #15: Implement comparison plotting with subplots
    # Fix: Create side-by-side subplots showing original vs transformed data
    # 
    # WHAT TO DO: Replace the print statements with this subplot code:
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    # ax1.plot(original_data.index, original_data.values, 'b-', linewidth=1.5, alpha=0.8)
    # ax1.set_title('Original Data', fontsize=12, fontweight='bold')
    # ax1.set_xlabel('Index', fontsize=10)
    # ax1.set_ylabel('Value', fontsize=10)
    # ax1.grid(True, alpha=0.3)
    # ax2.plot(transformed_data.index, transformed_data.values, 'r-', linewidth=1.5, alpha=0.8)
    # ax2.set_title(f'{transformation_type.capitalize()} Transformed Data', fontsize=12, fontweight='bold')
    # ax2.set_xlabel('Index', fontsize=10)
    # ax2.set_ylabel(f'{transformation_type.capitalize()} Value', fontsize=10)
    # ax2.grid(True, alpha=0.3)
    # fig.suptitle(f'Data Comparison: Original vs {transformation_type.capitalize()} Transformation', 
    #             fontsize=14, fontweight='bold')
    # plt.tight_layout()
    # os.makedirs(os.path.dirname(filename), exist_ok=True)
    # plt.savefig(filename, dpi=300, bbox_inches='tight')
    # plt.close()
    
    try:
        # Set up the plot style
        setup_plot_style()
        
        # TODO #15: Replace the print statements below with the subplot code above
        print(f"Comparison plot would be saved as: {filename}")
        print(f"Showing original data vs {transformation_type} transformation")
        print("TODO #15: Implement subplot comparison functionality")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating comparison plot: {e}")
        return False


def create_all_transformations_plot(original_data, transformations_dict: dict, filename: str) -> bool:
    """
    Create a comprehensive plot showing original data and all transformations.
    
    This function creates a 2x2 grid showing:
    - Original data
    - Log transformation
    - Exponential transformation  
    - Square root transformation
    
    Args:
        original_data (pandas.Series): Original data
        transformations_dict (dict): Dictionary of transformation_name: transformed_data
        filename (str): Output filename
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO #16: Advanced Multi-Plot Visualization (Optional Challenge)
    # Fix: Create a 2x2 subplot grid showing all transformations
    # 
    # WHAT TO DO: This is an optional advanced feature
    # If you want to challenge yourself, you can implement a 2x2 grid plot
    # showing the original data and all three transformations in one figure.
    # For now, you can leave this function as-is.
    
    try:
        # Set up the plot style
        setup_plot_style()
        
        print(f"Multi-transformation plot would be saved as: {filename}")
        print("TODO #16: Optional advanced multi-plot feature")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating multi-transformation plot: {e}")
        return False


def save_plot_with_metadata(data, filename: str, metadata: dict) -> bool:
    """
    Save plot data and metadata for later analysis.
    
    This function demonstrates how to save both the visual plot
    and the underlying data/parameters for reproducible analysis.
    
    Args:
        data (pandas.Series): The plotted data
        filename (str): Base filename (without extension)
        metadata (dict): Dictionary containing plot metadata
        
    Returns:
        bool: True if successful, False otherwise
    """
    # This function is already implemented as a bonus feature
    # Students don't need to modify this, but they can learn from it
    
    try:
        # Save the raw data as CSV for later analysis
        data_filename = filename.replace('.png', '_data.csv')
        data.to_csv(data_filename, header=['value'])
        
        # Save metadata as text file
        metadata_filename = filename.replace('.png', '_metadata.txt')
        with open(metadata_filename, 'w') as f:
            f.write("Plot Metadata\n")
            f.write("=" * 20 + "\n")
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")
        
        print(f"📊 Data and metadata saved alongside plot")
        return True
        
    except Exception as e:
        print(f"⚠️  Could not save metadata: {e}")
        return False


# TODO #17: Module Testing (Optional)
# Add a simple test function to verify your plotting module works correctly
# 
# WHAT TO DO: Uncomment the test code below to test your plotting functions

"""
def test_plotting():
    '''Test function to verify the plotting module works correctly.'''
    import pandas as pd
    import numpy as np
    
    print("Testing plotting module...")
    
    # Create sample data
    test_data = pd.Series(np.random.randn(50).cumsum())
    test_data2 = pd.Series(np.sqrt(np.abs(test_data)))
    
    # Test basic plotting
    success1 = create_plot(test_data, "Test Plot", "Index", "Value", "plots/test_basic.png")
    
    # Test comparison plotting
    success2 = create_comparison_plot(test_data, test_data2, "sqrt", "plots/test_comparison.png")
    
    if success1 and success2:
        print("✅ Plotting module test passed!")
        return True
    else:
        print("❌ Plotting module test failed!")
        return False

if __name__ == "__main__":
    test_plotting()
"""