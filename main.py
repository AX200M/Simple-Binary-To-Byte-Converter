#code to parse and convert binary data into string and bytes
import sys

filename_in = sys.argv[1]
filename_out = sys.argv[2]

filein = open(filename_in, 'r')
fileout = open(filename_out, 'wb')

outdata = bytes()
for line in filein:
    data = line.split()
    for d in data:
        if len(d) == 1:
            d = "0" + d #If binary value doesnt have a trailing 0 we account for it and add it to the file
            outdata += bytes.fromhex(d)
fileout.write(outdata)

#code taken from Matt Brown Video "Hacking an AT&T 4G Router For Fun and User Freedom"