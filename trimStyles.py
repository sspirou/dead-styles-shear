import sys, os

def main(pathToDirectory):
    print('IMPLEMENTATION COMING SOON')
    exit(0)

if __name__ == "__main__":
    if (sys.argv.__len__() <= 1):
        print("pathToDirectory is required")
        exit(1)
    main(sys.argv[1])