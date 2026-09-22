from xml.parsers.expat import model

from fastapi import FastAPI, status
from models.schemas import ModelResponse, ModelRequest

app = FastAPI()

models_list = [
{"model_id":1,"model_name":"Jev","model_org":"TypesafeAI","model_year":2026,"model_company_owner":"plato"},
{"model_id":2,"model_name":"gpt5.6:luna","model_org":"OpenAI","model_year":2025,"model_company_owner":"sam"},
{"model_id":3,"model_name":"claude sonet 5","model_org":"AnthropicAI","model_year":2025,"model_company_owner":"Amodei"}
]


@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello": "World"}

@app.get("/models-list")
def list_models():
    return models_list

@app.post("/add-model",response_model=list[ModelResponse],status_code=status.HTTP_201_CREATED)
def add_model(request: ModelRequest):
    inserted_model ={
        "model_id":request.model_id,
        "model_name":request.model_name,
        "model_org":request.model_org,
        "model_year":request.model_year,
        "model_company_owner":request.model_company_owner
    }

    models_list.append(inserted_model)

    return models_list