from fastapi import FastAPI
from .routers import router, product_api
import logging.config
import instana

import os

logger = logging.getLogger("productService")
os.environ['AUTOWRAPT_BOOTSTRAP'] = "Instana"

# Set logger name to project

logger.info("START Application")

# Tags for representative endpoints
tags = [
    {
        "name": "routers",
        "description": "Operations with xxx",
    }
]

# Define Fast api and description
app = FastAPI(
    title="Product service for Instana",
    description="This is a template of python MSA used in Garage project.",
    version="0.0.1",
    openapi_tags=tags,
)

# Add routers to main
app.include_router(router.router)
app.include_router(product_api.router)


# This path is for health check or test
@app.get("/")
async def root():
    return {"Hello World :D"}
