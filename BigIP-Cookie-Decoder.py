import struct

encoded_string = '487098378.24095.0000'
print("[*] String to decode: %s" % encoded_string)

(host, port, end) = encoded_string.split('.')

(a, b, c, d) = [i for i in struct.pack("<I", int(host))]

(e) = [e for e in struct.pack("<H", int(port))]
port = "0x%02X%02X" % (e[0],e[1])

print ("[*] Decoded Host and Port: %s.%s.%s.%s:%s" % (a,b,c,d, int(port,16)))
