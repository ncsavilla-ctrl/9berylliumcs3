# Computational Thinking Exercise
## [Smart School Canteen Queue OR Smart Vending Machine]
**Name:** Niña Celestine T. Savilla
**Section:** Beryllium
**Last Name:** Savilla
**Date:** August 20, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The school canteen’s lunch service is slow and inefficient because students take too long to decide, the cashier manually calculates payments and change, and there is no system for monitoring food stock.
---
## Step 2: Identify the Sub-Problems
1. Students take too long to decide what to order.
2. The cashier manually calculates the total cost and change.
3. There is no system to track which food items are running out.
4. Students have to wait in one long line.
---
## Step 3: Apply Computational Thinking Skills

| Students take too long to decide what to order. | Pattern Recognition | Divide menus into categories and remove unnecessary food that people don't buy |

| The cashier manually calculates the total cost and change. | Algorithm Design | Create a program that adds and automatically calcualates the total |

| There is no system to track which food items are running out. | Pattern Recognition/Abstraction | 
Create an inventory system that monitors the stocks |

| Students have to wait in one long line. | Decomposition | Divide the line into 3 and let different staffs handle each line |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
The cashier manually calculates the total cost and change.
### Pseudocode
START

Display menu and prices

Ask student to select food items
Store selected items

Set total = 0

FOR each selected item
    total = total + price of item
END FOR

Display total amount

Ask student to enter payment

IF payment >= total THEN
    change = payment - total
    Display "Order confirmed"
    Display change
ELSE
    Display "Insufficient payment"
END IF

END

---
