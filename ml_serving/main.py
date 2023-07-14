from typing import List

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from .config import default_ctr, object_storage_server_info
from .data_templates import ModelInput
from .logger import get_logger
from .model import SklearnModel
from .object_storage import MinioObjectStorage

log = get_logger(logger_name="main")

app = FastAPI()
model = SklearnModel(default_ctr=default_ctr)
object_storage = MinioObjectStorage(db_server_info=object_storage_server_info)


@app.get("/health")
def health_check() -> bool:
    return True


@app.on_event("startup")
def reload_latest_model():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        model.get_latest_model, "interval", minutes=1, args=(object_storage,)
    )
    scheduler.start()


@app.post("/model:predict")
def get_model_predict(data: ModelInput) -> List[float]:
    return model.predict(data.inputs)
