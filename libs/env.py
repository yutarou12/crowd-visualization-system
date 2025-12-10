import os
from dotenv import load_dotenv

load_dotenv()

# 環境変数の読み込み
API_PATH: str = os.getenv("API_PATH")
# VIDEO_PATHをCAMERASに変更
CAMERAS: list = [
    {
        "floor": "2F",
        "rtsp": os.getenv("CAMERA_PATH_2F")
    },
    {
        "floor": "3F",
        "rtsp": os.getenv("CAMERA_PATH_3F")
    }
]
