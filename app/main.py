from fastapi import FastAPI

# Create the application object. Uvicorn runs this.
app = FastAPI(title="KOL Analysis Tool")


# When someone sends a GET request to /health,
# run this function and return its result as JSON.
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
