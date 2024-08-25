class Config:
    # SECRET_KEY = '29dd6a597acb9246445ecb373cffb8b02af0d96eac93d7aa3a8abee04d68513e'
    JWT_SECRET_KEY = '8e69f1b5a65c9df31a479d5b9d9e6aac79ed8809fdc3b1dff72dc7396c07975b'  # Change to a strong secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
