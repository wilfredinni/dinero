# Dinero

```python
from dinero import Dinero
from dinero.currencies import CLP

amount = Dinero(234342.3010, CLP)
amount.raw_amount
amount.normalized_amount
amount.symbol
amount.code
amount.exponent

formatted = amount.formatted_amount(symbol=False, currency=False)
print(amount)
```

    $234,342 CLP

## Operations

### Add

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("333.3", EUR)
total = amount.add(333.3)
print(total)
```

    €666.60 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, EUR)

total = amount_1.add(amount_2)
print(total)
```

    €666.60 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", USD)
amount_2 = Dinero(333.3, USD)

total = amount_1 + amount_2
print(total)
```

    $666.60 USD

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, EUR)
amount_3 = Dinero(333.3, EUR)

total = sum([amount_1, amount_2, amount_3])
print(total)
```

    €999.90 EUR

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

amount_1.add(amount_2)
amount_1 + amount_2
sum([amount_1, amount_2])
```

    ---------------------------------------------------------------------------

    DifferentCurrencyError                    Traceback (most recent call last)

    Cell In [37], line 8
          5 amount_1 = Dinero("333.3", EUR)
          6 amount_2 = Dinero(333.3, USD)
    ----> 8 amount_1.add(amount_2)
          9 amount_1 + amount_2
         10 sum([amount_1, amount_2])


    File ~/projects/dinero/dinero/_dinero.py:53, in Dinero.add(self, amount)
         52 def add(self, amount: "OperationType | Dinero") -> "Dinero":
    ---> 53     return self.__add__(amount)


    File ~/projects/dinero/dinero/_dinero.py:106, in Dinero.__add__(self, addend)
        105 def __add__(self, addend: "OperationType | Dinero") -> "Dinero":
    --> 106     addend_obj = self._get_instance(addend)
        107     total = self.normalized_amount + addend_obj.normalized_amount
        108     return Dinero(str(total), self.currency)


    File ~/projects/dinero/dinero/_dinero.py:101, in Dinero._get_instance(self, amount)
         98     second_amount = Dinero(str(amount), self.currency)
        100 if second_amount.code != self.code:
    --> 101     raise DifferentCurrencyError("Currencies can not be different")
        103 return second_amount


    DifferentCurrencyError: Currencies can not be different

### Subtract

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20.20", EUR)
total = amount.subtract('10.20')
print(total)
```

    €10.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.20", EUR)
amount_2 = Dinero("10.20", EUR)
total = amount_1.subtract(amount_2)
print(total)
```

    €10.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("20.20", EUR)
amount_2 = Dinero("10.20", EUR)
total = amount_1 - amount_2
print(total)
```

    €10.00 EUR

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

amount_1.subtract(amount_2)
amount_1 - amount_2
```

    ---------------------------------------------------------------------------

    DifferentCurrencyError                    Traceback (most recent call last)

    Cell In [32], line 8
          5 amount_1 = Dinero("333.3", EUR)
          6 amount_2 = Dinero(333.3, USD)
    ----> 8 amount_1.subtract(amount_2)
          9 amount_1 - amount_2


    File ~/projects/dinero/dinero/_dinero.py:56, in Dinero.subtract(self, amount)
         55 def subtract(self, amount: "OperationType | Dinero") -> "Dinero":
    ---> 56     return self.__sub__(amount)


    File ~/projects/dinero/dinero/_dinero.py:114, in Dinero.__sub__(self, subtrahend)
        113 def __sub__(self, subtrahend: "OperationType | Dinero") -> "Dinero":
    --> 114     subtrahend_obj = self._get_instance(subtrahend)
        115     total = self.normalized_amount - subtrahend_obj.normalized_amount
        116     return Dinero(str(total), self.currency)


    File ~/projects/dinero/dinero/_dinero.py:101, in Dinero._get_instance(self, amount)
         98     second_amount = Dinero(str(amount), self.currency)
        100 if second_amount.code != self.code:
    --> 101     raise DifferentCurrencyError("Currencies can not be different")
        103 return second_amount


    DifferentCurrencyError: Currencies can not be different

### Multiply

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount.multiply(2)
print(total)
```

    €40.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1.multiply(amount_2)
