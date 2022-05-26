import pytest
from app.controller import (
    add_bookmark,
    list_bookmarks,
    remove_bookmark,
    search_documents,
    store_data,
)


@pytest.fixture
def documents():
    return [
        {
            "id": 1,
            "title": "Test title 1",
            "journal": "Test Journal 1",
            "date": "2022-01-01",
            "authors": "Author A, Author B",
            "url": "http://test.com/1",
            "bookmarked": False,
        },
        {
            "id": 2,
            "title": "Test title 2",
            "journal": "Test Journal 2",
            "date": "2022-01-01",
            "authors": "Author C, Author D",
            "url": "http://test.com/2",
            "bookmarked": True,
        },
        {
            "id": 3,
            "title": "Test title 3",
            "journal": "Test Journal 3",
            "date": "2022-01-01",
            "authors": "Author E, Author F",
            "url": "http://test.com/3",
            "bookmarked": False,
        },
    ]


@pytest.mark.parametrize(
    "keyword,max_results,expected",
    [
        (
            "Test",
            10,
            {
                "results": [
                    {
                        "id": 1,
                        "title": "Test title 1",
                        "journal": "Test Journal 1",
                        "date": "2022-01-01",
                        "authors": "Author A, Author B",
                        "url": "http://test.com/1",
                        "bookmarked": False,
                    },
                    {
                        "id": 2,
                        "title": "Test title 2",
                        "journal": "Test Journal 2",
                        "date": "2022-01-01",
                        "authors": "Author C, Author D",
                        "url": "http://test.com/2",
                        "bookmarked": True,
                    },
                    {
                        "id": 3,
                        "title": "Test title 3",
                        "journal": "Test Journal 3",
                        "date": "2022-01-01",
                        "authors": "Author E, Author F",
                        "url": "http://test.com/3",
                        "bookmarked": False,
                    },
                ],
                "total": 3,
            },
        ),
        (
            "Test",
            1,
            {
                "results": [
                    {
                        "id": 1,
                        "title": "Test title 1",
                        "journal": "Test Journal 1",
                        "date": "2022-01-01",
                        "authors": "Author A, Author B",
                        "url": "http://test.com/1",
                        "bookmarked": False,
                    }
                ],
                "total": 3,
            },
        ),
        (
            "2",
            10,
            {
                "results": [
                    {
                        "id": 2,
                        "title": "Test title 2",
                        "journal": "Test Journal 2",
                        "date": "2022-01-01",
                        "authors": "Author C, Author D",
                        "url": "http://test.com/2",
                        "bookmarked": True,
                    }
                ],
                "total": 1,
            },
        ),
    ],
)
def test_search_documents(keyword, max_results, expected, documents):
    results = search_documents(
        documents=documents, keyword=keyword, max_results=max_results
    )
    assert expected == results


def test_list_bookmarks(documents):
    results = list_bookmarks(documents=documents)
    assert {"results": [documents[1]], "total": 1} == results


@pytest.mark.parametrize("test_input", [(1), (4)])
def test_add_bookmark(documents, test_input):
    result = add_bookmark(documents, test_input)
    if test_input == 4:
        expected = None
    else:
        expected = documents[test_input]
        expected["bookmarked"] = True
    assert expected == result


@pytest.mark.parametrize("test_input", [(2), (4)])
def test_remove_bookmark(documents, test_input):
    result = remove_bookmark(documents, test_input)
    if test_input == 4:
        expected = None
    else:
        expected = documents[test_input]
        expected["bookmarked"] = False
    assert expected == result


def test_store_data():
    documents = store_data()
    assert len(documents) == 47298
