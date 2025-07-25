## Solution

The audio given is an SSTV transmission. We can use SSTV decoders for decoding it to an image.

Exmaple decoder: https://github.com/colaclanth/sstv/tree/master

```bash
sstv -d message.wav -o out.png
```
The exported image is a QR code.

Scan it and get the flag.