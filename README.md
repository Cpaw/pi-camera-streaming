# Raspberry Pi Camera Streaming Server 

##Setup

```bash
./setup.sh
```


##Run

```bash
# height width frame_rate html_port websocket_port
python3 server.py 640 480 30 6000 7000
```

##URL
Server address 127.0.0.1  
HTML server port 6000  
WebSocket server port 7000  


| address                            |                  |
|------------------------------------|------------------|
| http://127.0.0.1:6000/             | html             |
| http://127.0.0.1:6000/streaming.js | client script    |
| ws://127.0.0.1:7000/               | streaming server |



##Receive Sample

```html
<html>
  <head>
    <img id="cameraImg" src="" width="" height="">
    <script type="text/javascript" src='127.0.0.1:6000/streaming.js'></script>
  </head>
</html>
```
