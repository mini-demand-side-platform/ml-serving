import os

from .data_templates import DBServerInfo

object_storage_server_info = DBServerInfo(
    host=os.getenv("object_storage_host", "localhost"),
    port=os.getenv("object_storage_info", "9000"),
    database=os.getenv("object_storage_database", "object"),
    username=os.getenv("object_storage_username", "dsp"),
    password=os.getenv("object_storage_password", "dsppassword"),
)
default_ctr = float(os.getenv("default_ctr", 0.009905203839797677))
