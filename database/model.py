from pydantic import BaseModel

#creo model per poter fare delle api POST
class Wine(BaseModel):
    id:int
    color:str
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float   
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: int