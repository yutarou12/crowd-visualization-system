import os
from dotenv import load_dotenv

load_dotenv()

# 環境変数の読み込み
API_PATH: str = os.getenv("API_PATH")
VIDEO_PATH: str = os.getenv("VIDEO_PATH")
