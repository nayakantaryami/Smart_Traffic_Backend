# Smart Traffic Backend

A FastAPI-based backend service for intelligent traffic management using machine learning models.

## Features

- **Traffic Prediction**: Uses TensorFlow/Keras neural networks to predict optimal green light durations
- **Vehicle Detection**: YOLOv8-based vehicle counting from traffic camera images
- **REST API**: FastAPI endpoints for traffic prediction and image-based analysis
- **Scalable Processing**: Supports both manual input and automatic image processing

## Dependencies

This project has been tested and confirmed working with:

- **Python**: 3.12.3
- **TensorFlow**: 2.19.0 (CPU version)
- **Keras**: 3.10.0
- **FastAPI**: Latest version
- **YOLOv8**: For vehicle detection
- **NumPy/Pandas**: For data processing

## Installation

### Option 1: Automated Setup (Recommended)
```bash
git clone <repository-url>
cd Smart_Traffic_Backend
./setup.sh
```

### Option 2: Manual Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Smart_Traffic_Backend
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Validate installation**:
   ```bash
   python validate_dependencies.py
   ```

4. **Run the server**:
   ```bash
   ./run.sh
   # Or manually:
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Troubleshooting Installation Issues

If you encounter dependency conflicts or TensorFlow installation issues:

1. **Try the stable requirements**:
   ```bash
   pip install -r requirements-stable.txt
   ```

2. **Use environment variables for version control**:
   ```bash
   cp .env.example .env
   # Edit .env file with compatible versions for your environment
   ```

3. **For Python version compatibility issues**:
   - Python 3.12: Use `requirements.txt` (latest versions)
   - Python 3.8-3.11: Use `requirements-stable.txt` (tested stable versions)

4. **Common TensorFlow-CPU issues**:
   ```bash
   # If tensorflow-cpu>=2.19.0 fails, try:
   pip install tensorflow-cpu==2.15.0
   
   # For numpy compatibility issues:
   pip install "numpy>=1.21.0,<2.2.0"
   ```

## API Endpoints

### 1. Basic Prediction
- **Endpoint**: `POST /predict`
- **Purpose**: Predict green light durations from manual traffic data
- **Input**: Traffic counts, pedestrian counts, emergency vehicle flags

### 2. Image-based Prediction  
- **Endpoint**: `POST /predict-from-images`
- **Purpose**: Predict green light durations from traffic camera images
- **Input**: Four images (North, South, East, West directions)

### 3. Health Check
- **Endpoint**: `GET /`
- **Purpose**: Basic health check

## Model Architecture

The system uses two main components:

1. **Neural Network Model** (`traffic_model.h5`):
   - Predicts optimal green light durations
   - Uses scaled input/output with StandardScaler
   - Trained on traffic flow patterns

2. **YOLOv8 Object Detection**:
   - Counts vehicles in traffic images
   - Detects cars, motorcycles, buses, and trucks
   - Provides input data for the neural network

## File Structure

```
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   └── predictor.py     # Traffic prediction model
│   ├── schemas/
│   │   └── input_schema.py  # Pydantic data models
│   └── yolovision/
│       └── counter.py       # Vehicle counting logic
├── model/
│   ├── traffic_model.h5     # Trained neural network
│   ├── morning_time_scaler_independent.pkl  # Input scaler
│   ├── morning_time_scaler_dependent.pkl    # Output scaler
│   └── yolov8n.pt          # YOLOv8 weights
├── requirements.txt         # Python dependencies (latest)
├── requirements-stable.txt  # Stable dependencies (fallback)
├── runtime.txt             # Python version specification
├── .env.example            # Environment variables template
├── setup.sh                # Automated setup script
├── validate_dependencies.py # Dependency validation script
└── run.sh                  # Server startup script
```

## Dependency Compatibility Note

**TensorFlow 2.19.0 + Python 3.12 Compatibility**: This configuration has been tested and confirmed working. Previous compatibility issues between TensorFlow-CPU >=2.19.0 and Python 3.12 have been resolved in current package versions.

## Development

To validate your development environment:

```bash
python validate_dependencies.py
```

This script will verify all critical dependencies are properly installed and functional.

## License

[Add your license information here]