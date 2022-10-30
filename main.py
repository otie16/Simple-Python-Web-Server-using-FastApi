from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
def user_info():
    # server does something
    return {"slackUsername": "otie", "backend": True, "age": 23, "bio": "A talented young developer with a flair for solving real world problems with code"}
