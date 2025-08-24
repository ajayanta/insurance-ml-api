from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
# import the ml model
app = FastAPI()
# pydantic model to validate incoming data
@app.get('/')
def home():
    return {'message':'Insurance Premium Predicition API'}


@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'verson':MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = [{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }] 
    try:

        prediction=predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))





