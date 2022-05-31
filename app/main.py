from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from typing import Dict, List, Optional
from app.schemas import SearchResult, SearchResults
from app import controller

app = FastAPI(title="Journals API", openapi_url="/openapi.json")
api_router = APIRouter()
DOCUMENTS = controller.store_data()


@api_router.get("/", status_code=200, response_class=HTMLResponse)
def root() -> dict:
    """
    Search documents from webpage
    """
    with open("index.html", "r") as f:
        return f.read()


@api_router.get("/search/", status_code=200, response_model=SearchResults)
def search_documents(
    keyword: Optional[str] = None, max_results: Optional[int] = 1000
) -> dict:
    """
    Search for documents based on keyword
    """
    return controller.search_documents(
        documents=DOCUMENTS, keyword=keyword, max_results=max_results
    )


@api_router.patch(
    "/add_bookmark/{doc_id}", status_code=200, response_model=SearchResult
)
def add_bookmark(doc_id: int):
    """
    Add a bookmark to document
    """
    return controller.add_bookmark(documents=DOCUMENTS, doc_id=doc_id)


@api_router.patch(
    "/remove_bookmark/{doc_id}", status_code=200, response_model=SearchResult
)
def remove_bookmark(doc_id: int):
    """
    Remove a bookmark from document
    """
    return controller.remove_bookmark(documents=DOCUMENTS, doc_id=doc_id)


@api_router.get("/list_bookmarks/", status_code=200, response_model=SearchResults)
def list_bookmarks():
    """
    List all bookmarked documents
    """
    return controller.list_bookmarks(documents=DOCUMENTS)


@api_router.get("/view_bookmarks/", status_code=200, response_class=HTMLResponse)
def view_bookmarks():
    """
    View bookmarked documents in webpage
    """
    with open("bookmarks.html", "r") as f:
        return f.read()


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
