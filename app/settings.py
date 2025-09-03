import os

def _get(name, default=None, required=False):
    val = os.environ.get(name)
    if val is None:
        if required:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return default
    return val

class Settings:
    ENV = _get("ENV", default="dev")
    PORT = _get("PORT", default=8000,)
    DISCOUNT = _get("DISCOUNT", required=True)

settings = Settings()
