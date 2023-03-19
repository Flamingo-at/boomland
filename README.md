<h1 align="center">Boomland</h1>

<p align="center">Claim daily tokens $BGEM from <a href="http://boomland.io/daily">Boomland.io</a></p>
<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>

## ⚡ Installation
+ Install [python](https://www.google.com/search?client=opera&q=how+install+python)
+ [Download](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github) and unzip repository
+ Install requirements:
```python
pip install -r requirements.txt
```

## 💻 Preparing
+ Create ```wallets.txt``` in the project folder
+ Insert wallets each on a new line
  + Example: ```address:private_key```
+ The wallets should already have MATIC for the commission. For this you can use <a href="https://disperse.app/">disperse</a>
+ Run the bot:
```python
python boomland.py
```

**Wallets that successfully claim tokens will be in** ```successfully.txt``` **in the format** ```{address}:{private_key}:{balance_matic}```

## 📧 Contacts
+ Telegram - [@flamingoat](https://t.me/flamingoat)
