# Design Patterns - Complete Guide

## Video Reference
📺 **YouTube Playlist**: [Design Patterns Tutorial](https://www.youtube.com/watch?v=USLwIwyWVIM&list=PLJq-63ZRPdBtLBbzA2fIG9mOPclbPDSxq)


---

## Table of Contents
1. [Singleton Pattern](#1-singleton-pattern)
2. [Factory Pattern](#2-factory-pattern)
3. [Builder Pattern](#3-builder-pattern)
4. [Strategy Pattern](#4-strategy-pattern)
5. [Decorator Pattern](#5-decorator-pattern)
6. [Composite Pattern](#6-composite-pattern)
7. [Visitor Pattern](#7-visitor-pattern)
8. [Adapter Pattern](#8-adapter-pattern)

---

## 1. Singleton Pattern

### Theory
The Singleton pattern is a **creational design pattern** that ensures a class has only one instance throughout the application lifecycle and provides a global point of access to that instance. It restricts instantiation of a class to a single object and lazily initializes it on first use.

**Key Characteristics:**
- Only one instance exists
- Global access point
- Lazy or eager initialization
- Thread-safe implementation (in multi-threaded environments)

**How it Works:**
- Make the constructor private to prevent direct instantiation
- Create a static method that returns the single instance
- Store the instance in a static variable

### Real-Time Usage Examples

**1. Database Connection Pool**
- Most applications need only one connection pool manager
- Multiple connections, but single manager instance
- Example: Django's database connection handler

**2. Configuration Manager**
- Application settings loaded once and shared globally
- Example: Reading `config.json` or environment variables

**3. Logging Service**
- Single log file handler across the application
- Example: Python's `logging` module uses singleton for root logger

**4. Cache Manager**
- Redis or Memcached client instances
- Single connection manager for the entire application

**5. Device Drivers**
- Hardware access (printer, scanner) requires single controller
- Prevents conflicts from multiple access points

### Practice Code

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            self.connected = True
            print("Database connected")
    
    def query(self, sql):
        return f"Executing: {sql}"

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
db1.connect()
print(db2.query("SELECT * FROM users"))
```

---

## 2. Factory Pattern

### Theory
The Factory pattern is a **creational design pattern** that provides an interface for creating objects without specifying their exact classes. It delegates the instantiation logic to subclasses or a factory method, promoting loose coupling between the creator and the concrete products.

**Key Characteristics:**
- Encapsulates object creation
- Returns objects through a common interface
- Decides which class to instantiate at runtime
- Promotes loose coupling

**Types:**
- **Simple Factory**: Single factory class with creation logic
- **Factory Method**: Subclasses decide which class to instantiate
- **Abstract Factory**: Factory of factories for related object families

### Real-Time Usage Examples

**1. Database Connectors**
- Based on config, create MySQL, PostgreSQL, or MongoDB connection
- Example: SQLAlchemy's engine creation

**2. Document Generators**
- Create PDF, Word, or Excel documents based on user choice
- Example: Report generation systems

**3. UI Components**
- Create Windows, Mac, or Linux UI elements
- Example: Cross-platform GUI frameworks (Qt, Tkinter themes)

**4. Payment Gateway Integration**
- Create PayPal, Stripe, or Razorpay payment handlers
- Example: E-commerce checkout systems

**5. Notification Systems**
- Create Email, SMS, or Push notification senders
- Example: Alert/notification services

**6. Logging Handlers**
- Create File, Console, or Remote logging handlers
- Example: Python logging library

### Practice Code

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    elif animal_type == "bird":
        return Bird()

# Test
animal = animal_factory("cat")
print(animal.speak())  # Meow!
```

---

## 3. Builder Pattern

### Theory
The Builder pattern is a **creational design pattern** that constructs complex objects step by step. It separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It's particularly useful when an object requires many parameters or has complex initialization logic.

**Key Characteristics:**
- Step-by-step object construction
- Fluent interface (method chaining)
- Separates construction from representation
- Handles complex initialization elegantly

**Components:**
- **Builder**: Interface for creating parts
- **Concrete Builder**: Implements builder interface
- **Director**: Constructs object using builder (optional)
- **Product**: The complex object being built

### Real-Time Usage Examples

**1. Query Builders**
- SQL query construction (SELECT, WHERE, JOIN, ORDER BY)
- Example: Django ORM, SQLAlchemy queries

**2. HTTP Request Builders**
- Building requests with headers, params, body, auth
- Example: `requests` library, `urllib3`

**3. Document/Report Builders**
- Creating complex documents with sections, styles, images
- Example: PDF generation libraries

**4. Configuration Objects**
- Building server configs, application settings
- Example: Spring Framework configuration

**5. UI Component Builders**
- Creating complex UI forms with validation rules
- Example: Form builders in React, Angular

**6. Email Builders**
- Constructing emails with subject, body, attachments, recipients
- Example: Email marketing platforms

### Practice Code

```python
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    
    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}GB, Storage={self.storage}GB"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def build(self):
        return self.computer

# Test
pc = ComputerBuilder().set_cpu("Intel i7").set_ram(16).set_storage(512).build()
print(pc)
```

---

## 4. Strategy Pattern

### Theory
The Strategy pattern is a **behavioral design pattern** that defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it. The pattern enables selecting an algorithm at runtime without using conditional statements.

**Key Characteristics:**
- Defines a family of algorithms
- Encapsulates each algorithm
- Makes algorithms interchangeable
- Eliminates conditional statements
- Open/Closed principle (open for extension, closed for modification)

**Components:**
- **Strategy Interface**: Common interface for all algorithms
- **Concrete Strategies**: Specific algorithm implementations
- **Context**: Uses a strategy object

### Real-Time Usage Examples

**1. Payment Processing**
- Different payment methods (Credit Card, PayPal, Cryptocurrency)
- Example: E-commerce checkout systems

**2. Sorting Algorithms**
- Choose QuickSort, MergeSort, BubbleSort based on data size
- Example: Java's `Collections.sort()` with Comparator

**3. Compression Algorithms**
- ZIP, RAR, GZIP compression strategies
- Example: File compression utilities

**4. Routing Algorithms**
- Shortest path, fastest route, scenic route
- Example: Google Maps navigation

**5. Validation Strategies**
- Email validation, phone validation, password strength
- Example: Form validation libraries

**6. Authentication Methods**
- OAuth, JWT, Session-based, API Key
- Example: Authentication systems

**7. Pricing Strategies**
- Regular pricing, discount pricing, seasonal pricing
- Example: E-commerce pricing engines

### Practice Code

```python
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class Cart:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

# Test
cart = Cart(PayPal())
print(cart.checkout(100))
```

---

## 5. Decorator Pattern

### Theory
The Decorator pattern is a **structural design pattern** that allows adding new functionality to objects dynamically without altering their structure. It provides a flexible alternative to subclassing for extending functionality. Decorators wrap the original object and add behavior before or after delegating to it.

**Key Characteristics:**
- Adds responsibilities dynamically
- Wraps original object
- Maintains same interface
- Stacks multiple decorators
- Single Responsibility Principle

**Components:**
- **Component**: Interface for objects that can be decorated
- **Concrete Component**: Object being decorated
- **Decorator**: Maintains reference to component
- **Concrete Decorators**: Add specific behaviors

### Real-Time Usage Examples

**1. Python Decorators**
- `@login_required`, `@cache`, `@timing` decorators
- Example: Flask/Django route decorators

**2. Input/Output Streams**
- BufferedReader wrapping FileReader in Java
- Example: File I/O with buffering, compression, encryption

**3. GUI Components**
- Adding scroll bars, borders, shadows to windows
- Example: Java Swing components

**4. Middleware**
- HTTP request/response processing (logging, auth, compression)
- Example: Express.js middleware, Django middleware

**5. Text Formatting**
- Bold, italic, underline text decorators
- Example: Rich text editors

**6. Coffee Shop Example**
- Base coffee + milk + sugar + whipped cream
- Each addition wraps the previous

**7. Caching Layers**
- Adding cache layer to database queries
- Example: Redis cache decorator over database calls

### Practice Code

```python
class Coffee:
    def cost(self):
        return 5
    def description(self):
        return "Coffee"

class Milk:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2
    
    def description(self):
        return self.coffee.description() + " + Milk"

class Sugar:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return self.coffee.description() + " + Sugar"

# Test
drink = Coffee()
drink = Milk(drink)
drink = Sugar(drink)
print(f"{drink.description()}: ${drink.cost()}")
```

---

## 6. Composite Pattern

### Theory
The Composite pattern is a **structural design pattern** that composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly. The pattern is particularly useful when you need to implement a tree-like structure where leaves and branches should be treated similarly.

**Key Characteristics:**
- Tree structure representation
- Uniform treatment of objects
- Recursive composition
- Part-whole hierarchy
- Single interface for both leaf and composite

**Components:**
- **Component**: Interface for all objects in composition
- **Leaf**: Individual object with no children
- **Composite**: Object that can have children
- **Client**: Manipulates objects through component interface

### Real-Time Usage Examples

**1. File System**
- Files (leaf) and Folders (composite) containing files/folders
- Example: Windows Explorer, Mac Finder

**2. Organization Hierarchy**
- Employees and Managers (managers have subordinates)
- Example: HR management systems

**3. GUI Components**
- Panel containing buttons, text fields, other panels
- Example: Java Swing, HTML DOM tree

**4. Graphics Drawing**
- Shapes and groups of shapes
- Example: Adobe Illustrator, graphic design tools

**5. Menu Systems**
- Menu items and submenus
- Example: Application menu bars

**6. Product Categories**
- Main category → subcategories → products
- Example: E-commerce category trees

**7. Document Structure**
- Document → Sections → Paragraphs → Text
- Example: Word processors, document editors

### Practice Code

```python
class Component:
    def show(self, indent=0):
        pass

class File(Component):
    def __init__(self, name):
        self.name = name
    
    def show(self, indent=0):
        print("  " * indent + f"- File: {self.name}")

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def show(self, indent=0):
        print("  " * indent + f"+ Folder: {self.name}")
        for child in self.children:
            child.show(indent + 1)

# Test
root = Folder("root")
file1 = File("file1.txt")
sub = Folder("subfolder")
file2 = File("file2.txt")

root.add(file1)
root.add(sub)
sub.add(file2)
root.show()
```

---

## 7. Visitor Pattern

### Theory
The Visitor pattern is a **behavioral design pattern** that lets you separate algorithms from the objects on which they operate. It allows adding new operations to existing object structures without modifying them. The pattern uses a technique called "double dispatch" where the operation executed depends on both the visitor type and the element type.

**Key Characteristics:**
- Separates algorithm from object structure
- Adds operations without modifying classes
- Double dispatch mechanism
- Open/Closed principle
- Useful for operations across heterogeneous collections

**Components:**
- **Visitor**: Interface declaring visit operations for each element type
- **Concrete Visitor**: Implements each operation
- **Element**: Interface with accept method
- **Concrete Elements**: Call appropriate visitor method

**When to Use:**
- Need to perform operations on objects of different types
- Object structure rarely changes but operations change frequently
- Want to avoid polluting classes with many unrelated operations

### Real-Time Usage Examples

**1. Compiler Design**
- AST (Abstract Syntax Tree) traversal for code generation, optimization
- Example: Type checking, code generation visitors

**2. Tax Calculation**
- Different tax rules for different product types
- Example: E-commerce tax calculation systems

**3. Export/Serialization**
- Export to JSON, XML, CSV from object structure
- Example: Data export tools

**4. Reporting Systems**
- Generate different reports from same data structure
- Example: Financial reporting, analytics dashboards

**5. Document Processing**
- Spell check, word count, formatting across document elements
- Example: Word processors, text editors

**6. Shopping Cart**
- Calculate total, apply discounts, check inventory for different item types
- Example: E-commerce platforms

**7. Game Engines**
- Rendering, collision detection, AI behavior on game entities
- Example: Unity, Unreal Engine entity systems

### Practice Code

```python
class Book:
    def __init__(self, price):
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_book(self)

class Fruit:
    def __init__(self, weight, price_per_kg):
        self.weight = weight
        self.price_per_kg = price_per_kg
    
    def accept(self, visitor):
        return visitor.visit_fruit(self)

class PriceCalculator:
    def visit_book(self, book):
        return book.price
    
    def visit_fruit(self, fruit):
        return fruit.weight * fruit.price_per_kg

# Test
items = [Book(20), Fruit(2, 5), Book(15)]
calc = PriceCalculator()
total = sum(item.accept(calc) for item in items)
print(f"Total: ${total}")  # 45
```

---

## 8. Adapter Pattern

### Theory
The Adapter pattern is a **structural design pattern** that allows objects with incompatible interfaces to collaborate. It acts as a bridge between two incompatible interfaces by wrapping an existing class with a new interface. This pattern is also known as the "Wrapper" pattern.

**Key Characteristics:**
- Converts one interface to another
- Makes incompatible interfaces compatible
- Wraps existing class
- Reuses existing code without modification
- Can work with class or object adapters

**Types:**
- **Class Adapter**: Uses inheritance (multiple inheritance)
- **Object Adapter**: Uses composition (preferred in Python)

**Components:**
- **Target**: Interface client expects
- **Adaptee**: Existing interface that needs adapting
- **Adapter**: Converts Adaptee interface to Target interface
- **Client**: Uses Target interface

### Real-Time Usage Examples

**1. Third-Party Library Integration**
- Wrapping external APIs to match your interface
- Example: Adapting different payment gateways to common interface

**2. Legacy Code Integration**
- Making old systems work with new code
- Example: Adapting old database drivers to new ORM

**3. Data Format Conversion**
- XML to JSON, CSV to Database
- Example: ETL (Extract, Transform, Load) processes

**4. Hardware Interfaces**
- USB to HDMI, USB-C to USB-A adapters (physical analogy)
- Example: Device driver abstraction layers

**5. Logging Systems**
- Adapting different logging libraries to standard interface
- Example: Python's logging adapter for third-party loggers

**6. Authentication Systems**
- Adapting OAuth, SAML, LDAP to common auth interface
- Example: Single Sign-On (SSO) implementations

**7. Database Adapters**
- Making different databases work through common interface
- Example: Django database backends, PDO in PHP

**8. API Versioning**
- Adapting old API versions to new versions
- Example: REST API backward compatibility layers

### Practice Code

```python
class OldPrinter:
    def print_old(self, text):
        return f"[Old] {text}"

class NewPrinter:
    def print_new(self, text):
        return f"[New] {text}"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print_new(self, text):
        return self.old_printer.print_old(text)

# Test
old = OldPrinter()
adapter = PrinterAdapter(old)
print(adapter.print_new("Hello"))  # [Old] Hello
```

---

## Pattern Categories Summary

### Creational Patterns
Focus on object creation mechanisms
- **Singleton**: One instance only
- **Factory**: Create objects without specifying exact class
- **Builder**: Construct complex objects step-by-step

### Structural Patterns
Focus on object composition and relationships
- **Decorator**: Add functionality dynamically
- **Composite**: Tree structures with uniform treatment
- **Adapter**: Make incompatible interfaces work together

### Behavioral Patterns
Focus on communication between objects
- **Strategy**: Interchangeable algorithms
- **Visitor**: Operations on object structures

---

## Quick Reference Table

| Pattern | Problem It Solves | Real-World Analogy |
|---------|-------------------|-------------------|
| Singleton | Need exactly one instance | Government president |
| Factory | Complex object creation | Car factory |
| Builder | Many construction parameters | Burger customization |
| Strategy | Multiple algorithms for same task | Navigation routes |
| Decorator | Add features dynamically | Coffee add-ons |
| Composite | Tree-like structures | File system |
| Visitor | Operations on various types | Tax inspector |
| Adapter | Incompatible interfaces | Power plug adapter |

---
