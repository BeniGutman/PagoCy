from datetime import datetime
from pydantic import BaseModel


class Scan(BaseModel):
    start: datetime
    finish: datetime = None
