#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.config
# @Calendar: 2025-04-21 11:26
# @Time: 11:26
# @Author: mammon, kiramario
import datetime, os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from web.fastapi_demo.src.constants import Environment


# xxx/python_demo
current_path = Path.cwd()
fastapi_root_path = current_path / "web" /"fastapi_demo"

class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS:list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS:list[str]

    APP_VERSION: str = "1.0"

    model_config = SettingsConfigDict(
        env_file = str((fastapi_root_path / ".env").resolve()),
        extra="ignore"
    )


# 模块单例，import settings from fastapi.src.config
# 第一次加载执行的代码，后期直接从pyc加载
settings = Config()


def run():
    load_dotenv(dotenv_path=fastapi_root_path / ".env", verbose=True)
    print(os.getenv("environment", default=None))


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
