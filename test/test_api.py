from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Allen Institute for AI Research Papers" in str(response.content)


def test_search():
    response = client.get("/search")
    assert response.status_code == 200
    assert response.json()["total"] == 47298


def test_list_bookmarks():
    response = client.get("/list_bookmarks")
    assert response.status_code == 200
    assert response.json()["total"] == 0


def test_add_bookmark():
    response = client.patch("/add_bookmark/9")
    assert response.status_code == 200
    assert response.json() == {
        "id": 9,
        "title": "Clinical and Immunologic Responses in Patients with Viral Keratoconjunctivitis",
        "journal": "American Journal of Ophthalmology",
        "date": "1975-10-31",
        "authors": "Knopf, Harry L.S.; Hierholzer, John C.",
        "url": "https://doi.org/10.1016/0002-9394(75)90398-0",
        "bookmarked": True,
    }


def test_remove_bookmark():
    response = client.patch("/remove_bookmark/9")
    assert response.status_code == 200
    assert response.json() == {
        "id": 9,
        "title": "Clinical and Immunologic Responses in Patients with Viral Keratoconjunctivitis",
        "journal": "American Journal of Ophthalmology",
        "date": "1975-10-31",
        "authors": "Knopf, Harry L.S.; Hierholzer, John C.",
        "url": "https://doi.org/10.1016/0002-9394(75)90398-0",
        "bookmarked": False,
    }


def test_read_bookmarks():
    response = client.get("/view_bookmarks")
    assert response.status_code == 200
    assert "Allen Institute for AI Research Papers" in str(response.content)
