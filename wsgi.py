from app import create_app

application = create_app()  # Note: using 'application' instead of 'app'

if __name__ == "__main__":
    application.run()
