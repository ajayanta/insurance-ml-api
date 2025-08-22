# Insurance Premium Risk Prediction API (FastAPI)

This project provides a **REST API** built with [FastAPI](https://fastapi.tiangolo.com/) that predicts whether a customer **should pay a High, Medium, or Low annual insurance premium** based on their profile.

It demonstrates how to serve a trained **RandomForest classification model** as a production-ready API.

---

##  Features

- **RandomForest Classifier** to predict premium risk (`Low`, `Medium`, `High`)  
- **FastAPI backend** for high-performance asynchronous API  
- **Input validation** with Pydantic  
- **Health check endpoint** to verify model status  
- **Interactive API docs** via auto-generated Swagger UI and ReDoc  

---

## Project Structure

insurance-premium-prediction/
│
├── config/
│ └── city_tier.py # Helper/config file for city tier mapping
│
├── model/
│ ├── model.pkl # Trained RandomForest model (binary file)
│ └── predict.py # Loads model and defines predict_output(), MODEL_VERSION
│
├── schema/
│ └── user_input.py # Pydantic schema for input validation
│
├── app.py # FastAPI app entry point
├── requirements.txt # Python dependencies

