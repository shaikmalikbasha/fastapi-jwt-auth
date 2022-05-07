from fastapi import FastAPI

from app import auth, index_controller, role_controller, routes, user_controller
from app.db_setup import Base, engine

API_VERSION = "/api/v1"
app = FastAPI()


# @app.on_event("startup")
# def init_database():
#     print("Initializing the database...")
#     Base.metadata.create_all(bind=engine)
#     print("Successfully initialized!")

app.include_router(routes.router, prefix=API_VERSION)

# app.include_router(user_controller.router)
# app.include_router(role_controller.router)
# app.include_router(auth.auth_router)
# app.include_router(index_controller.admin_router)
# app.include_router(index_controller.manager_router)
# app.include_router(index_controller.user_router)
