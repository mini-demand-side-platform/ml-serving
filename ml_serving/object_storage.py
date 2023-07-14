from abc import ABC, abstractmethod
from typing import Any, List

from minio import Minio

from .data_templates import DBServerInfo
from .logger import get_logger

log = get_logger(logger_name="object_storage")


class ObjectStorage(ABC):
    @abstractmethod
    def get_object(self):
        pass

    @abstractmethod
    def list_object(self):
        pass


class MinioObjectStorage(ObjectStorage):
    def __init__(self, db_server_info: DBServerInfo) -> None:
        self._db_server_info = db_server_info

    def _get_connection(self):
        return Minio(
            endpoint=self._db_server_info.host + ":" + self._db_server_info.port,
            access_key=self._db_server_info.username,
            secret_key=self._db_server_info.password,
            secure=False,
        )

    def get_object(self, bucket_name: str, object_name: str) -> Any:
        conn = self._get_connection()
        return conn.get_object(bucket_name=bucket_name, object_name=object_name)

    def list_object(self, bucket_name: str) -> List[str]:
        object_name_list = []
        conn = self._get_connection()
        objects = conn.list_objects(bucket_name, recursive=True)
        for obj in objects:
            object_name_list.append(obj.object_name)
        return object_name_list
