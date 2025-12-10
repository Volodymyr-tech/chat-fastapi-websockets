from pydantic import BaseModel, Field


class MessageRead(BaseModel):
    id: int = Field(..., description="unic id")
    sender_id: int = Field(..., description="ID оsender")
    recipient_id: int = Field(..., description="ID reciever")
    content: str = Field(..., description="Content message")


class MessageCreate(BaseModel):
    recipient_id: int = Field(..., description="unic id")
    content: str = Field(..., description="Content message")