from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # QdrantSettings
    QDRANT_URL: str

    # Googleapisettings
    GOOGLE_API_KEY: str
    # GROQ settings
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = Settings()