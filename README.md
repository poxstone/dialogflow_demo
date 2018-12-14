# DIALOG CALL CALENDAR
- Documentation:
    - [Make - cloud functions](https://cloud.google.com/functions/docs/writing/http#writing_http_helloworld-python)
    - [Deploy - cloud functions](https://cloud.google.com/functions/docs/deploying/)
## INSTALL
- Create Service Account and add "Editor"
- Enable APIS in Main Project:
    - Dialogflow
- Requirements:
  ```bash
  python3.7 -m pip install -r requirements.txt -t ./lib --upgrade;
  ```
### Run Local
```bash
python3.7 app_flask.py;
```

### Test Local
```bash

# Cron export
curl -X POST localhost:8080/calendar_export;

# Confirm text_speech=(acepto|cancelo|reagendo)
curl -X POST localhost:8080/calendar_populate;

# Reagend confirm text_speech=(opcion uno|opcion dos)
curl -X POST localhost:8080/calendar_confirm -H 'Content-Type: application/json' -d '{"id":"camilo.rojas@eforcers.com.co-eforcers.com.co_5006sh1r2q0u07ilusiuealics@group.calendar.google.com-prqm36617okvv001ql66cet3j4","text_speech":"opcion dos"}';

# test service
curl -X POST http://localhost:8080/calendar_service -H 'Content-Type: application/json' -d '{"session_id": "","query_text":"camilo.rojas@eforcers.com.co-eforcers.com.co_bg29m0a1tcbdorho9lt1282u4g@group.calendar.google.com-vt8qomqui5fa1ug6sen0fmrv78"}'

```

## Deploy

```bash
PROJECT="<<PROJECT>>";
gcloud functions deploy "calendar_export" --runtime="python37" --trigger-http --memory=128 --timeout=315 --project="${PROJECT}";
```

## Test deploy
```bash

PROJECT="<<PROJECT>>";

# Cron export (calendar_name,user_email)
curl -k -X POST https://us-central1-${PROJECT}.cloudfunctions.net/calendar_export -H 'Content-Type: application/json' -d '{}';

# Confirm text_speech=(acepto|cancelo|reagendo)
curl -k -X POST https://us-central1-${PROJECT}.cloudfunctions.net/calendar_confirm -H 'Content-Type: application/json' -d '{"id":"camilo.rojas@eforcers.com.co-eforcers.com.co_5006sh1r2q0u07ilusiuealics@group.calendar.google.com-prqm36617okvv001ql66cet3j4","text_speech":"acepto"}';

# Reagend confirm text_speech=(opcion uno|opcion dos)
curl -k -X POST https://us-central1-${PROJECT}.cloudfunctions.net/calendar_confirm -H 'Content-Type: application/json' -d '{"id":"camilo.rojas@eforcers.com.co-eforcers.com.co_5006sh1r2q0u07ilusiuealics@group.calendar.google.com-prqm36617okvv001ql66cet3j4","text_speech":"opcion dos"}';

# Populate
curl -k -X POST https://us-central1-${PROJECT}.cloudfunctions.net/calendar_populate -H 'Content-Type: application/json' -d '{}';

```
