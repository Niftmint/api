# niftmint
Flask application that interfaces with the NFT smart contract, formats the output and returns the output. web service is hosted on heroku.

# HEROKU
## CREATE
Create the application in heroku:

    > heroku create niftmint

To setup a remote to your local repository:

    > heroku git:remote -a niftmint

## DEPLOY
To re-deploy to Heroku, use the following git push command to push code from your local repository’s main branch to the heroku remote:

    > git push heroku main

## ACCESS
To connect to the web service:

    > heroku open

## LOGGING
To view logs:

    > heroku logs --app niftmint

# INSTALL PYTHON MODULES
    > pip3 install -r requirements.txt

# RUNNING LOCALLY
Specify the application name:

    > export FLASK_APP=app

To run flask:

    > flask run

# INTERFACING WITH SMART CONTRACT
See comments in routes.py for how to generate the abi of the smart contract you want to interact with.
