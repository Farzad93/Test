from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# اجازه‌ی دسترسی از فرانت‌اند (مثلاً از Netlify یا لوکال)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # برای تست، بعداً محدودش کن
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API is working!"}

@app.post("/register")
async def register_user(request: Request):
    data = await request.json()
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")

    # اینجا می‌تونی دیتا رو ذخیره کنی یا لاگ بزنی
    print(f"New registration: {name}, {phone}, {email}")

    return {"message": f"{name} عزیز، ثبت‌نام شما با موفقیت انجام شد!"}