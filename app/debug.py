from fastapi import APIRouter, FastAPI, status

router = APIRouter()


@router.get("/crash", tags=["debug"])
def test_crash():
    1 / 0


@router.get("/no_content", status_code=status.HTTP_204_NO_CONTENT, tags=["debug"])
def no_content():
    return


def mount_debug_endpoints(app: FastAPI):
    app.include_router(router)
