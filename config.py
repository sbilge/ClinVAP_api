
class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    ALLOWED_EXTENSIONS = ["json", "vcf", "docx"]


    # UPLOADS = " path/to/the/server"
    # DOWNLOADS = "path/to/the/server"
    # SECRET_KEY = "" random string or download python secret module from python or os.random get a random string. What if secret key anywys

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    UPLOADS = "/Users/bilges/Desktop/abi_tuebingen/clinical_reporting/ClinVAP_app/app/static/input/uploads"
    DOWNLOADS = "/Users/bilges/Desktop/abi_tuebingen/clinical_reporting/ClinVAP_app/app/static/output/downloads"
    # SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False

    # UPLOADS = "path/for/testing"
    # DOWNLOADS = "path/for/testing"

