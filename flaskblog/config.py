import os


class Config:
    # ==========================================
    # Core Flask Configuration
    # ==========================================
    SECRET_KEY = os.environ.get('SECRET_KEY')

    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY environment variable is required")

    # ==========================================
    # Database Configuration
    # ==========================================
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///site.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'in-v3.mailjet.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() == 'true'

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    MAIL_MAX_EMAILS = 5
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False