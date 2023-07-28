from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from .manager import get_user_manager
from .models import User
from config import SECRET_AUTH
from fastapi import APIRouter, Depends, Request


router = APIRouter(
    prefix="/authapi",
    tags=["Authapi"]
)
bearer_transport = BearerTransport(tokenUrl="auth/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)

jwt_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

async def get_enabled_backends(request: Request):
    """Return the enabled dependencies following custom logic."""
    if request.url.path == "/protected-route-only-jwt":
        return [jwt_backend]
    else:
        return [jwt_backend]

current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)


@router.get("/protected-route-only-jwt")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated with a JWT."



