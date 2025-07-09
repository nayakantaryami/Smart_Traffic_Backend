#!/bin/bash

# Smart Traffic Backend Setup Script
# This script handles dependency installation with fallback options

set -e

echo "Smart Traffic Backend - Dependency Setup"
echo "========================================"

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "Detected Python version: $PYTHON_VERSION"

# Function to install with fallback
install_dependencies() {
    local requirements_file=$1
    echo "Attempting to install dependencies from $requirements_file..."
    
    if pip install -r "$requirements_file"; then
        echo "✓ Dependencies installed successfully from $requirements_file"
        return 0
    else
        echo "✗ Failed to install from $requirements_file"
        return 1
    fi
}

# Try installation with different strategies
if [[ "$PYTHON_VERSION" == "3.12" ]]; then
    echo "Using Python 3.12 optimized requirements..."
    if ! install_dependencies "requirements.txt"; then
        echo "Falling back to stable requirements..."
        install_dependencies "requirements-stable.txt"
    fi
elif [[ "$PYTHON_VERSION" =~ ^3\.(8|9|10|11)$ ]]; then
    echo "Using stable requirements for Python $PYTHON_VERSION..."
    if ! install_dependencies "requirements-stable.txt"; then
        echo "Falling back to main requirements..."
        install_dependencies "requirements.txt"
    fi
else
    echo "Warning: Python $PYTHON_VERSION may not be fully supported"
    echo "Attempting installation with main requirements..."
    if ! install_dependencies "requirements.txt"; then
        echo "Falling back to stable requirements..."
        install_dependencies "requirements-stable.txt"
    fi
fi

echo ""
echo "Validating installation..."
if python3 validate_dependencies.py; then
    echo ""
    echo "✓ Setup completed successfully!"
    echo "You can now run the server with: ./run.sh"
else
    echo ""
    echo "✗ Validation failed. Please check the error messages above."
    echo "You may need to install dependencies manually or try a different Python version."
    exit 1
fi