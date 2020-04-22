
class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    EXTENSIONS = ["json", "vcf", "docx", "png"]
    SECRET_KEY = "throw-away-key"
    # UPLOADS = " path/to/the/server"
    # DOWNLOADS = "path/to/the/server"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    # UPLOADS = " path/to/uploads"
    # DOWNLOADS = "path/to/downloads"
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    # TESTING = True
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    # UPLOADS = " path/to/uploads"
    # DOWNLOADS = "path/to/downloads"

