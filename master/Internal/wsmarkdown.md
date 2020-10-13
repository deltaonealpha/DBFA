---
name: 'Telegram and Python'
description: 'Connect Telegram and Python to create some awesome stuff'
author: '@deltaonealpha'
img: '<dta_insert_placeholder>'
---

# Hello, _world_!
<br />
<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>Hmm... Telegram.. Python?</h3>
</div>

Yes, Telegram, it is one of the world’s leading messaging apps. <br /> Well, “one of the leading apps”. Why Telegram of all?<br /><br />Well, for starters, it is one of the very few messaging companies that provide open-source API access to everyone. All of Telegram (except the server software) is completely open source!<br />In fact, the official Telegram app is rather called a client. As its open source, there are literally a gazillion Telegram clients out there.<br />You don’t like your client? Code one yourself, it is that flexible!  
<br />

<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>But Python..?</h3>
  <h5>Why would one even connect the two?</h5>
</div>


Python is a leading language today. Being extremely flexible and one of the easiest languages to learn, Python has a lot going for it, and connecting the just makes a lot of sense.

Let me give you an example.
My father’s friend lost a lot of money because his restaurant’s manager logged meagre sales and pocketed much of the profit.
On hearing this, I started to think, what if every purchase got logged on its own, in a place inaccessible for everyone but the owner? 
Pondering on a way to solve this, I created DBFA, a scalable billing framework written in Python3. It can manage your store, employees, payments, inventory, orders, deliveries, invoicing, and a lot more.
A core feature of DBFA is complete Telegram logging. As soon as a bill is issued, it immediately logs the sales activity in the store owner’s Telegram account as a message from a bot, with all communications over TSL-encrypted HTTPS. Not only this, it even logs every event where store data is being accessed.

Expanding on this, I even added inline button-based two-factor-authentication as text inputs can be super manipulative.
Yeah, all using Telegram and Python! What I did is nothing compared to what you all can do. Yeah, *you!*


<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>Sounds nice?</h3>
  <h5>Let’s plan this workshop then!</h5>
</div>

_Requisites:_
-	Basic Python skills.
-	A Telegram account.
-	pip install requests

_Topics:_
-	Creating a Telegram bot
-	A bit on Telegram’s WEB BOT API
-	Connecting and sending a message
    o	Understanding the code
-	Receiving messages from the bot
    o	Understanding the code
-	A small project combining all this
-	_EXTRA RESOURCES_: Marking received messages as read and a   dive into BOT API v2 and inline stuff!

_NOTE_: This workshop will be a quick one, so that it can be made quickly without getting boring. 
For the inquisitive ones out there, there will be some references and resources attached at the end so you can tinker a bit more.


<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>BOTS EVERYWHERE</h3>
  <h5>Creating a bot in Telegram!</h5>
</div>
 
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture1.png?raw=true

Telegram has these ‘bots’, or simple chats which can be handled autonomously. They’re basically a way for developers and service providers to automate interactions.
To interface with a bot, we first need to create one, and get its credentials.
Making a bot is quite easy. Ironically enough, you create bots via a bot called _‘BotFather’_. 
https://t.me/BotFather
<br />Its Telegram’s official bot.


<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>SENDING MESSAGES</h3>
  <h5>Time to experiment!</h5>
</div>

Telegram’s WEB API is remarkably simple, yet powerful, allowing you to essentially send and retrieve messages just by visiting a URL! 

We will now try out an example:
-	Randomly ping this bot on Telegram: https://t.me/get_id_bot
and save the ‘chat ID’ it gives you.
-	Then, head over here: https://repl.it/@deltaonealpha/BasicTelegramBotSendText

Try running this repl.it by entering your bot’s access token and the chat ID you received by pinging the _get_id_ bot.
--
_get_id_ is a wonderfull bot created by Fredy Kardian Udo (t.me/fredykardian)
--

When you are done with trying this out, proceed ahead.


<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>DISECTING THE CODE</h3>
</div>

Now that we have experienced how seamlessly the WEB API works (I hope you did not skip), let us trace down every line: 
This is requests, an alternative to Python’s built-in URLLIB. This needs to be installed via _pip_ (command in workshop requisites section) if you’re running this off your own PC. 
Running this code on repl.it doesn’t require you to pip.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture2.png

