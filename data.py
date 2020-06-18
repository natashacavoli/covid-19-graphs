"""."""
from client import Client

import matplotlib.pyplot as p
import datetime
import pandas
import json


class Data(object):
    """."""

    def __init__(self):
        """."""
        self._client = Client()

    def _format(self, data):
        """."""
        names = []
        values = []

        for i in data:

            date = datetime.datetime.\
                strptime(i["Date"], "%Y-%m-%dT%H:%M:%SZ")

            date = datetime.datetime.\
                strftime(date, "%Y-%m-%d")

            names.append(date)

            values.append(i["Cases"])

        return {"names": names, "values": values}

    def confirmed(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=10)

        data = self._client.country(
            country,
            "confirmed",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#1a75ff")

        p.title("Confirmed Cases")

        p.show()

    def deaths(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=10)

        data = self._client.country(
            country,
            "deaths",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#ff6666")

        p.title("Deaths")

        p.show()

    def recovered(self, country):
        """."""
        today = datetime.datetime.today().date()

        first = today - datetime.timedelta(days=10)

        data = self._client.country(
            country,
            "recovered",
            first.isoformat(),
            today.isoformat())

        r = self._format(data)

        p.plot(r["names"], r["values"], "#39ac39")

        p.title("Recovered")

        p.show()

    def countries_to_df(self, columns=[], head=10):
        """."""
        data = self._client.summary()

        data = json.dumps(data["Countries"])

        data = pandas.read_json(data, orient="records")

        data = data.sort_values(by=columns, ascending=False).head(head)

        return data

    def countries_confirmed(self):
        """."""
        data = self.countries_to_df(["TotalConfirmed"])

        data = data[["CountryCode", "TotalConfirmed"]].copy()

        data.columns = ["Country Code", "Total Confirmed"]

        data.plot.bar(x="Country Code", y="Total Confirmed", color="#1a75ff")

        p.title("Countries Confirmed Cases")

        p.xlabel("Country Code")

        p.ylabel("Total Confirmed (millions)")

        p.show()

    def countries_deaths(self):
        """."""
        data = self.countries_to_df(["TotalDeaths"])

        data = data[["CountryCode", "TotalDeaths"]].copy()

        data.columns = ["Country Code", "Total Deaths"]

        data.plot.bar(x="Country Code", y="Total Deaths", color="#ff3333")

        p.title("Countries Deaths")

        p.xlabel("Country Code")

        p.ylabel("Total deaths")

        p.show()

    def countries_recovered(self):
        """."""
        data = self.countries_to_df(["TotalRecovered"])

        data = data[["CountryCode", "TotalRecovered"]].copy()

        data.columns = ["Country Code", "Total Recovered"]

        data.plot.bar(x="Country Code", y="Total Recovered", color="#39ac39")

        p.title("Countries Recovered")

        p.xlabel("Country Code")

        p.ylabel("Total recovered")

        p.show()

d = Data()

d.countries_deaths()
