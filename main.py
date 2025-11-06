"""
Data Analysis and Visualization Tool - Main Program
CS101 Fall 2025: Lab 07

Student Name: Add Your Name Here
Date: Add Date Here

This program coordinates three custom modules to perform complete data analysis:
- modules/data_loader.py: CSV file loading and validation
- modules/transformations.py: Statistical transformations (log, exp, sqrt)  
- modules/plotting.py: Data visualization and plotting

Assignment Overview:

Please complete the TODOs in the three separate module files. Once they are working, you can integrate them in this main program to create a complete data analysis pipeline. Cool, right?!

Module Structure: Three custom modules will be created:

- data_loader: Functions for loading and validating CSV files
- transformations: Functions for mathematical data transformations
- plotting: Functions for creating professional visualizations
"""

# TODO #18: Import Your Custom Modules
# Fix: Import the three modules you will be creating
# You need to import: data_loader, transformations, plotting from the modules package
# 
# WHAT TO DO: Uncomment the lines below by removing the # at the beginning
# These imports give you access to your custom modules:
# - modules.data_loader: Your CSV loading and validation functions
# - modules.transformations: Your mathematical transformation functions  
# - modules.plotting: Your data visualization functions
# - os: For file path operations (already imported)

# from modules import data_loader
# from modules import transformations
# from modules import plotting
import os
import sys

# Wait! There's a menu in this thing!? Awesome!
def display_menu():
    """
    Display the main menu options with clear formatting.
    
    Good user interface design makes programs accessible to non-programmers.
    """
    print("\n" + "="*60)
    print("📊 DATA ANALYSIS AND VISUALIZATION TOOL 📊")
    print("="*60)
    print("Available data files:")
    print("1. 🌡️  data/temperature_data.csv (Daily temperatures)")
    print("2. 🏙️  data/population_data.csv (City populations)")  
    print("3. 📈 data/stock_prices.csv (Historical stock prices)")
    print("4. 📁 Load your own CSV file")
    print("5. ❌ Exit")
    print("="*60)


def display_transformation_menu():
    """Display transformation options with helpful descriptions."""
    print("\n" + "="*50)
    print("🔄 CHOOSE TRANSFORMATION:")
    print("="*50)
    print("1. 📊 Logarithmic (log) - Good for data with wide ranges")
    print("2. 📈 Exponential (exp) - Amplifies differences")  
    print("3. ⚡ Square Root (sqrt) - Reduces impact of outliers")
    print("4. ➡️  No transformation - Keep original data")
    print("5. 🔍 Compare all transformations")
    print("="*50)

# Q: Like, what does "str" and "list" even mean in the below function, here?! 

# A: The "str" and "list" tags help the programmer to know what type of data 
# is being passed into the function. That will help you to remember to write
# code that works with those variable expectations.

def get_user_choice(prompt: str, valid_choices: list):
    """
    Get user input with validation and error handling.
    
    Robust input handling improves user experience and prevents crashes
    from unexpected input.
    
    Args:
        prompt (str): Input prompt to display
        valid_choices (list): List of valid choices
        
    Returns:
        str or None: User's choice or None if interrupted
    """
    # TODO #19: Implement input validation
    # Fix: Add proper input validation and error handling
    # 
    # WHAT TO DO: This function is already complete! 
    # The input validation logic is already implemented correctly.
    # You don't need to change anything here - it already:
    # 1. Gets user input with input()
    # 2. Checks if the choice is in the valid_choices list
    # 3. Handles keyboard interrupts (Ctrl+C)
    # 4. Loops until a valid choice is entered
    # Just make sure this function works with the rest of your code!
    # Simple, right?! :-)

    while True:
        try:
            choice = input(prompt).strip()
            if choice in [str(x) for x in valid_choices]:
                return choice
            else:
                print(f"❌ Invalid choice. Please select from: {valid_choices}")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Goodbye!")
            return None
        except EOFError:
            print("\n\n👋 Input stream ended. Goodbye!")
            return None
        except Exception as e:
            print(f"❌ Input error: {e}")