print(total)
```

    €40.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR, CLP

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1 * amount_2
print(total)
```

    €40.00 EUR

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("20.00", USD)
total = amount * 2.9
print(total)
```

    $58.00 USD

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("333.3", EUR)
amount_2 = Dinero(333.3, USD)

amount_1.multiply(amount_2)
amount_1 * amount_2
```

    ---------------------------------------------------------------------------

    DifferentCurrencyError                    Traceback (most recent call last)

    Cell In [28], line 8
          5 amount_1 = Dinero("333.3", EUR)
          6 amount_2 = Dinero(333.3, USD)
    ----> 8 amount_1.multiply(amount_2)
          9 amount_1 * amount_2


    File ~/projects/dinero/dinero/_dinero.py:59, in Dinero.multiply(self, amount)
         58 def multiply(self, amount: "OperationType | Dinero") -> "Dinero":
    ---> 59     return self.__mul__(amount)


    File ~/projects/dinero/dinero/_dinero.py:119, in Dinero.__mul__(self, multiplicand)
        118 def __mul__(self, multiplicand: "OperationType | Dinero") -> "Dinero":
    --> 119     multiplicand_obj = self._get_instance(multiplicand)
        120     total = self.normalized_amount * multiplicand_obj.normalized_amount
        121     return Dinero(str(total), self.currency)


    File ~/projects/dinero/dinero/_dinero.py:101, in Dinero._get_instance(self, amount)
         98     second_amount = Dinero(str(amount), self.currency)
        100 if second_amount.code != self.code:
    --> 101     raise DifferentCurrencyError("Currencies can not be different")
        103 return second_amount


    DifferentCurrencyError: Currencies can not be different

### Divide

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount.divide(2)
print(total)
```

    €10.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1.divide(amount_2)
print(total)
```

    €10.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("20.00", EUR)
amount_2 = Dinero("2.0", EUR)
total = amount_1 / amount_2
print(total)
```

    €10.00 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount = Dinero("20", EUR)
total = amount / 2
print(total)
```

    €10.00 EUR

```python
# different currencies will raise a DifferentCurrencyError
from dinero import Dinero
from dinero.currencies import EUR, USD

amount_1 = Dinero("20", EUR)
amount_2 = Dinero(2, USD)

amount_1.divide(amount_2)
amount_1 / amount_2
```

    ---------------------------------------------------------------------------

    DifferentCurrencyError                    Traceback (most recent call last)

    Cell In [19], line 8
          5 amount_1 = Dinero("20", EUR)
          6 amount_2 = Dinero(2, USD)
    ----> 8 amount_1.divide(amount_2)
          9 amount_1 / amount_2


    File ~/projects/dinero/dinero/_dinero.py:62, in Dinero.divide(self, amount)
         61 def divide(self, amount: "OperationType | Dinero") -> "Dinero":
    ---> 62     return self.__truediv__(amount)


    File ~/projects/dinero/dinero/_dinero.py:124, in Dinero.__truediv__(self, divisor)
        123 def __truediv__(self, divisor: "OperationType | Dinero") -> "Dinero":
    --> 124     divisor_obj = self._get_instance(divisor)
        125     total = self.normalized_amount / divisor_obj.normalized_amount
        126     return Dinero(str(total), self.currency)


    File ~/projects/dinero/dinero/_dinero.py:101, in Dinero._get_instance(self, amount)
         98     second_amount = Dinero(str(amount), self.currency)
        100 if second_amount.code != self.code:
    --> 101     raise DifferentCurrencyError("Currencies can not be different")
        103 return second_amount


    DifferentCurrencyError: Currencies can not be different

### Operations

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.2", EUR)
amount_2 = Dinero(333.3, EUR)
amount_3 = Dinero(333.4, EUR)

highest = max([amount_1, amount_2, amount_3])
lowest = min([amount_1, amount_2, amount_3])

print(highest)
print(lowest)
```

    €333.40 EUR
    €333.20 EUR

```python
from dinero import Dinero
from dinero.currencies import EUR

amount_1 = Dinero("333.2", EUR)
amount_2 = Dinero(333.3, EUR)

# less than
amount_1.less_than(amount_2)
amount_1.less_than(333.3)
amount_1 < amount_2
amount_1 < 333.3

# less than or equal
amount_1.less_than_or_equal(amount_2)
amount_1.less_than_or_equal(333.3)
amount_1 <= amount_2
amount_1 <= 333.3

# greater than
amount_1.greater_than(amount_2)
amount_1.greater_than(333.3)
amount_1 < amount_2
amount_1 < 333.3

# greater than or equal
amount_1.greater_than_or_equal(amount_2)
amount_1.greater_than_or_equal(333.3)
amount_1 > amount_2
amount_1 > 333.3

# equals
amount_3 = Dinero(333.2, EUR)
amount_1.equals_to(amount_3)
amount_1.equals_to(333.2)
amount_1 == amount_3
amount_1 == 333.2
```

    True

## to_dict

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.259", USD)
amount.to_dict(amount_with_format=False)
```

    {'amount': '3333.26',
     'currency': {'code': 'USD', 'base': 10, 'exponent': 2, 'symbol': '$'}}

## to_json

```python
from dinero import Dinero
from dinero.currencies import USD

amount = Dinero("3333.2", USD)
amount.to_json(amount_with_format=False)
```

    '{"amount": "3333.20", "currency": {"code": "USD", "base": 10, "exponent": 2, "symbol": "$"}}'
