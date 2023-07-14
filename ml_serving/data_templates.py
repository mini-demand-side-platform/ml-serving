from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


class ModelInput(BaseModel):
    inputs: List[List[float]]


@dataclass
class DBServerInfo:
    host: str
    port: str
    database: str
    username: str
    password: str
