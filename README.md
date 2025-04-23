# 使用此脚本获取摄像头和GPS信息
## 获取HTTPS证书
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```
## 安装依赖并启动
```
pip install flask #安装依赖
python app.py #启动
```