Now we define a function, _sendMsg()_. To call this function, we will need to pass three parameters with it, your _bot’s token_, your _chat ID_ and the text you need to send. As simple as that!
_send_text_ concatenates your token, chat ID and message with the base URL of Telegram’s API. This includes the method _sendMessage_, which is used to… well, send messages.
Now we define and call a variable, response, which allows us to use the requests module’s get function to access the URL we stored in the variable _send_text_, in the above step.
Now we just return _response.json_ in an effort to improve our code and unify things.
And…. that’s it!
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture8.png?raw=true

What follows is just a bunch of input() statements to receive values from the user to pass-on to the function.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture9.png?raw=true

Then we create a text variable with out text, and simple pass it to the function!
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture10.png?raw=true



<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>RECEIVING MESSAGES</h3>
</div>

Remember using _sendMessage_ in the URL when sending a message via your bot?
To receive messages, we use _getUpdates_. Telegram handles receiving messages brilliantly! Whenever you call _getUpdates_ with your bot token, it returns a .JSON with all your queued messages.
Why do I say “queued”? Because your messages don’t clear till you issue a “receipt” to Telegram of the same.
Each message comes with an _updateID_, which you can return to Telegram to clear that from the queue. For example, if you have 10 messages, simply passing the _updateID_ of the latest message clears all 10 messages.
Yeah, this might sound complex, but this small demonstration on repl.it should make it seem all easy-peasy!

Send a few texts to your BOT via Telegram, then visit this link, and enter your BOT’s token:
https://repl.it/@deltaonealpha/TelegramGetUpdates#main.py


Worked marvellously, right?
Code dissection follows.

<div style={{ padding: '20px', backgroundColor: 'tomato' }}>
  <h3>DISECTING THE CODE</h3>
</div>

Again, we import _requests_ and _json_. Since _json_ is a part of Python’s standard library, you won’t need to install it when using this code on your local installation.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture11.png?raw=true

Now we take an input for the BOT token, and concatenate it with the required URL, issuing _getUpdates_. Then we define a variable updates, as a .JSON returned by requests.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture12.png?raw=true

And now? We simple slice the text out, and print.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture13.png?raw=true

And… that’s it!


<div style={{ padding: '20px', backgroundColor: 'magenta' }}>
  <h3>Its PROJECT TIME</h3>
</div>

Now since we are all aware of basic Telegram BOT controls, why not make a 5-minute project integrating all this? 
In this mini-project, we will be asking the user for their chat ID and bot token, and telling them to send a “hello” to our bot. If the bot detects “hello”, it will respond with a greeting and if it doesn’t, it will send a different reply ;)
Let’s start!

We start by importing _requests_ and _json_ to handle sending and receiving messages, and then time to include delays in our code.
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture14.png?raw=true

Now we take inputs from the user:
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture15.png?raw=true

Now, the user is instructed to send “hello” to their Telegram bot and then enter any key to proceed. 
(We have to wait for a confirmation else the code will immediately proceed to replying when the user hasn’t even sent anything :D)
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture16.png?raw=true

Now, we simply concatenate the inputs into a URL and define a variable _updates_ as a request to this URL:
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture17.png?raw=true

Then we print the slice the .JSON received, print the received text and put it in an _if…else_ block to compare it and detect whether the message is “hello” (or its case variations) or something entirely different! 
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture18.png?raw=true

If the message is _“hello”_, we send a greeting back!
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture19.png?raw=true

If the message is not “hello”, we still send a message back, but a different one: 
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture20.png?raw=true


And… that’s it!
P.S. You can send multiple messages, one _“hello”_, and maybe one not that, and the bot will reply to each!
You can try this on a repl.it if you feel too lazy to code: https://repl.it/@deltaonealpha/TelegramWorkshopSampleProject#main.py

Screenshots:
#### repl.it shell
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture22.png?raw=true

#### Telegram chat window
https://github.com/deltaonealpha/PyTelegramWorkshop/blob/main/assets/Picture23.png?raw=true


<div style={{ padding: '20px', backgroundColor: 'magenta' }}>
  <h2>Goodbye!</h2>
</div>

That was all for this workshop. This is the first ever workshop that I’ve made in my life and the first time when I’ve tried to teach something to such a wide and diverse community!
I really hope this workshop was fun. If you have any doubts, contact me on HackClub’s Slack: @deltaonealpha (https://hackclub.slack.com/team/U01AVFQUCAD)

_(P.S For those who’d like to stick around longer, there are a few external resources linked below as a bonus, which allow you to make this part of something even bigger! Hack on!)_
