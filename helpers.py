import re, os, binascii

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

from constants import ACCOUNT_JSON, SCOPES_DIALOG, PROJECT_ID


class Credentials:
    @staticmethod
    def get_service_account():
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            ACCOUNT_JSON,
            scopes=SCOPES_DIALOG)
        return credentials


class DialogFlowService:
    calendar_service = None

    def __init__(self, project_id=PROJECT_ID, language_code='es-ES',
                 session_id=''):
        self.project_id = project_id
        self.session_id = session_id if session_id else \
            DialogFlowService.gen_random_id()
        self.language_code = language_code
        self.calendar_service = Credentials.getByServiceAccount()
        self.dialogflow_service = discovery.build('dialogflow', 'v2',
                                           credentials=self.calendar_service)
    @staticmethod
    def gen_random_id():
        session_id = str(binascii.b2a_hex(os.urandom(10)))
        session_id = re.sub('[/\'",]', '', session_id)
        return session_id

    def intent(self, text_query):
        session = 'projects/{}/agent/sessions/{}'.format(self.project_id,
                                                         self.session_id)
        body = {
          "queryInput":
          {
            "text":
            {
              "languageCode": self.language_code,
              "text": text_query
            }
          }
        }

        intent = self.dialogflow_service.projects().agent().sessions().\
            detectIntent(session=session, body=body)

        response_intent = intent.execute()
        return response_intent

    def get_session_id(self):
        return self.session_id
