#!/bin/bash

# Lab 07 Setup and Testing Script
# CS101 Fall 2025: Data Analysis and Visualization

echo "🚀 Setting up Lab 07: Data Analysis and Visualization"
echo "=================================================="

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   Visit: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

echo "✓ uv found"

# Install dependencies
echo "📦 Installing dependencies..."
uv sync

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Check if data files exist
echo "📊 Checking data files..."
for file in "data/temperature_data.csv" "data/population_data.csv" "data/stock_prices.csv"; do
    if [ -f "$file" ]; then
        echo "✓ $file exists"
    else
        echo "❌ $file missing"
    fi
done

# Create plots directory if it doesn't exist
mkdir -p plots

echo ""
echo "🎯 Setup complete! To run the program:"
echo "   uv run python main.py"
echo ""
echo "📝 Don't forget to complete the reflection in writing/reflection.md"
echo "🐛 Fix all TODOs in main.py before submitting"