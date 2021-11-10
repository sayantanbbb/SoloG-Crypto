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

```d_log``` :- ```np.log(d)```

```lower_shadow``` :- ```np.minimum(df['Close'], df['Open']) - df['Low']```

```upper_shadow``` :- ```df['High'] - np.maximum(df['Close'], df['Open'])```

```lower_shadow_log``` :- ```np.log(lower_shadow)```

```upper_shadow_log``` :- ```np.log(upper_shadow)```

```df_feat["high_div_low"] = df_feat["High"] / df_feat["Low"]```



```python
def log_return(series, periods=1):
    return np.log(series).diff(periods=periods)
```

``` five_min_log_return = log_return(df.VWAP, periods=5) ```

``` abs_one_min_log_return = log_return(df.VWAP,periods=1).abs()   ```

```df['trade']``` :- ```df['Close']-df['Open']```

```df['gtrade']``` :- ```df['trade']/df['Count']```

```shadow1``` :- ```trade/Volume```

```shadow2``` :- ```upper_shadow/low```

```shadow3``` :- ```upper_shadow/Volume```

```shadow4``` :- ```lower_shadow/high```

```shadow5``` :- ```lower_shadow/Volume```

```shadow_diff1``` :- ```upper_shadow-lower_shadow```

```shadow_diff2``` :- ```shadow_diff1/count```

```shadow_diff3``` :- ```shadow_diff2/Volume```



