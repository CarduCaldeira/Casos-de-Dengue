
from pydantic_settings import BaseSettings, SettingsConfigDict

class AWSSettings(BaseSettings):
    """
   
    """
    
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str

