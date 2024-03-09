from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Union

from pydantic import AnyHttpUrl, BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    ENV: str = Field(..., env="ENV")
    DARKNET_BINARY_LOCATION: str = Field(...,env="DARKNET_BINARY_LOCATION") # Location of Darknet Binary
    DARKNET_DATA_FILE: str = Field(..., env="DARKNET_DATA_FILE") # Darknet data file
    DARKNET_CFG_FILE: str = Field(..., env="DARKNET_CFG_FILE") # Darknet configuration file
    DARKNET_WEIGHTS: str = Field(..., env="DARKNET_WEIGHTS") # Weights for Darknet

    class Config:
        env_file = str(BASE_DIR) + "/.env"


class LocalSettings(Settings):
    DB_URL: str = Field(..., env="LOCAL_DB_URL")
    DEBUG: bool = True


class TestSettings(Settings):
    DB_URL: str = Field(..., env="TEST_DB_URL")
    DEBUG: bool = True


class DevSettings(Settings):
    DB_URL: str = Field(..., env="DEV_DB_URL")
    DEBUG: bool = False


class ProdSettings(Settings):
    DB_URL: str = Field(..., env="PROD_DB_URL")
    DEBUG: bool = False


@lru_cache()
def get_settings() -> Union[LocalSettings, TestSettings, DevSettings, ProdSettings]:
    envs: Dict = {
        "local": LocalSettings,
        "test": TestSettings,
        "dev": DevSettings,
        "prod": ProdSettings,
    }
    settings: Union[LocalSettings, TestSettings, DevSettings, ProdSettings] = envs[
        Settings().ENV
    ]()
    if not settings:
        raise Exception(
            """Environment does not exist
            Please chose one of below:-
            prod
            dev
            local
            test
            """
        )
    return settings


settings: Union[LocalSettings, TestSettings, DevSettings, ProdSettings] = get_settings()