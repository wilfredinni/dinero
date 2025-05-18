Create a new currency conversion tool for the Dinero Python library that:

1. Implements a `convert()` method for Dinero objects with the following signature:
   ```python
   def convert(self, exchange_rate: str | float, currency: Currency) -> Dinero
   ```

2. Enables conversion of Dinero objects to different currencies using:
   - A specified exchange rate
   - Target currency specification
   - Built-in currency objects (e.g., USD, CLP)

3. Requirements:
   - Accept both string and float inputs for exchange rates
   - Validate exchange rates (must be positive non-zero numbers)
   - Verify currency objects are valid
   - Perform accurate mathematical calculations maintaining precision
   - Return a new Dinero object in the target currency

4. Error Handling:
   - Raise ValueError for invalid exchange rates (negative, zero, non-numeric)
   - Raise TypeError for invalid currency objects
   - Include descriptive error messages

Example Usage:
```python
from dinero import Dinero
from dinero.currencies import USD, CLP

# Convert USD to CLP
usd_amount = Dinero(amount="100", currency=USD)
clp_amount = usd_amount.convert(exchange_rate="750", currency=CLP)
# Returns: Dinero(75000, CLP)
```
5. Testing:
   - Write unit tests for the `convert()` method
   - Test with various exchange rates and currency combinations
   - Ensure edge cases are covered (e.g., zero, negative rates)
   - Validate that the returned Dinero object has the correct amount and currency