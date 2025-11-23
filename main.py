"""
Spade App - Entry point for running the backend server locally
"""
import uvicorn

def main():
    print("Starting Spade App backend server...")
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