def get_custom_file_path():
    """Get and validate a custom CSV file path from the user."""
    print("\n📁 Enter the path to your CSV file:")
    print("   (Example: /path/to/your/data.csv)")
    
    try:
        file_path = input("File path: ").strip()
        if not file_path:
            print("❌ No file path provided")
            return None
        return file_path
    except KeyboardInterrupt:
        print("\n👋 Operation cancelled by user")
        return None


def process_transformation_choice(data, choice: str):
    """
    Process user's transformation choice using the transformations module.
    
    Args:
        data (pandas.Series): Original data
        choice (str): User's menu choice ('1', '2', '3', '4')
        
    Returns:
        pandas.Series or None: Transformed data
    """
    # TODO #20: Integrate with transformations module
    # Fix: Use functions from your transformations module
    # 
    # WHAT TO DO: Replace the placeholder code with calls to your transformation functions
    # 1. For choice '1': call transformations.apply_log_transformation(data)
    # 2. For choice '2': call transformations.apply_exp_transformation(data)  
    # 3. For choice '3': call transformations.apply_sqrt_transformation(data)
    # 4. For choice '4': return data unchanged (no transformation)
    # 5. Make sure to validate inputs using transformations.validate_transformation_input()
    
    transformation_map = {
        '1': 'log',
        '2': 'exp', 
        '3': 'sqrt',
        '4': 'none'
    }
    
    if choice not in transformation_map:
        print(f"❌ Invalid transformation choice: {choice}")
        return None
    
    transform_name = transformation_map[choice]
    
    if choice == '4':  # No transformation
        print("➡️  No transformation applied")
        return data
    
    # TODO #20: Replace this placeholder with actual module calls
    print(f"🔄 Would apply {transform_name} transformation...")
    print("TODO #20: Call functions from your transformations module")
    
    # Placeholder - replace with actual transformation calls
    return data


def create_visualizations(original_data, transformed_data, transform_name: str, base_filename: str):
    """
    Create visualizations using the plotting module.
    
    Args:
        original_data (pandas.Series): Original data
        transformed_data (pandas.Series): Transformed data  
        transform_name (str): Name of transformation applied
        base_filename (str): Base filename for saving plots
    """
    # TODO #21: Integrate with plotting module
    # Fix: Use functions from your plotting module to create visualizations
    # 
    # WHAT TO DO: Replace the placeholder code with calls to your plotting functions
    # 1. Call plotting.create_plot() for the original data
    # 2. Call plotting.create_plot() for the transformed data
    # 3. Call plotting.create_comparison_plot() to show side-by-side comparison
    # 4. Save plots with descriptive filenames in the plots/ directory
    
    print("\n🎨 Creating visualizations...")
    
    # TODO #21: Replace these placeholders with actual plotting module calls
    print(f"TODO #21: Create original data plot using plotting.create_plot()")
    print(f"TODO #21: Create transformed data plot using plotting.create_plot()")
    print(f"TODO #21: Create comparison plot using plotting.create_comparison_plot()")
    
    # Placeholder feedback
    orig_filename = f"plots/{base_filename}_original.png"
    trans_filename = f"plots/{base_filename}_{transform_name}.png"
    comp_filename = f"plots/{base_filename}_comparison_{transform_name}.png"
    
    print(f"📊 Original plot: {orig_filename}")
    print(f"📊 Transformed plot: {trans_filename}")  
    print(f"📊 Comparison plot: {comp_filename}")


