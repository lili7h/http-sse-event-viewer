import requests
from requests_sse import EventSource, InvalidStatusCodeError, InvalidContentTypeError

with EventSource("http://127.0.0.1:3621/mac/game/events/v1", timeout=30) as event_source:
    try:
        for event in event_source:
            print(event)
    except InvalidStatusCodeError:
        pass
    except InvalidContentTypeError:
        pass
    except requests.RequestException:
        pass
