# Fastapi : framewrok that handle server side operations

from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initialize our fastapi app
app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)

# model & tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("device:", device)
model.to(device)

# templating
templates = Jinja2Templates(directory=".")

# Input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text):
    text = re.sub(r"\n+", " ", text)      # remove new lines
    text = re.sub(r"\s+", " ", text)      # remove extra spaces
    text = re.sub(r"<.*?>", "", text)     # remove html tags
    text = text.strip().lower()
    return text


def summarize_dialogue(dialogue):

    dialogue = clean_data(dialogue)

    # tokenize
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # generate summary
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # decode output
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary


# API Endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):

    summary = summarize_dialogue(dialogue_input.dialogue)

    return {
        "summary": summary
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )