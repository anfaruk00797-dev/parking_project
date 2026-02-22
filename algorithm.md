Algorithm: Parking Fee Calculation

1. รับจำนวนชั่วโมงที่จอด (hours)
2. ถ้า hours <= 0
      แสดง error
3. ถ้า hours <= 2
      ค่าจอด = 0
4. ถ้า hours > 2 และ <= 5
      ค่าจอด = (hours - 2) * 20
5. ถ้า hours > 5
      ค่าจอด = (3 * 20) + (hours - 5) * 50
6. แสดงค่าจอด