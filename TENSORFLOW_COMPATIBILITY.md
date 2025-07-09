# TensorFlow-CPU Compatibility Guide

## Problem Description
Users may encounter the following error when installing dependencies:

```
ERROR: Ignored the following versions that require a different python version: 1.21.2 Requires-Python >=3.7,<3.11
ERROR: Could not find a version that satisfies the requirement tensorflow-cpu>=2.19.0
ERROR: No matching distribution found for tensorflow-cpu>=2.19.0
```

## Root Cause
This error typically occurs due to:
1. **Python version incompatibility**: Some package versions have strict Python version requirements
2. **Package index issues**: Temporary PyPI connection problems or regional mirror issues
3. **Architecture compatibility**: Different CPU architectures may have limited package availability

## Solutions

### Quick Fix (Recommended)
Use the automated setup script:
```bash
./setup.sh
```

### Manual Solutions

#### Option 1: Use Flexible Version Ranges (Primary)
The updated `requirements.txt` now uses flexible version ranges:
- `tensorflow-cpu>=2.15.0,<2.20.0` (instead of `>=2.19.0`)
- `numpy>=1.21.0,<2.2.0` (instead of unrestricted)

#### Option 2: Use Stable Requirements (Fallback)
```bash
pip install -r requirements-stable.txt
```

#### Option 3: Install Specific Versions
```bash
pip install tensorflow-cpu==2.15.0
pip install "numpy>=1.21.0,<2.2.0"
pip install -r requirements.txt
```

#### Option 4: Environment-Specific Installation
Copy and customize the environment variables:
```bash
cp .env.example .env
# Edit .env with your preferred versions
```

### Python Version Compatibility Matrix

| Python Version | TensorFlow-CPU | NumPy | Status |
|----------------|----------------|-------|--------|
| 3.8            | 2.15.0         | 1.25.2| ✅ Stable |
| 3.9            | 2.15.0         | 1.25.2| ✅ Stable |
| 3.10           | 2.15.0         | 1.25.2| ✅ Stable |
| 3.11           | 2.15.0-2.19.0  | 1.25.2-2.1.3| ✅ Stable |
| 3.12           | 2.19.0         | 2.1.3 | ✅ Latest |

## Verification
After installation, run:
```bash
python validate_dependencies.py
```

This will confirm all dependencies are working correctly.

## Additional Troubleshooting

### Network Issues
If you encounter network timeouts:
```bash
pip install --timeout 1000 -r requirements.txt
# or
pip install --index-url https://pypi.python.org/simple/ -r requirements.txt
```

### Platform-Specific Issues
For different operating systems or architectures, you may need to use:
```bash
pip install --only-binary=all -r requirements.txt
```

### Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Report Issues
If none of these solutions work, please report the issue with:
1. Your Python version (`python --version`)
2. Your operating system
3. The complete error message
4. Output of `pip --version`