from google import genai
import csv
import google.generativeai as gen
import json

gen.configure(api_key="AIzaSyDCkb9IUsp9NSQBhWXMAmkJLDbYtwZV23Y")
client = genai.Client(api_key="AIzaSyDCkb9IUsp9NSQBhWXMAmkJLDbYtwZV23Y")

def generate_output2(input):
    response = client.models.generate_content(
      model="gemini-2.0-flash", contents=f"{input} cast and crew",
      config = {
        'response_mime_type' : 'application/json'
      }
    )
    reply = response.text
    return reply

def getcsv_response(pathname : str) -> list[str]:
  parts = [f"----csv ${pathname}-----"]
  with open(pathname, "r", newline="") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
      str = " "
      parts.append(str.join(row))
  print(parts)
  return parts


def research_csv(input):
  model = gen.GenerativeModel(model_name="gemini-2.0-flash")
  config = {
        'response_mime_type' : 'application/json'
       }
  convo = model.start_chat(history=[
    {
      "role":"user",
      "parts": getcsv_response("csv1.csv")
    }
 ])

  prompt = "Could you generate csv with updated status of this data based on history provided, for Reconciliation? hide history data"

  data = {
    "prompt": prompt,
    "data": getcsv_response(input)
  }

  chat = convo.send_message(json.dumps(data))
  return chat.text



def reconcile_csv_usecase1(input):
  model = gen.GenerativeModel(model_name="gemini-2.0-flash")
  config = {
        'response_mime_type' : 'application/json'
       }
  convo = model.start_chat(history=[
    {
      "role":"user",
      "parts": getcsv_response("history_data.csv")
    }
 ])

  prompt = "Could you generate csv with updated status of this data based on history provided, for Reconciliation? also add the comment based on history data? hide history data"

  data = {
    "prompt": prompt,
    "data": getcsv_response(input)
  }

  chat = convo.send_message(json.dumps(data))
  return chat.text