import asyncio
import datetime
import cv2
import requests
from ultralytics import YOLO
import libs.env as env
import schedule
import time


def load_yolo_model(model_path='model/yolo11s.pt'):
    model = YOLO(model_path)
    return model


model = load_yolo_model()
print(f"モデルがロードされました: {model}")


async def detect_video(m, rtsp_url: str, floor: str):
    date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cap = cv2.VideoCapture(rtsp_url)
    try:
        ret, frame = cap.read()
        if not ret or frame is None:
            print(f"[{date_now}] [{floor}] フレーム取得に失敗")
            return

        results = m(frame)
        people_count = 0
        for r in results:
            for box in r.boxes:
                if int(box.cls[0]) == 0:  # クラスID 0 が person を想定
                    people_count += 1
                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        #url = f"{env.API_PATH}?floor={floor}&count={people_count}"
        try:
            print(f"[{date_now}] [{floor}] API送信: 人数 {people_count}")
            #requests.post(url=url, timeout=5)
        except Exception as e:
            print(f"[{date_now}] [{floor}] API送信エラー: {e}")

        print(f"[{date_now}] [{floor}] 人数: {people_count}")
    except Exception as e:
        print(f"[{date_now}] [{floor}] エラー: {e}")
    finally:
        cap.release()


async def process_cameras():
    tasks = []
    for cam in env.CAMERAS:
        tasks.append(detect_video(model, cam['rtsp'], cam['floor']))
    await asyncio.gather(*tasks)


def send_data_periodically():
    def job():
        asyncio.run(process_cameras())

    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    send_data_periodically()
