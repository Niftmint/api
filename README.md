# niftmint
Flask application that interfaces with the NFT smart contract, formats the output and returns the output. web service is hosted on heroku.

# HEROKU
## DEPLOYING
To deploy to Heroku, use the following git push command to push code from your local repository’s main branch to the heroku remote:

    > git push heroku main

This step only needs to be performed once. To setup a remote to your local repository:

    > heroku git:remote -a niftmint

## LOGGING
To view logs:

    > heroku logs --app niftmint

# VIRTUAL ENVIRONMENT
## CREATE 
    > python3 -m venv virtual   [where 'virtual' is folder name of the virtual environment]

## ACTIVATE 
	> source virtual/bin/activate  [where 'virtual' is the folder of the virtual env]

	DEACTIVATE VIRTUAL 
	> deactivate

## INSTALL PYTHON MODULES IN VIRTUAL ENVIRONMENT
    > pip3 install -r requirements.txt
