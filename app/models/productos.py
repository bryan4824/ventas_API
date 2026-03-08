from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    quantity: int
    price: float = Field(ge=0)
    category_id: int  # <-- Usamos el ID de la categoría
    min_stock: int


class ProductCreate(BaseModel):
    vendedor_id: UUID # <-- Este es el "vínculo"
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(ge=0)
    category_id: int  # <-- Usamos el ID de la categoría
    quantity: int = Field(default=0, ge=0)
    min_stock: int = Field(default=0, ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, ge=0)
    category_id: Optional[int] = None
    min_stock: Optional[int] = Field(None, ge=0)
    ingreso_date: Optional[date] = None

class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    #Esquema para mostrar los productos
    id: UUID
    vendedor_id: UUID
    name: str = Field(..., min_length=1, max_length=200, description="Nombre del producto")
    quantity: int = Field(..., ge=0, description="Cantidad de productos en stock")
    price: float = Field(ge=0)
    category_id: int  # <-- Usamos el ID de la categoría
    ingreso_date: date
    min_stock: int = Field(..., ge=0)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProductListOut(BaseModel):
    #Salisa de numero total de registros 
    total: int
    items: List[ProductOut]

