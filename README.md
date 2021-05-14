# Anti-Cheat Bot

To start the bot, first install dependencies for both the client and server. In the server folder, use `python -m venv venv` to create a virtual environment. Then,
run `venv/bin/activate` to start the virtual environment. Then install dependencies with `pip install -r requrements.txt`. Once you've done this, you can start the server
using `python run.py`.

To install dependencies for the client, go into the client folder and run `npm install` or `yarn install`, depending on whether you use npm or yarn. Then start the client
using `npm start` or `yarn start`.

Once both the client and server are running, visit http://localhost:3000 to view the application.

## Production

To create a production build, run `npm run build` or `yarn build` in the `client` folder. Then visit http://localhost:5000 to view the application.
