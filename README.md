# Healx Technical Test

## Local Setup

1. `pip install poetry` (or follow the instructions: https://python-poetry.org/docs/#installation)
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. [UNIX]: Run the FastAPI server with the bash script: `./run.sh`
4. [WINDOWS]: Run the FastAPI server with the Powershell command: `.\run.ps1`
5. Open http://localhost:8001/

To stop the server, press CTRL+C

## Docker build

1. Install docker https://docs.docker.com/get-docker/
2. `docker build . -t healx`
2. `docker run -p 8001:8001 healx`
3. Open http://localhost:8001/

## Navigating API

### Openapi specification
http://localhost:8001/docs 

### Search webpage
http://localhost:8001/ 

### View bookmarks in webpage
http://localhost:8001/view_bookmarks

## Tests

Run `pytest test` from the base directory

## Improvement considerations
The code represents the minimum requirement to meet the criteria that has been documented. A more complex solution appeared to be outside of the scope of the exercise. The current solution has numerous issues:

1. The data is loaded into memory on startup, if the application is stopped the bookmarking does not persist.
2. The CSV file is downloaded and processed on startup which may be slow depending on internet connection.
3. Bookmarking is stored on a global basis. If this application is used by multiple users
4. The first 1000 entries are displayed from a search to keep reasonable performance. 
5. The webpages are minimally styled and not particularly asthetically pleasing.
6. The search behaviour requirements were not specified, this included which fields should be searched, the sort ordering requirement and any special search text processing such as stem words or phonetic processing on author name searches. As such the simplest version; an in memory exact text match on the displayed fields was employed.

## The following changes would be recommended

1. Store the data in a better medium, the most straight forward would be to use elasticsearch. This would allow for relevance ranking results, word stemming and phonetic processing if necessary.
2. Split the backend and frontend into separate components using a React app for the frontend and having the FastAPI backend only serve JSON data from REST requests. This should allow for straight forward caching of appropriate static resources.
3. Serve the search results either paginated or infinite scrolling to have a performance search page which presents all results.
4. Store user data on a database such as POSTGRES to allow bookmarking to persist and be delivered on a per user basis.
5. Improve the visual asthetic as this has a strong impact on [perceived usability](https://medium.com/aleph-universe/be-aware-of-aesthetic-usability-effect-in-user-research-ac4c93193089).
