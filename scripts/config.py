# """Environment-based configuration."""

# from __future__ import annotations

# import os


# def get_env(key: str, default: str | None = None, required: bool = False) -> str | None:
# 	value = os.getenv(key, default)
# 	if required and value is None:
# 		raise ValueError(f"Missing required environment variable: {key}")
# 	return value


# API_KEY = get_env("API_KEY", required=False)
# # BASE_URL = get_env("BASE_URL", default="")

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")