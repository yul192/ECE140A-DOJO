import multipart
from fastapi import FastAPI, Form


# Create the FastAPI instance
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes")
async def read_notes():
    """
    Read the notes from the file and return them.
    :return:
    """
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No notes yet."
    return {"notes": content}


@app.post("/notes")
async def write_notes(note: str = Form(...)):
    """
    Write the notes to the file. post your messages to the notes endpoint.
    :param note:
    :return:
    """
    with open("notes.txt", "w") as file:
        file.write(note)
    return {"message": "Note saved successfully."}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
