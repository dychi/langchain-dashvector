import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")

load_dotenv(dotenv_path)

DASHVECTOR_API_KEY = os.getenv("DASHVECTOR_API_KEY", "")
DASHVECTOR_ENDPOINT = os.getenv("DASHVECTOR_ENDPOINT", "")
DASHVECTOR_COLLECTION_NAME = (
    "test-collection"  # os.getenv("DASHVECTOR_COLLECTION_NAME")
)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
