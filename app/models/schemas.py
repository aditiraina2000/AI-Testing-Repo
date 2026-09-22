from pydantic import BaseModel, Field
from typing import Annotated


class BaseModelStructure(BaseModel):
    model_id : int
    model_name : str
    model_org : Annotated[str, Field(min_length=3, max_length=20)]
    model_year : Annotated[int, Field(ge=2020)]
    model_company_owner : str | None = None

class ModelResponse(BaseModelStructure):
    pass

class ModelRequest(BaseModelStructure):
    pass
