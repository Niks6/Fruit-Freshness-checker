
from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
import io
import tensorflow as tf 
from tensorflow.keras.preprocessing import image 

# --- IMPORTANT: Replace with your actual model loading ---
# The model file 'model.h5' should be in the same directory as app.py
try:
    model = tf.keras.models.load_model('model.h5')
    dummy_input = np.zeros((1, 299, 299, 3), dtype=np.float32)
    _ = model.predict(dummy_input)
    print("Model loaded successfully and warmed up.")
except Exception as e:
    print(f"Error loading Keras/TF model 'model.h5': {e}")

    raise RuntimeError(f"Failed to load the model: {e}. Please ensure 'model.h5' is valid and accessible.")

CLASS_NAMES = ['1_day_older(raw)', '2_day_older(fresh)', '3_day_older(ripe)', '4_day_older(total ripe)', '5_day_older','6_day_older(slightly rotten)','7_day_older(rotten)']

def predict_freshness(image_bytes, model, class_names):
    """
    Preprocesses the uploaded image bytes and makes a prediction using the model.
    Returns the predicted class name and its confidence.
    """
    img = Image.open(io.BytesIO(image_bytes))
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img = img.resize((299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_freshness = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    return predicted_freshness, confidence

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page with the image upload form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles image upload, preprocessing, prediction, and displays results."""
    if 'file' not in request.files:
        return render_template('index.html', prediction_text='No image file provided.', error=True)

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction_text='No selected file.', error=True)

    if file:
        try:
            image_bytes = file.read()

            if model:
                predicted_freshness, confidence = predict_freshness(image_bytes, model, CLASS_NAMES)

                result_text = (f"The item is predicted to be: <strong>{predicted_freshness}</strong> "
                               f"with <strong>{confidence*100:.2f}%</strong> confidence.")

                return render_template('index.html', prediction_text=result_text)
            else:
                return render_template('index.html', prediction_text='Model not loaded. Cannot make prediction.', error=True)

        except Exception as e:
            # Log the error for debugging
            print(f"Prediction error: {e}")
            return render_template('index.html', prediction_text=f'Error processing image or making prediction: {e}', error=True)

    return render_template('index.html', prediction_text='Something went wrong with the file upload.', error=True)

if __name__ == "__main__":
    app.run(debug=True) 
