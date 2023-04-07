import json
from loguru import logger
import requests

STATUS_URL = "http://grbsrv.opengribs.org/getstatus2.php"
SAMPLE_URL = "http://grbsrv.opengribs.org/getmygribs2.php/?osys=Unknown&ver=1.2.4&la1=77.13907608&la2=81.928578885&lo1=15.309623066&lo2=39.065873066&model=gfs_p25_&wmdl=none&intv=3&days=1&cyc=last&par=W%3BT%3BR%3B&wpar="
RESPONSE_URL = """
{
  "status": true,
  "message": {
    "url": "http://grbsrv.opengribs.org/downloads/1680890706199/20230407_180506_GFS_P25_.grb2",
    "size": 50942,
    "sha1": "a1b02628cc671856d8cb4db8359b8d6ca1aa1b5d"
  }
}
"""

logger = logger.bind(name="main")

# Send a request with a sample url and parse response to figure out the url to donlwoad
def get_url():
    response = requests.get(SAMPLE_URL)
    if response.status_code == 200:
        return json.loads(response.content)["message"]["url"]
    else:
        return None

# Download response url
def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("test.grb2", "wb") as f:
            f.write(response.content)
    else:
        logger.error("Error downloading file")


def main():
    url = get_url()
    if url:
        download(url)
    else:
        logger.error("Error getting url")


if __name__ == "__main__":
    main()
