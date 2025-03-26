#Steps
To install python command -
Open cmd - python3 <Enter> -> download from store

Import project into vs code.

Open terminal

cd .\requirement\  
pip install -r .\req.txt

If uvicorn command not found then, run - pip install uvicorn
If gemini ai not installed - 
In new terminal -
pip install -q -U google-genai


Refer https://ai.google.dev/gemini-api/docs/quickstart?lang=python to generate api key. Refer instruction.
geminiUtil file -
Paste it in api_key = ""

python -m uvicorn main:app --reload
swagger - /docs

Below 2 endpoints to be used. Sample csv - csv_user.csv, usecase1_test.csv attached could be used to post below apis.
/csvRecon - 
/csvRecon/usecase1 -

---------------------------
