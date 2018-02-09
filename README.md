# slackbot-exchange-rate

Slack bot to ask echange rate.

## Settings

* Make your work space on [Slack](https://slack.com/)
* Install [Bots](https://tech-test-ca.slack.com/apps/A0F7YS25R-bots) to your Slack and check a token
* Clone this repository and make below settings file.

```bash
$ touch settings.yml
$ vi settings.yml
API_TOKEN : "YOUR TOKEN FOR BOTS"
$ pip install -r requirements.txt
```

## Execute

```bash
$ python mybot/run.py
```

## Questions you can ask to the bot

### hi

### rates

* USD/JPY
* CAD/JPY
* JPY/USD
* JPY/CAD
