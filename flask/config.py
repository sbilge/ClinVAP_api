
class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    EXTENSIONS = ["json", "vcf", "docx"]
    SECRET_KEY = "throw-away-key"
    UPLOADS = "/app/app/static/input/uploads"
    DOWNLOADS = "/app/app/static/output/downloads"
    NF_CONF = "/app/app/static/input/nf_conf"

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOADS = "/app/app/static/input/uploads"
    DOWNLOADS = "/app/app/static/output/downloads"
    NF_CONF = "/app/app/static/input/nf_conf"
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    UPLOADS = "/app/app/static/input/uploads"
    DOWNLOADS = "/app/app/static/output/downloads"
    NF_CONF = "/app/app/static/input/nf_conf"
