from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_host: str
    database_port: int = 5432
    database_name: str
    database_user: str
    database_pswd: str
