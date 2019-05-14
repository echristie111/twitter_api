[<<< Previous](accessing_api.md) | [Next >>>](scraping_data.md)

# Creating a Twitterbot

Once you have the api.py script working, open it with your editor and try uncommenting some of the other lines at the bottom. You should be able to post a tweet to your account and to perform a Twitter search.

For example, to tweet out a message, remove the `#` symbols and extra space from the front of this line:

```python
### api.update_status(status="Look at me! I'm tweeting this using APIs. #INDHRI @dhsouthbend @enc213")
```

Once you have uncommented and changed the text, save your file and run "python api.py" again from Git Bash. Then, check your Twitter account afterwards to see if it worked. Once you're comfortable connecting to and using the Twitter API, you can use the twitterbot.py script in this repository to create your own Twitterbot! See the comments in twitterbot.py for more information.


[<<< Previous](accessing_api.md) | [Next >>>](scraping_data.md)
