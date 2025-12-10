# SOLID Principles - Quick Reference Guide

![SOLID Principles](https://img.youtube.com/vi/5999cgzA95A/maxresdefault.jpg)

**Video Reference:** [SOLID Principles Explained](https://www.youtube.com/watch?v=5999cgzA95A)

---

## Overview

SOLID is an acronym for five object-oriented design principles introduced by Robert C. Martin (Uncle Bob). These principles help create maintainable, scalable, and flexible software.

---

## 🔷 **S - Single Responsibility Principle (SRP)**

**Definition:** A class should have only one reason to change - one responsibility.

**Key Idea:** Each class should focus on doing one thing well.

### ❌ Bad Example
```python
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def save_to_database(self):
        # Database logic here
        print(f"Saving {self.name} to database")
```

### ✅ Good Example
```python
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class UserRepository:
    def save(self, user):
        print(f"Saving {user.get_name()} to database")
```

---

## 🔷 **O - Open/Closed Principle (OCP)**

**Definition:** Classes should be open for extension but closed for modification.

**Key Idea:** Add new functionality without changing existing code.

### ❌ Bad Example
```python
class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit":
            # Process credit card
            pass
        elif payment_type == "paypal":
            # Process PayPal
            pass
```

### ✅ Good Example
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self):
        print("Processing credit card payment")

class PayPalProcessor(PaymentProcessor):
    def process(self):
        print("Processing PayPal payment")
```

---

## 🔷 **L - Liskov Substitution Principle (LSP)**

**Definition:** Objects of a superclass should be replaceable with objects of subclasses without breaking the application.

**Key Idea:** Subclasses must behave like their parent classes.

### ❌ Bad Example
```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
```

### ✅ Good Example
```python
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return "Flying"

class Penguin(Bird):
    def move(self):
        return "Swimming"
```

---

## 🔷 **I - Interface Segregation Principle (ISP)**

**Definition:** Clients should not be forced to depend on interfaces they don't use.

**Key Idea:** Create specific interfaces instead of one general-purpose interface.

### ❌ Bad Example
```python
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Working")
    
    def eat(self):
        # Robots don't eat!
        raise Exception("Robots don't eat")
```

### ✅ Good Example
```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working")
    
    def eat(self):
        print("Eating")

class Robot(Workable):
    def work(self):
        print("Working")
```

---

## 🔷 **D - Dependency Inversion Principle (DIP)**

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Key Idea:** Depend on interfaces, not concrete implementations.

### ❌ Bad Example
```python
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling!
```

### ✅ Good Example
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class PostgresDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL")

class UserService:
    def __init__(self, database: Database):
        self.db = database  # Loose coupling!
```

---

## 📌 Benefits of SOLID Principles

- **Maintainability:** Easier to understand and modify code
- **Scalability:** Simple to add new features
- **Testability:** Components can be tested independently
- **Flexibility:** Easy to swap implementations
- **Reduced Coupling:** Less dependencies between classes

---

## 🎯 Quick Memory Aid

- **S** - One class, one job
- **O** - Extend, don't modify
- **L** - Subtypes must be substitutable
- **I** - Small, specific interfaces
- **D** - Depend on abstractions

---
