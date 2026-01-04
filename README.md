# GCM Connector
This is a simple connector to talk to the data uploaded from
a Freestyle Libre 2 Plus Sensor.

# Usage
Assuming you already have a sensor uploading data download the 
LibreLinkUp application and create an account. LibreLinkUp application 
explains how to access you sensor data.

## Credentials
Copy the following contents into your `claude_desktop_config.json` file. This
is usually located here `~/Library/Application\ Support/Claude/claude_desktop_config.json`.

```
"mcpServers": {
        "blood_sugar_history": {
            "command": "uv",
            "args": [
                "--directory",
                "/PATH/TO/CODE/DIRECTORY",
                "run",
                "main.py"
            ],
            "env": {
                "API_USERNAME": "username@youremail.com",
                "API_PASSWORD": "supersecret"
            }
        },
        "blood_sugar": {
            "command": "uv",
            "args": [
                "--directory",
                "/PATH/TO/CODE/DIRECTORY",
                "run",
                "main.py"
            ],
            "env": {
                "API_USERNAME": "username@youremail.com",
                "API_PASSWORD": "supersecret"
            }
        }
    }
```

If you don't have the file cp the example from the route of this directory:
```
cp claude_desktop_config.json  ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

In your `~/Library/Application\ Support/Claude/claude_desktop_config.json`, update the `API_USERNAME` and
`API_PASSWORD` with the credentials you used to set up the LibreLinkApp.

Now restart Claude and see if the connector appears as below in the image:

![alt text](images/Connector%20Example.png "Connector example")

# Running
Fire up Claude and ask something related to your blood sugar.

## Current
Ask `get my current blood sugar`:
![alt text](images/Blood%20Sugar%20Current.png "Current blood sugar example")

Ask Claude to work with your data `draw a graph on my blood sugar history`:
![alt text](images/Blood%20Sugar%20History.png "Blood sugar history example query")
