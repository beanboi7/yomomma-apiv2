#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
from app.main import app
import json
import random

client = TestClient(app)

with open('./jokes.json') as f:
  all_jokes = json.load(f)
no_of_jokes = len(all_jokes)

def check_joke_in_file(joke_json):
    if joke_json["joke"] in all_jokes:
        return True
    return False

# Base test
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"joke": "Yo momma"}

# Test for asserting random joke is in the file
def test_get_message_text():
    response = client.get("/jokes")
    response_json = response.json()
    assert response.status_code == 200
    assert check_joke_in_file(response_json)

# Test for asserting length of query count > 1
def test_query_count():
    random_count = random.randint(2,no_of_jokes)
    response = client.get(f"/jokes?count={random_count}")
    response_json = response.json()
    assert response.status_code == 200
    assert len(response_json) == random_count

# Test for asserting invalid query count
def test_invalid_query_count():
    random_count = random.randint(no_of_jokes,no_of_jokes*2)
    response = client.get(f"/jokes?count={random_count}")
    assert response.status_code == 404

# Test for asserting correct joke is indexed
def test_specific_index():
    random_index = random.randint(0,no_of_jokes-1)
    response = client.get(f"/jokes/{random_index}")
    assert response.status_code == 200
    assert response.json()["joke"] == all_jokes[random_index]

# Test for asserting index out of range
def test_index_out_of_range():
    random_index = random.randint(no_of_jokes,no_of_jokes*2)
    response = client.get(f"/jokes/{random_index}")
    assert response.status_code == 404

# Test for asserting index out of range (negative)
def test_index_out_of_range_negative():
    random_index = -1 * random.randint(no_of_jokes,no_of_jokes*2)
    response = client.get(f"/jokes/{random_index}")
    assert response.status_code == 404

# Test for asserting correct search results
def test_search():
    query = random.choice(random.choice(all_jokes).split())
    response = client.get(f"/search?query={query}")
    assert response.status_code == 200
    for search_result in response.json()["results"]:
        assert query in search_result.lower()