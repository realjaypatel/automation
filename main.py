from fastapi import FastAPI, Request, status
from routers import app1, app2


app = FastAPI()



@app.get("/healthy")
def health_check():
    return {'status': 'healthy'}

app1.main()

app.include_router(app2.router)