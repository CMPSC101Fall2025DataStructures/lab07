"""
This package contains three modules for data analysis and visualization:

1. data_loader.py - CSV file loading, validation, and summary statistics
2. transformations.py - Mathematical transformations (log, exp, sqrt)
3. plotting.py - Data visualization and plot creation

You can implement the functions in each module to create a complete
data analysis pipeline. Nifty, right?!

"""

# Make it easy to import all modules
from . import data_loader
from . import transformations  
from . import plotting

__all__ = ['data_loader', 'transformations', 'plotting']