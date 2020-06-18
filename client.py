"""."""
import requests


class Client:
    """."""

    def __init__(self):
        """."""
        self._base_url = "https://api.covid19api.com/"

    def _get_request(self, url, data={}):
        """."""
        _url = self._base_url + url

        try:
            r = requests.get(url=_url)

            r = r.json()
        except:
            r = None

        return r

    def summary(self):
        """."""
        url = "summary"

        return self._get_request(url=url)

    def country(self, country, status="confirmed", ini="", end=""):
        """."""
        url = "country/" + country

        if status:

            url += "/status/" + status

        if ini:

            url += "?from=" + ini

        if end:

            url += "&to=" + end

        return self._get_request(url=url)
