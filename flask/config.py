
class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    EXTENSIONS = ["json", "vcf", "docx"]
    SECRET_KEY = "throw-away-key"
    # UPLOADS = " path/to/the/server"
    # DOWNLOADS = "path/to/the/server"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    # UPLOADS = "/Users/bilges/Desktop/abi_tuebingen/clinical_reporting/ClinVAP_app/flask/app/static/input/uploads"
    # DOWNLOADS = "/Users/bilges/Desktop/abi_tuebingen/clinical_reporting/ClinVAP_app/flask/app/static/output/downloads"
    UPLOADS = "/app/app/static/input/uploads"
    DOWNLOADS = "/app/app/static/output/downloads"
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    UPLOADS = "/app/app/static/input/uploads"
    DOWNLOADS = "/app/app/static/output/downloads"
