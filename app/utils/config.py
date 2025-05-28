from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    QDRANT_URL: str
    GOOGLE_API_KEY: str
    GROQ_API_KEY: str
    MONGODB_URI: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )



settings = Settings()