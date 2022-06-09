"""Configuration file, because we have only one environment we only need one
    class"""
import os


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    JSON_SORT_KEYS = False


class DevelopmentConfig:
    """Development configuration."""

    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, DevelopmentConfig)
