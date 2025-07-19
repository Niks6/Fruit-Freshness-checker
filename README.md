# Banana Ripeness Prediction using InceptionV3

## Overview
This project deploys a deep learning model that predicts the age (ripeness level) of bananas after being plucked from the tree. The model uses a custom dataset and InceptionV3 architecture, deployed as a web service on Render.

## Live Demo
The model is deployed at: [https://your-render-service.onrender.com](https://your-render-service.onrender.com)

## Features
- REST API endpoint for predictions
- Web interface for easy testing(made using flask)
- Scalable cloud deployment
- Automatic CI/CD from GitHub

## Project Structure
```
.
├── app/                  # Flask/FastAPI application
│   ├── main.py           # Web server entry point
│   ├── model.py          # Model loading and prediction logic
│   └── templates/        # HTML templates (if web interface exists)
├── model/                # Trained model files
│   └── inceptionv3_banana.h5
├── requirements.txt      # Python dependencies
├── render.yaml           # Render deployment configuration
├── Dockerfile            # Container configuration (if using Docker)
└── README.md
```

## Local Development
1. Clone the repository:
```bash
git clone [https://github.com/yourusername/banana-ripeness-prediction.git](https://github.com/Niks6/Fruit-Freshness-checker.git)
cd Fruit-Freshness-checker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app/main.py
```

The API will be available at `http://localhost:5000`

## API Endpoints
### Prediction Endpoint
`POST /predict`
- Accepts: Image file (JPEG/PNG)
- Returns: JSON with prediction results

Example using curl:
```bash
curl -X POST -F "file=@banana.jpg" https://your-render-service.onrender.com/predict
```

Example response:
```json
{
  "prediction": 2.5,
  "confidence": 0.92,
  "message": "Banana is approximately 2.5 days old"
}
```

## Deployment on Render
This project is configured for automatic deployment on Render:

1. **Web Service Deployment**:
   - Connected to GitHub repository
   - Automatic deploys on push to main branch
   - Health checks enabled

2. **Environment Variables**:
   - `PYTHON_VERSION`: 3.9
   - `MODEL_PATH`: ./model/inceptionv3_banana.h5

3. **Scaling**:
   - Standard instance type
   - Auto-scaling configured (if needed)

## Monitoring
The deployed service includes:
- Uptime monitoring
- Performance metrics
- Log streaming

## CI/CD Pipeline
- Push to main branch triggers rebuild
- Automated tests run before deployment
- Health checks verify successful deployment

## Troubleshooting
Common issues:
1. **Model loading errors**: Verify the model file exists at the specified path
2. **Memory issues**: Increase instance size in Render dashboard
3. **Timeout errors**: Adjust health check timeout in render.yaml

## License
MIT License - See [LICENSE](LICENSE) for details.

## Contact
For support or questions:
- Email: your.email@example.com
- GitHub Issues: [https://github.com/yourusername/banana-ripeness-prediction/issues](https://github.com/yourusername/banana-ripeness-prediction/issues)
