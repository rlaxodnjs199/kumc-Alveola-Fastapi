import os
import sys

import uvicorn

if sys.argv[1] == "dev":
    os.environ["ENV"] = "dev"
elif sys.argv[1] == "prod":
    os.environ["ENV"] = "prod"
else:
    print("Wrong env setting provided: Please choose between dev and prod.")
    exit()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
