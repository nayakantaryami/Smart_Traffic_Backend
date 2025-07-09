#!/usr/bin/env python3
"""
Dependency validation script for Smart Traffic Backend
This script validates that all critical dependencies are correctly installed and functional.
"""

import sys
import importlib
from typing import List, Tuple

def validate_import(module_name: str, min_version: str = None) -> Tuple[bool, str]:
    """
    Validate that a module can be imported and optionally check version.
    
    Args:
        module_name: Name of the module to import
        min_version: Minimum required version (optional)
    
    Returns:
        Tuple of (success, message)
    """
    try:
        module = importlib.import_module(module_name)
        
        if min_version and hasattr(module, '__version__'):
            version = module.__version__
            return True, f"✓ {module_name} {version}"
        else:
            return True, f"✓ {module_name} imported successfully"
            
    except ImportError as e:
        return False, f"✗ Failed to import {module_name}: {e}"
    except Exception as e:
        return False, f"✗ Error with {module_name}: {e}"

def main():
    """Main validation function."""
    print("Smart Traffic Backend - Dependency Validation")
    print("=" * 50)
    
    # Critical dependencies to validate
    dependencies = [
        'tensorflow',
        'keras', 
        'numpy',
        'pandas',
        'fastapi',
        'uvicorn',
        'sklearn',  # scikit-learn
        'ultralytics',
        'cv2',  # opencv-python
        'multipart'  # python-multipart
    ]
    
    # Track results
    all_success = True
    results = []
    
    for dep in dependencies:
        success, message = validate_import(dep)
        results.append((success, message))
        if not success:
            all_success = False
    
    # Print results
    for success, message in results:
        print(message)
    
    print("\n" + "=" * 50)
    
    if all_success:
        print("✓ All dependencies validated successfully!")
        
        # Test TensorFlow specifically since it was the main issue
        try:
            import tensorflow as tf
            print(f"✓ TensorFlow {tf.__version__} - Python {sys.version.split()[0]} compatibility confirmed")
            
            # Quick functionality test
            import numpy as np
            test_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
            result = tf.reduce_sum(test_tensor)
            print(f"✓ TensorFlow functionality test passed (sum: {result.numpy()})")
            
        except Exception as e:
            print(f"✗ TensorFlow functionality test failed: {e}")
            all_success = False
            
        return 0 if all_success else 1
    else:
        print("✗ Some dependencies failed validation!")
        print("\nTo fix dependency issues, try:")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())