from utils import read_url_as_string, download_file
from re import findall as regex_search
from os.path import isdir

## Is this ugly? Yes! Should you use it? Depends
##  
## I wanted something to do ugly things so this did the trick
## Probably could be better but... Maybe later


# Base URL
base = "URL"

# The regular expression to find the links in the html string
searchExpression = r'<a href="(.*)">Download<\/a>'

# The query parameter used for pagination
paginationQuery = "page"

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

# Loop and parse each page
for i in range(1, total+1):
    print(f"Parsing page {str(i)} out of {str(total)}")

    # Get the html of the page as an html string
    html = read_url_as_string(f"{base}?{paginationQuery}={str(i)}")

    # Get the download links of the PDFs
    # Yes, yes. Using regex on HTML strings in never good due to walla walla. But 
    # in this use case it doesn't really matter much. We control the output so meh
    links = regex_search(searchExpression, html)
    
    # Push links to collection
    final.extend(links)


# Check how many links we got
print(f"\r\n\r\nParsing complete. Starting document downloads. {str(len(final))} downloads in queue")

for i, link in enumerate(final):
    print(f"Downloading file {str(i+1)} of {str(len(final))}")
    download_file(link, storageLocation)