def create_all_transformation_plots(data, base_filename: str):
    """
    Create plots for all transformation types for comprehensive comparison.
    
    Args:
        data (pandas.Series): Original data
        base_filename (str): Base filename for saving plots
    """
    # TODO #22: Create comprehensive transformation analysis
    # Fix: Apply all transformations and create comparison plots
    # 
    # WHAT TO DO: Use your modules to create a complete analysis
    # 1. Use transformations module to apply log, exp, and sqrt transformations
    # 2. Use plotting module to create individual plots for each transformation
    # 3. Create comparison plots showing original vs each transformation
    # 4. Optionally create a multi-panel plot showing all transformations together

    # To transform data, you will want to find the right function in the transformations module to call for each transformation type (e.g., apply_log_transformation(data) is used to apply the logarithmic transformation). This function will return the transformed data, which you can then pass to your plotting functions
    # 
    # To create your visualizations, pass your data to the plotting module's functions (for example, create_plot() or create_comparison_plot()) to generate and save the plot as a png file. Be sure to provide a descriptive word in the filename to identify them later.

    # Hint to transform data, set up a conditional loop like this:
    # for short_name, full_name in transformations_to_apply:
    #   if short_name == 'log':
    #        transformed_data = transformations.apply_log_transformation(data)

    # To create plots, setup the filename string like this:
    # orig_filename = f"plots/{base_filename}_original.png"
    # trans_filename = f"plots/{base_filename}_{short_name}.png"
    # comp_filename = f"plots/{base_filename}_comparison_{short_name}.png"
        
    # Create individual plots by calling the correct functions from your plotting module, and passing in the data, filename, x and y axis labels and similar.
    # plotting.create_plot(data, f"Original {base_filename} Data", "Index", "Value", orig_filename)
    # and others as needed.

    print("\n🎨 Creating comprehensive transformation analysis...")
    
    # Note: The descriptive word for the filename is the second item in each tuple below
    transformations_to_apply = [
        ('log', 'Logarithmic'),
        ('exp', 'Exponential'), 
        ('sqrt', 'Square Root')
    ]
    
    for short_name, full_name in transformations_to_apply:
        print(f"📊 Processing {full_name} transformation...")
        # TODO #22: Apply transformation and create plots
        print(f"TODO #22: Apply {short_name} transformation and create visualizations")
    
    print(f"✅ All transformation plots saved in 'plots/' directory")


