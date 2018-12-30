# FacebookDataApp
Ultimate tool for making sense of your facebook data!

In order to use this application you will first need to download your facebook data via the facebook website in the settings. Here's an article that shows how: https://www.wired.com/story/download-facebook-data-how-to-read/. This process can take a couple of days, trust me its a lot of data. Once you've gotten your data, place it in the `app/facebook_launcher/` folder and make sure to name the data folder `facebook_data`.

#### Important: Your directory needs to be named `facebook_data` in order for the app to work.

Once you've done this, you're all set! Run the command `flask run` in order to launch the app. In a couple of seconds you should see the screen below: 


Note: If you encounter problems when running the command `flask run` try the following command: `export FLASK_APP=facebook.py` and then try `flask run` again.

Now that you are at the right page, Enter your name in the first box and a friends name in the second box and hit the "Count Messages!" button. If everything went well you should a screen like the one below:


Well, everything else should be pretty simple, feel free to try running the app with all your friends! If you have any ideas for future functionality that you would like to see definitely let me know!
