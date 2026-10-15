import os
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = os.getenv("CODALIO_APP_RUN_URL", "").strip()
token = os.getenv("CODALIO_APP_RUN_TOKEN", "").strip()

print(f"URL: {url}")
print(f"Token: {token}")

request = Request(
    url,
    data=b"{}",
    method="POST",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    },
)

try:
    with urlopen(request, timeout=120) as response:
        payload = json.loads(response.read().decode("utf-8"))
        print(f"Success payload: {payload}")
except HTTPError as exc:
    try:
        payload = json.loads(exc.read().decode("utf-8"))
    except Exception as e:
        payload = {"detail": f"HTTP {exc.code}"}
    print(f"HTTPError payload: {payload}")
except Exception as e:
    print(f"Exception: {e}")
