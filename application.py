from app import create_app
application = create_app('default')
#windows cmd ren gitignore.txt .gitignore #
if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8080')
