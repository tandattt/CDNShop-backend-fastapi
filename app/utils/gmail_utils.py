import os
import base64
import pickle
from pathlib import Path
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from app.core.config import settings

# Base directory (root of the project)
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration from settings
SCOPES = settings.SCOPES
TOKEN_PICKLE = BASE_DIR / 'templates' / 'pickle' / 'token.pickle'
CLIENT_SECRET_FILE = BASE_DIR / 'templates' / 'json' / 'cdn.json'
EMAIL_TEMPLATE_PATH = BASE_DIR / 'templates' / 'emails' / 'email_template.html'


def gmail_authenticate():
    creds = None
    if TOKEN_PICKLE.exists():
        with open(TOKEN_PICKLE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PICKLE, 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service


def format_amount(amount: float) -> str:
    """Format amount with comma as thousand separator and VND symbol"""
    return "{:,.0f}₫".format(amount)


def load_template(template_path: Path) -> str:
    """Load HTML template from file"""
    return template_path.read_text(encoding='utf-8')


def create_message(to: str, order_id: str, amount: float) -> dict:
    """Create email message using HTML template"""
    template = load_template(EMAIL_TEMPLATE_PATH)
    formatted_amount = format_amount(amount)

    message_text = template.replace('{{order_id}}', order_id)\
                        .replace('{{formatted_amount}}', formatted_amount)

    subject = "Thanh toán thành công CDN_Shop"
    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}


def send_message(service, user_id: str, message: dict):
    sent_message = service.users().messages().send(userId=user_id, body=message).execute()
    return sent_message['id']

