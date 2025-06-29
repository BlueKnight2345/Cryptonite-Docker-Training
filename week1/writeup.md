Started off with making the simple Flask todo app, then proceeded to make the required Dockerfile for it.

Basic docker commands used:

`
docker build -t flask-app .
`

`
docker run -p 5000:5000 flask-app
`

Starting off by pulling the python slim base image, setting a working directory, copy all the files from our folder into the docker working directory, ensuring requirements are satisfied and then finally exposing the required port and running the python app.

To go ahead with the following tasks, to use gunicorn instead of flask run, made changes to the dockerfile, changing the command to run the file and modified the python file 

The next task involves using volumes to ensure the data in the sqlite database persists beyond the lifetime of the docker container.

this can be achieved using the command 

`
docker run -v $(pwd)/instance:/app/instance flask-app
`

which binds the ../instance folder on my machine to the /app/instance folder in the docker container

The next task involves bind mounts, which enable us to edit files locally and see the results live within the docker container and avoids us having to rebuild the container everytime we make an edit.

We start off my modifying `COPY . . ` as this freezes the code in the image and doesn't allow us to make edits.

We may change it to `COPY requirements.txt .`

So now instead of our image containing the code which is built into the container, we bind the code which we have locally directly into the container.

So we run `docker run -p 5000:5000 -v $(pwd):/app flask-app` after building the image again

which binds our present working directory to `/app`


With this any modifications made to static files like html or css and reflected within the app running on the container

I verified this by changing some of the css code.

I modified my flask app with environment variables to test their functionality by modifying a page banner based on environment variables passed.

`docker run -p 5000:5000 -v $(pwd):/app -e ENV_VAR=1 flask-app`

```
def index():
    app_mode = os.getenv("ENV_VAR", "base")

    if app_mode == "1":
        banner = "variable is now set to 1"
    elif app_mode == "2":
        banner = "variable is now set to 2"
    else:
        banner = "No variable has been set"
```
Environment variables can be useful to change app functionality for different purposes based on the environment variable set such as a mode which displays logs for debugging.

Now we move on to the netcat shell

<!-- We create a non root user with `RUN useradd -ms /bin/bash user` giving it a home directory and letting it use bash

We then install updates as well as netcat and bash

We then create a writeable directory and give access to the user and finally listen on port 9001 and switch to user when someone connects.
 -->

Ok this part gave me a lot of trouble, had to gpt my way through a lot of this, but got several errors with netcat.

faced issues such as it instantly shutting down the container before it could connect, spamming error messages and unable to connect all together.

ended up ditching netcat in the docker image and using socat instead, need to take some more time to understand this properly.
