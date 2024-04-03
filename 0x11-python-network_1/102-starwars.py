#!/usr/bin/python3
""" sends a search request to the star war API
Manages pagination to display all results
Usage: ./102-starwars.py <search string>
The search request is sent to the star wars API
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    count = results.get("count")
    print("Number of results: {}".format(results.get("count")))

    b = 0
    while b < count:
        for r in results.get("results"):
            print(r.get("name"))
            for link in r.get("films"):
                film = requests.get(link).json()
                print("\t{}".format(film.get("title")))
            b += 1

        next_page = results.get("next")
        if next_page is not None:
            results = requests.get(next_page).json()
