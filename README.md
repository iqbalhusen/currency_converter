# currency_converter
Converts currency using Yahoo Finance API, supports historical date.
<br>
###Usage
```
>>> from currency_converter import convert
>>> convert('USD', 'INR', amount=45233, date='20140506')
2718955.63
>>>
```
**Valid Arguments**

 - **from_curr**
*Type*: String. Valid currency acronym.
 - **to_curr**
*Optional*. *Type*: String. Valid currency acronym. *default:* `USD`.
 - **amount**
*Optional*. *Type*: Float. *default:* `1.0`.
 - **date**
*Optional*. *Type*: String. *Format:* `YYYYMMDD`.*default:* `None`.
<br>

###Reference

 - https://github.com/brianriley/python-currency
 - https://gist.github.com/yml/940298