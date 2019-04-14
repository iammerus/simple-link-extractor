from urllib import request
import os

def read_url_as_string(url, encoding='utf8'):
    """
    Read the url specified as a string in the specified encoding
    """

    # Send http request
    fp = request.urlopen(url)

    # Read response bytearray
    responseBytes = fp.read()

    # Decode the byte array in the specified encoding scheme
    response = responseBytes.decode("utf8")

    # Close stream
    fp.close()

    return response

def download_file(url, storePath):     
    """
    Download the specified file into the specified directory
    """   
    
    filename = url.split('/').pop()

    request.urlretrieve(url, f'{storePath}{os.sep}{filename}')