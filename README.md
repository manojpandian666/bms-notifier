# BookMyShow-notifier
Get Notified in telegram if your movie tickets opened in your favourite theatre.
<br>
<br>
![image](https://user-images.githubusercontent.com/75692359/170918735-8da774f8-d2f9-4d95-8bdb-363c09638856.png)
<br>
<br>

Let's say you want notification if your favourite theatre opens tickets for **VIKRAM** movie.
1. Go and grab the url from bookmyshow page url like shown in the above image. 
<br>
<strong>bookmyshow --> open your movie --> click book tickets --> grab the url from page</strong>
<br>
<br>
2. Then copy the theatre name from the same page as it is.[This should be same string as in web page]
<br><br>
3. Then create a bot in telegram and copy bot id from it. [Link](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
<br><br>
4. Then get chat id by following steps in this link. [Link](https://www.alphr.com/find-chat-id-telegram/)
<br><br>
5. Voila... Everything is done. Just paste these four parameter in config_vars in heroku and you are ready to go.
<br>
This will work only in local machine. If you need some online solution, try to use any hosting provider to host your code.
<br><br>

## Hosting (Heroku)

If you came this far you should be intelligent enough to figure out by yourself. Just kidding use the below button to deploy it to heroku.<br><br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/manojpandian666/bms-notifier)
<br><br>**Add these config_vars**
![image](https://user-images.githubusercontent.com/75692359/170926888-f712c876-65e8-4ed5-ad58-d247dec3e0e9.png)
<br><br>
After deploying in heroku make sure to turn on the worker.
<br><br>
![image](https://user-images.githubusercontent.com/75692359/170928832-97d0cfa7-cca8-46a7-9d38-7a7fed934047.png)
<h3 style="text-align:center;">Made with ♥️ by Manoj Pandian</h3>
