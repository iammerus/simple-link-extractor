from utils import read_url_as_string, download_file
from re import findall as regex_search
from os.path import isdir


# Base URL
base = "http://www.footofthecross.com/"

# Declare final links array
final = []

# Total number of pages
total = 13

# Get total number of pages
storageLocation = input("Where should the downloads be saved? (Enter full path): ")

# Sanity check that shit
if(not storageLocation or not isdir(storageLocation)):
    print("Please enter a valid path. Ensure that the directory exists")
    exit()

# Shit is about to go down
print(f"\r\nFetching {str(total)} pages from '{base}'", end="\r\n\r\n")

