#Rread file and convert to list
def read_file(filename) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    f=open(filename,"r")
    name=f.read().split(",")
    ls=[]
    for i in name:
        ls.append(int(i))
    return ls
print(read_file("data.txt"))

#Print list from file
