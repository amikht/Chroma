from PIL import Image, ImageChops
import sys, math


def usage():
    print("sksksksks you fucked up")


if __name__ == "__main__":

    
    if len(sys.argv) == 2:
        print("seperating channels")
        try:
            with Image.open(sys.argv[1]) as im:
                
                r, g, b = im.split()
        except IOError as e:
            print()
        
        filename = sys.argv[1].split(".")[0]
        filetype = sys.argv[1].split(".")[1]

        print (r.size, r.mode, r.format)
        
        r.save(filename + "_red." + filetype)
        g.save(filename + "_green." + filetype)
        b.save(filename + "_blue." + filetype)

    elif len(sys.argv) == 3:
        print("seperating channels")
        try:
            with Image.open(sys.argv[1]) as im:
                
                r, g, b = im.split()
        except IOError as e:
            print()
        
        print("offsetting channels")

        offset = int(sys.argv[2])
        print(offset)
        
        g = ImageChops.offset(g, offset, 0)
        b = ImageChops.offset(b, int(math.cos(2 * math.pi / 3 ) * offset),
                    int(math.sin(2 * math.pi / 3 ) * offset))
        r = ImageChops.offset(r, int(math.cos(4 * math.pi / 3) * offset),
                    int(math.sin(4 * math.pi / 3 ) * offset))
        
        print("merging channels")

        result = Image.merge("RGB", [r, g, b])
        result.show()

        filename = sys.argv[1].split(".")[0]

        print("saving file: " + filename + "_final.png")

        result.save("final.png")

    else:
        usage()