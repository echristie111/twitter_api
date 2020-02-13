[<<< Previous](getting_key.md) | [Next >>>](creating_twitterbot.md )

# Accessing the API

1\. Clone (or download) this repository to your computer and navigate to the folder once it's downloaded.

You can clone the repository with this command in your terminal:

```bash
git clone https://github.com/echristie111/twitter-api.git
```  
or  

```bash
git clone https://github.com/dhsouthbend/twitter-api.git
```
or, go back to the main page and download [here](https://github.com/echristie111/twitter_api)    	

Once you've cloned or downloaded the directory, navigate into it using your command line (or through your GUI/search bar).

2\. Open the my_keys.py file in your text editor, VS Code.

3\. Copy your four numbers (Consumer Key, Consumer Secret, Access Token Key, and Access Token Secret), replacing the xxx on each relevant line. Make sure to keep the single quotes around the numbers.

4\. Save the `my_keys.py` file.

5\. Make sure you have the Tweepy library for Python installed. To check, type

	python

at the command line. When you see the >>> prompt, type

    import tweepy

If you see no output, then Tweepy is already installed, so skip to Step #7. If you get an error, follow Step #6. Once you're finished with Python, type

    exit()

to return to the bash shell.  

6\. If Tweepy isn't installed, run

	pip install tweepy

at the bash shell to install the library.  

7\. To test out your key, run the api.py script:

	python api.py

If you see the name of your Twitter account, everything is working!


[<<< Previous](getting_key.md) | [Next >>>](creating_twitterbot.md)
