from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, crud, schemas
from .database import engine, get_db
from .hashing import get_password_hash, verify_password

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    # Redirect root URL to signup page
    return RedirectResponse(url="/signup")

@app.get("/signup")
def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if crud.get_user(db, username=username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    hashed_password = get_password_hash(password)
    crud.create_user(db, schemas.UserLogin(username=username, password=hashed_password))
    # After signup, redirect to the login page
    return RedirectResponse(url="/login", status_code=302)

@app.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user(db, username=username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # You should manage session or token here
    # After login, redirect to the blog page
    return RedirectResponse(url="/blog", status_code=302)

@app.get("/blog")
async def blog_home(request: Request, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db)
    return templates.TemplateResponse("index.html", {"request": request, "blogs": blogs})

@app.post("/like/{blog_id}")
async def like_blog(blog_id: int, db: Session = Depends(get_db)):
    # You need to manage session/user_id here
    user_id = 1  # Example user ID
    crud.like_blog(db, blog_id, user_id)
    return RedirectResponse(url="/blog", status_code=302)

@app.post("/comment/{blog_id}")
async def comment_blog(blog_id: int, comment: str = Form(...), db: Session = Depends(get_db)):
    # You need to manage session/user_id here
    user_id = 1  # Example user ID
    crud.comment_blog(db, schemas.CommentCreate(content=comment, blog_id=blog_id), user_id)
    return RedirectResponse(url="/blog", status_code=302)

@app.get("/logout")
def logout():
    # Implement logout functionality here (e.g., clear session or token)
    return RedirectResponse(url="/login", status_code=302)

@app.get("/add-blog")
def add_blog_form(request: Request):
    return templates.TemplateResponse("add_blog.html", {"request": request})

@app.post("/add-blog")
async def add_blog(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    new_blog = schemas.BlogCreate(title=title, content=content)
    crud.create_blog(db, new_blog)
    return RedirectResponse(url="/blog", status_code=302)
@app.get("/add-blog")
def add_blog_form(request: Request):
    return templates.TemplateResponse("add_blog.html", {"request": request})

@app.post("/add-blog")
async def add_blog(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    new_blog = schemas.BlogCreate(title=title, content=content)
    crud.create_blog(db, new_blog)
    return RedirectResponse(url="/blog", status_code=302)
