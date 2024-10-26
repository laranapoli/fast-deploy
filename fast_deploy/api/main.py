import os

import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

from fast_deploy.loaders.sklearn_loader import SklearnModelLoader

app = FastAPI()

model_loader = SklearnModelLoader()
model = None


@app.post('/upload-model')
async def upload_lodel(file: UploadFile = File(...)):
    global model

    try:
        tmp_file_path = f'./{file.filename}'
        with open(tmp_file_path, 'wb') as f:
            content = await file.read()
            f.write(content)

        model = model_loader.load_model(tmp_file_path)

        os.remove(tmp_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class PredictionInput(BaseModel):
    features: list[float]


@app.post('/predict')
async def predict(input_data: PredictionInput):
    if model is None:
        raise HTTPException(
            status_code=400,
            detail='Modelo não carregado. Faça o upload primeiro.',
        )

    try:
        features = np.array([input_data.features])
        probabilities = model.predict_proba(features).tolist()
        prediction = model.predict(features).tolist()

        return {
            'prediction_proba': probabilities[0][1],
            'predicted': prediction[0],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
