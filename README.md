# Corona-RPi-Display
A simple script to keep an eye on the total number of cases and deaths of COVID-19
in **Poland**, also RPi's temperature to fill a blank line on the display.

## Datasource
Data are fetching from
[Gov](https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2)
and Twitter [@MZ_GOV_PL](https://twitter.com/MZ_GOV_PL).

## Usage
### Requirements
You need to install required packages.
```shell script
$ pip3 install -r requirements.txt
```

### Terminal
Print results in the console.
```shell script
$ python3 print.py 
```

### LCD 2x16
Before you run, you must choose pins used to LCD connection in `/lcd_2x16.py`,
according to the [GPIO/BCM](https://pinout.xyz/).
```shell script
$ python3 lcd_2x16
```
