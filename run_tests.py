#!/usr/bin/env python3
"""
Test Runner for Data Analysis Project
CS101 Fall 2025: Lab 07

Run this script to test all modules after completing the TODOs.
Make sure to uncomment the test functions in each module first!
"""

def run_all_tests():
    """Run tests for all three modules."""
    print("="*60)
    print("🧪 RUNNING ALL MODULE TESTS")
    print("="*60)
    
    try:
        # Test data_loader module
        print("\n📁 Testing Data Loader Module...")
        from modules.data_loader import test_data_loader
        test_data_loader()
        
        # Test transformations module
        print("\n🔄 Testing Transformations Module...")
        from modules.transformations import test_transformations
        test_transformations()
        
        # Test plotting module
        print("\n📊 Testing Plotting Module...")
        from modules.plotting import test_plotting
        test_plotting()
        
        print("\n✅ All module tests completed!")
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure you've completed the TODOs and uncommented the test functions!")
    except Exception as e:
        print(f"❌ Test Error: {e}")

if __name__ == "__main__":
    run_all_tests()