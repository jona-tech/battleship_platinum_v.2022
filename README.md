
# A
## A
### A
#### A
##### A
###### A

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Bugs

* invalid syntax in input(enter row 1-5)
* fix input('enter row 1-5')

* if statement for row input in pick_a_ship var doesn't loop
* changed if statement to while loop

* Hardest obstacle: figuring out how to make ships invisible for users
* fix: show one empty board while getting ship values from invisible board
