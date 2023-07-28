from fastapi import FastAPI
from auth.base_config import auth_backend, fastapi_users
from auth.base_config import router as router_authapi
from auth.schemas import UserRead, UserCreate
from fastapi.middleware.cors import CORSMiddleware
from shop.router import router as router_shop
from product.router import router as router_product
from order.router import router as router_order
from google_config import google_oauth_client

app = FastAPI(
    title="RestoflowAPI"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_authapi)

app.include_router(router_product)

app.include_router(router_shop)

app.include_router(router_order)

app.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        auth_backend,
        "SECRET",
        is_verified_by_default=True,
    ),
    prefix="/auth/google",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_oauth_associate_router(google_oauth_client, UserRead, "SECRET"),
    prefix="/auth/associate/google",
    tags=["auth"],
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

