from typing import Optional, Sequence
from pydantic import BaseModel


class SearchResult(BaseModel):
    id: int
    title: str
    journal: str
    date: str
    authors: str
    url: Optional[str]
    bookmarked: bool


class SearchResults(BaseModel):
    total: int
    results: Sequence[SearchResult]
