# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation means combining the product information, such as productName and stockQuantity, with the methods that manage them inside a Product class. Instead of allowing these values to be changed directly from anywhre in the program, they can be protected and modified only through specific methods like updateStock() or setPrice(). This helps prevent mistakes such as entering a negative price or accidentally making the available stock less than zero.

### 2. Abstraction

Abstraction allows the program to hide complicated operations and provide the useer with simple ways to perform tasks. For exampple, a method called addNewProduct() could allow the user to enter a product name, price, and starting stock without needing to know how the system saves and organizes the info. The complicated steps are handled by the rogram in the background. This makes the system simpler for usesrs and easier for programmers to manage.

### 3. Inheritance

Inheritance can be useful when the store sells different categorues of products that have common information. For example, a general Product class could be used as the parent class, while Snack, Drink, and SchoolSuppy classes could inherit its basic properties such as name, price, and stock. Each child class can then have additional information, such as the flavor of a snack or the size of a drink. This allows us to reuse existing code instead of creating everything from the beginning.

### 4. Polymorphism

Polymorphism allows different types of products to perform a similar action in their own way. For example, the system could have a displayDetials() method that is used by Snack, Drink, and SchoolSupply objects. A snack could display its flavor, a dirnk could display its volume, and a school supply could display its brand or type. Using the same method for different objects ,akes the programe easier to expand and organize.

## Reflection

Among the four pillars, I think abstraction would be the most useful for a sari-sari store inventory system. Store owners and cashiers should be able to perform tasks without having to understand the complicated processes happening insied the program.This would make the system easier to use, especially. for someone who does not have much programming or technical knowledge.