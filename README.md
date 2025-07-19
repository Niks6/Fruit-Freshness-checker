# Banana Ripeness Prediction using InceptionV3

## Overview
This project deploys a deep learning model that predicts the age (ripeness level) of bananas after being plucked from the tree. The model uses a custom dataset and InceptionV3 architecture, deployed as a web service on Render.

## Live Demo
The model is deployed at: [(https://fruit-freshness-checker.onrender.com)](https://fruit-freshness-checker.onrender.com)

## Features
- REST API endpoint for predictions
- Web interface for easy testing(made using flask)
- Scalable cloud deployment
- Automatic CI/CD from GitHub

## Project Structure
```
.
├── data/                  
│   ├── banana_dataset                      # Raw dataset
│   ├── fine_output_banana_dataset          # fine tuned dataset
│   └── templates/        
├── templates/              
│   └── index.html         # webpage
├── requirements.txt       # Python dependencies
├── model.h5               # InceptionV3 model
├── freshness_checker      # jupyter notebook
└── app.py                 # Flask App
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
python app.py
```

The API will be available at `http://[http://127.0.0.1:5000/](http://127.0.0.1:5000/)`

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
  "confidence": 92.,
  "message": "3_days_old"
}
```

## Deployment on Render
This project is configured for automatic deployment on Render:

1. **Web Service Deployment**:
   - Connected to GitHub repository
   - Automatic deploys on push to main branch
   - Health checks enabled

2. **Environment Variables**:
   - `PYTHON_VERSION`: 3.10.13
   - `MODEL_PATH`: ./model.h5

3. **Scaling**:
   - Standard instance type
   - Auto-scaling configured (if needed)


## Troubleshooting
Common issues:
1. **Model loading errors**: Verify the model file exists at the specified path
2. **Memory issues**: Increase instance size in Render dashboard
3. **Timeout errors**: Adjust health check timeout in render.yaml

## License
MIT License - See [LICENSE](LICENSE) for details.

## Contact
For support or questions:
- Email: codeisforcoders@gmail.com
