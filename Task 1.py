try:
    print("Reading file content:")
    fh=open("sample.txt","rt")
    Line1=fh.readline()
    Line2=fh.readline()
    fh.close()
    print(f"Line 1: {Line1.strip('\n')}")
    print(f"Line 2: {Line2}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")