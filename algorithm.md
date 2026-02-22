Algorithm: Parking Fee Calculation

Input: Number of hours parked (hours)

1. If hours < 0
      Return "Invalid input"

2. If hours <= 2
      Fee = 0

3. If hours > 2 and hours <= 5
      Fee = (hours - 2) * 20

4. If hours > 5
      Fee = (3 * 20) + (hours - 5) * 50

5. Return Fee