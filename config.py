
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
    UPLOADS = "uploads/folder/here"
    DOWNLOADS = "downloads/folder/here"
    # SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
    # UPLOADS = "path/for/testing"
    # DOWNLOADS = "path/for/testing"

