from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000", 
            "https://flying-briefly-fox.ngrok-free.app", 
            "https://flying-briefly-fox.ngrok-free.app/docs", 
            "http://localhost:8000",
            "*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

# new with ngrok