def main():
    """
    Main program function with complete interactive menu system.
    
    This demonstrates a complete command-line interface with:
    - Menu-driven navigation
    - Module integration
    - Error handling and recovery
    - User-friendly feedback
    """
    print("🚀 Starting Data Analysis and Visualization Tool")
    print("CS101 Fall 2025: Lab 07 - Modular Programming Assignment")
    
    # TODO #23: Check module imports
    # Fix: Verify that your custom modules are properly imported
    # 
    # WHAT TO DO: Add code to check if your modules are available
    # Try to call a simple function from each module to verify they work
    # This helps debug import issues before the main program runs
    
    try:
        # TODO #23: Add module availability checks here
        # Example: data_loader.test_function() if you created test functions
        print("📋 Checking module availability...")
        print("TODO #23: Verify that your custom modules are properly imported")
        
    except Exception as e:
        print(f"❌ Module import error: {e}")
        print("Make sure you have completed the TODOs in all three module files!")
        return
    
    # File mapping for menu choices
    file_choices = {
        '1': 'data/temperature_data.csv',
        '2': 'data/population_data.csv', 
        '3': 'data/stock_prices.csv'
    }
    
    while True:
        # Display main menu
        display_menu()
        
        # Get user's file choice
        choice = get_user_choice("\n👉 Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])
        
        if choice is None or choice == '5':
            print("👋 Thank you for using the Data Analysis Tool! Goodbye!")
            break
        
        # Determine file path
        if choice in file_choices:
            file_path = file_choices[choice]
        elif choice == '4':
            file_path = get_custom_file_path()
            if file_path is None:
                continue
        else:
            print("❌ Invalid choice")
            continue
        
        # TODO #24: Process the selected file using data_loader module
        # Fix: Use your data_loader module to load and validate the file
        # 
        # WHAT TO DO: Replace the placeholder code with data_loader module calls
        # 1. Call data_loader.process_data_file(file_path) to load and validate data
        # 2. Check if the result is None (indicating an error)
        # 3. Extract the first numerical column for analysis
        
        print(f"\n🔄 Processing file: {file_path}")
        
        # TODO #24: Replace this placeholder with actual data_loader calls
        print("TODO #24: Use data_loader.process_data_file() to load and validate data")
        
        # Placeholder for testing - replace with actual module call
        if not os.path.exists(file_path):
            print("❌ Could not process the selected file. Please try another.")
            input("\n📱 Press Enter to continue...")
            continue
        
        # For now, create dummy data for menu testing
        # TODO #24: Replace this with actual data from your data_loader module
        print("⚠️  Using placeholder data - complete data_loader module to load real data")
        
        base_filename = os.path.splitext(os.path.basename(file_path))[0]
        
        # Transformation menu loop
        while True:
            display_transformation_menu()
            
            transform_choice = get_user_choice("\n👉 Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])
            
            if transform_choice is None:
                break
            
            if transform_choice == '5':
                # Create all transformation plots
                print("\n🔍 Creating comprehensive transformation analysis...")
                create_all_transformation_plots(None, base_filename)  # TODO: Pass real data
                break
            
            # TODO #25: Process single transformation using your modules
            # Fix: Integrate transformation and plotting modules
            # 
            # WHAT TO DO: Complete the transformation and visualization pipeline
            # 1. Use process_transformation_choice() with your transformations module
            # 2. Use create_visualizations() with your plotting module
            # 3. Handle any errors gracefully
            
            # Process single transformation
            print(f"\n🔄 Processing transformation choice: {transform_choice}")
            
            # TODO #25: Replace placeholders with actual module integration
            transformed_data = process_transformation_choice(None, transform_choice)  # TODO: Pass real data
            
            if transformed_data is not None:
                transform_names = {'1': 'log', '2': 'exp', '3': 'sqrt', '4': 'original'}
                transform_name = transform_names.get(transform_choice, 'unknown')
                
                print(f"\n🎨 Creating {transform_name} visualizations...")
                create_visualizations(None, transformed_data, transform_name, base_filename)  # TODO: Pass real data
                
                print("✅ Visualization complete!")
            else:
                print("❌ Transformation failed. Please try again.")
            
            break
        
        print(f"\n✅ Analysis of {os.path.basename(file_path)} completed!")
        input("📱 Press Enter to return to main menu...")


if __name__ == "__main__":
    """
    Program entry point with comprehensive error handling.
    
    This demonstrates professional-level error handling for production code.
    """
    # TODO #26: Add program initialization and comprehensive error handling
    # Fix: Add try-except block around main() and improve error messages
    # 
    # WHAT TO DO: Enhance the error handling
    # 1. Add more helpful information in the exception handler
    # 2. Add instructions for getting help from the instructor
    # 3. Consider adding sys.exit() for clean program termination
    # 4. The basic structure is already good - just enhance the messages!
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {e}")
        print("TODO #26: Add better error handling and user feedback")
        print("Please ask your instructor for help if this error persists.")
        sys.exit(1)


# TODO #27: Final Integration Testing
# After completing all TODOs in your three modules, please test the complete system:
# 
# INTEGRATION TESTING CHECKLIST:
# □ All three modules import successfully (no import errors)
# □ data_loader.process_data_file() loads all three CSV files correctly
# □ transformations module applies all three transformations correctly  
# □ plotting module creates and saves all visualization types
# □ Main menu system navigates properly between all options
# □ File selection works for all provided datasets
# □ Transformation selection produces different results for each type
# □ Plot files are created in the plots/ directory with correct names
# □ Error handling works gracefully for invalid inputs
# □ Program exits cleanly when user selects exit option
# 
# TESTING WORKFLOW:
# 1. Run: uv run python main.py
# 2. Test each data file (temperature, population, stock prices)
# 3. Test each transformation type on different datasets
# 4. Test the "compare all transformations" option
# 5. Test error handling with invalid file paths
# 6. Verify all plots are saved correctly
# 7. Check that all modules work together seamlessly
# 
# Remember: Complete the TODOs in your three module files BEFORE testing this main program! (Otherwise Python will get mad at you!)