# coding:utf-8
import io
import time
import picamera

class CameraStreaming:
    def __init__(self, width, height, framerate, img_type='jpeg'):
        self.img_type = img_type
        self.camera = picamera.PiCamera()
        self.camera.brightness = 50 # Default 50
        self.camera.framerate = framerate
        self.camera.resolution = (width, height)
        time.sleep(2) # Initialize

    def streaming(self, send_img):
        with io.BytesIO() as stream:
            for foo in self.camera.capture_continuous(stream, self.img_type, use_video_port=True):
                stream.seek(0)
                frame = stream.getvalue()
                result = send_img(frame)
                if result is not None:
                    print(time.strftime('%T'), result)
                stream.seek(0)
                stream.truncate()
