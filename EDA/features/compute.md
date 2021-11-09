Info:-

```
timestamp - A timestamp for the minute covered by the row.
Asset_ID - An ID code for the cryptoasset.
Count - The number of trades that took place this minute.
Open - The USD price at the beginning of the minute.
High - The highest USD price during the minute.
Low - The lowest USD price during the minute.
Close - The USD price at the end of the minute.
Volume - The number of cryptoasset units traded during the minute.
VWAP - The volume weighted average price for the minute.
Target - 15 minute residualized returns. See the 'Prediction and Evaluation' section of this notebook for details of how the target is calculated.
```

New stuff :- 

```dy``` :- ``` df['high']-df['low']```

```d``` :- ``` dy/df['Count']```

```lower_shadow``` :- ```np.minimum(df['Close'], df['Open']) - df['Low']```

```upper_shadow``` :- ```df['High'] - np.maximum(df['Close'], df['Open'])```

```python
def log_return(series, periods=1):
    return np.log(series).diff(periods=periods)
```

``` five_min_log_return = log_return(df.VWAP, periods=5) ```

``` abs_one_min_log_return = log_return(df.VWAP,periods=1).abs()   ```

```df['trade']``` :- ```df['Close']-df['Open']```

```df['gtrade']``` :- ```df['trade']/df['Count']```


