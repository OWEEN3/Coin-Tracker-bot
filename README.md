# 🚀 Coin Tracker bot

A simple Telegram bot for monitoring cryptocurrency prices.

## 🛠️ Technologies
- Python (`python-telegram-bot`)
- SQLAlchemy
- PostgreSQL
- Alembic
- Redis

## 📦 Installation and Setup
1. Change the bot token in the `.env` file.
2. Build images and start containers using Docker Compose:
```docker compose build ```
```docker compose up```

## ✨ Features

Every 60 seconds (interval configurable) the bot queries the Binance API to get the latest cryptocurrency prices.
Price data is stored in the bot’s internal storage.
When starting to work with the bot, the user receives a welcome message and the bot menu. The user data is saved in the database so as not to display a welcome message every time the user writes the ```/start``` command.

<img width="462" height="398" alt="image" src="https://github.com/user-attachments/assets/13cf5ca5-78ee-478b-a9e2-37a0f86f708e" />

At first, users have no coins to track. 

<img width="177" height="76" alt="image" src="https://github.com/user-attachments/assets/99478c21-dd4c-4cbe-af42-fbd5b7636dc2" />

But they can be added in the corresponding menu item.


<img width="165" height="117" alt="image" src="https://github.com/user-attachments/assets/95a23aaf-2b1f-4a5a-9ae3-ca1aff0af019" />

Users can add and remove cryptocurrencies in their watchlist. All information about the tracked cryptocurrencies of users is also stored in the database.

<img width="190" height="190" alt="image" src="https://github.com/user-attachments/assets/d64fcf15-ec05-4f0b-af82-5aef035bd87f" />

In the *Settings* section, users can:

* Enable or disable price updates.

* Configure the update interval.

* Choose the type of updates: either edit existing messages or send new ones.

<img width="274" height="194" alt="image" src="https://github.com/user-attachments/assets/ccf0f9ec-af64-4b1e-b370-08950a04e78a" />

For the update to work, the user needs to go to the watchlist. If it is enabled, the user's watchlist will be added to the redis. The message with the coin rate will be updated, or a new one will be sent at the configured interval:

| Update | New |
| ------ | --- |
| <img width="180" height="100" src="https://github.com/user-attachments/assets/6c5097ec-f90e-441a-b5c2-a2e2580bdae3" /> <br> <img width="198" height="118" src="https://github.com/user-attachments/assets/96c240e2-d654-4038-a1ca-fbdebf70a34f" /> | <img width="185" height="103" src="https://github.com/user-attachments/assets/bba574bd-3b37-4954-af98-e59c12d273df" /> <br> <img width="201" height="223" src="https://github.com/user-attachments/assets/181122d1-2615-4985-a74e-67a8726d3fa8" /> |


