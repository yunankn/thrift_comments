from uuid import UUID
from typing_extensions import Annotated
from pydantic import BaseModel, Field, ConfigDict


class Comment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: UUID
    text: str
