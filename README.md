
Wi-Fiカメラのデータと物体検出アルゴリズム「YOLO」を用いた、混雑状況を取得するサービスです。

Presence confirmation service using Wi-Fi cameras and AI.

## 1.機能
 - 在室時 : 
   - WiFiカメラの映像を元に、在室者数をカウントし、任意のAPIに送ります。
   - 在室者数をカウントするために、YOLOv8を使用しています。
 - 不在時 :
   - WiFiカメラの映像を元に、在室者数をカウントし、任意のAPIに送ります。

## 2.環境変数
 - VIDEO_PATH : `WiFiカメラの映像のURL`
 - API_PATH : `APIとなるスプレッドシートのURL`

## 3.動作環境
 - Python 3.10.12
 - Docker 28.1.1, build 4eba377
 - Docker Compose v2.35.1

## 4.使用ライブラリ
 - ultralytics
 - opencv-python
 - python-dotenv
 - schedule
