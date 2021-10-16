import sys

ab=[]

def main():
    ab=[]
    print("i")
    for i in sys.stdin:
        ab = i.split()
        print(ab)
    closest_corner(ab)

def closest_corner(coords):
    print("running")
    xf,yf=coords[0,1]
    print(xf,yf)

if __name__ == '__main__':
    main()

