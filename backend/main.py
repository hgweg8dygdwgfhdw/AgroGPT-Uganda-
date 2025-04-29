from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import weather, farm, auth, routes
import uvicorn

app = FastAPI(
    title="AgroGPT Uganda API",
    description="""
    AgroGPT Uganda - Agricultural Advisory and Support System

    ## Features
    * 👨‍🌾 Farm Management
    * 🌱 Crop Management
    * 🌦️ Weather Services
    * 🔍 Disease Diagnosis
    * 💰 Market Information
    * 📱 SMS and USSD Services
    * 🌍 Multi-language Support

    ## Authentication
    All protected endpoints require Bearer token authentication. 
    Get your token by using the `/api/v1/token` endpoint.

    ## Documentation
    - `/docs` - Swagger UI documentation (interactive)
    - `/redoc` - ReDoc documentation (readable)
    - Full API documentation is available in the repository at `docs/api.md`
    """,
    version="1.0.0",
    contact={
        "name": "AgroGPT Uganda Support",
        "url": "https://github.com/yourusername/AgroGPT-Uganda-",
        "email": "support@agrogpt-uganda.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "Authentication",
            "description": "Operations for user authentication and token management",
        },
        {
            "name": "Farm Management",
            "description": "CRUD operations for managing farms",
        },
        {
            "name": "Crop Management",
            "description": "Operations for managing crops and their lifecycle",
        },
        {
            "name": "Weather",
            "description": "Weather forecasting and agricultural metrics",
        },
        {
            "name": "Disease Diagnosis",
            "description": "Plant disease diagnosis using image and text analysis",
        },
        {
            "name": "Market Information",
            "description": "Market prices and trends for agricultural products",
        },
        {
            "name": "SMS Services",
            "description": "SMS notifications and USSD service integration",
        },
        {
            "name": "General",
            "description": "Utility endpoints and system information",
        },
    ],
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/v1/openapi.json"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from different modules
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(farm.router, prefix="/api/v1", tags=["Farm Management"])
app.include_router(weather.router, prefix="/api/v1", tags=["Weather"])
app.include_router(routes.router, prefix="/api/v1", tags=["General"])

@app.get("/", tags=["General"])
async def root():
    return {
        "message": "Welcome to AgroGPT Uganda API",
        "version": "1.0.0",
        "status": "active",
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "markdown": "/docs/api.md"
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 