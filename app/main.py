from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings



#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# my_posts = [{"title": "title of post ", "content": "content of post 1", "id": 2000},
#              {"title":"my Favourite team", "content": "I love Chelsea footbal club", "id": 2}, 
#              {"title":"my Favourite team", "content": "I love Chelsea footbal club", "id": 25}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] ==id:
#             return i
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
    

@app.get("/")
def root():
    return {"message": "Welcome to My Api!!!!!"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
    
#     posts = db.query(models.post).all()
#     return {"data": posts}




