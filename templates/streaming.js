// var server = "ws://raspberrypi.local:5000";
var server = "{{ ws_server }}"
var img = document.getElementById("cameraImg");
var arrayBuffer;

//WebSocketでサーバに接続
var ws = new WebSocket(server);
ws.binaryType = 'arraybuffer';
ws.onopen = function(){console.log("Connection was established");};

// 受信してbase64 encode
ws.onmessage = function(evt){
  img.src = "data:image/jpeg;base64," + base64Encode(new Uint8Array(evt.data));
};

// タブを閉じたらサーバにセッションの終了
window.onbeforeunload = function(){ ws.close(1000);};

// 速度
function base64Encode(input){
  var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var output = "";
  var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
  var i = 0;

  while(i < input.length){
    chr1 = input[i++];
    chr2 = i < input.length ? input[i++] : Number.NaN; // Not sure if the index
    chr3 = i < input.length ? input[i++] : Number.NaN; // checks are needed here

    enc1 = chr1 >> 2;
    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
    enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
    enc4 = chr3 & 63;

    if(isNaN(chr2)){
      enc3 = enc4 = 64;
    } else if(isNaN(chr3)){
      enc4 = 64;
    }
    output += keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
  }
  return output;
}
