# Pytest Comprehensive Notes

## 1. Pytest Basics

### What is Pytest?

Pytest is a mature, feature-rich testing framework for Python that makes it easy to write simple and scalable test cases. It's the most popular testing framework in the Python ecosystem due to its simplicity and powerful features.

### Installation

```bash
pip install pytest
```

### Writing Your First Test

Pytest automatically discovers test files and functions that follow these naming conventions:
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`

**Example:**

```python
# test_sample.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

### Running Tests

```bash
# Run all tests in current directory
pytest

# Run a specific test file
pytest test_sample.py

# Run a specific test function
pytest test_sample.py::test_add

# Run with verbose output
pytest -v

# Run with output capture disabled (see print statements)
pytest -s
```

### Assertions

Pytest uses Python's built-in `assert` statement with detailed introspection:

```python
def test_assertions():
    # Basic assertions
    assert 1 == 1
    assert "hello" in "hello world"
    assert [1, 2, 3] == [1, 2, 3]
    
    # Assertions with messages
    assert 5 > 3, "5 should be greater than 3"
    
    # Testing exceptions
    import pytest
    with pytest.raises(ValueError):
        int("not a number")
    
    # Testing exception messages
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")
```

### Test Organization

```python
# Grouping tests in classes
class TestMathOperations:
    def test_addition(self):
        assert 2 + 2 == 4
    
    def test_subtraction(self):
        assert 5 - 3 == 2
```

### Markers

Markers allow you to set metadata on test functions:

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    # A test that takes long time
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_modern_feature():
    pass

@pytest.mark.xfail
def test_known_failure():
    assert False  # Expected to fail
```

Run specific markers:
```bash
pytest -m slow  # Run only tests marked as slow
pytest -m "not slow"  # Run all tests except slow ones
```

---

## 2. What are Fixtures?

### Overview

Fixtures are functions that run before (and sometimes after) test functions. They're used to set up preconditions for tests, such as database connections, test data, or configuration. Fixtures promote code reuse and make tests more maintainable.

### Basic Fixture Example

```python
import pytest

@pytest.fixture
def sample_data():
    """Provides sample data for tests"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_length(sample_data):
    assert len(sample_data) == 5
```

### Fixture with Setup and Teardown

```python
@pytest.fixture
def database_connection():
    # Setup: runs before test
    db = connect_to_database()
    print("Database connected")
    
    yield db  # Provide the fixture value
    
    # Teardown: runs after test
    db.close()
    print("Database closed")

def test_query(database_connection):
    result = database_connection.query("SELECT * FROM users")
    assert len(result) > 0
```

### Fixture Advantages

- **Reusability**: Write setup code once, use in multiple tests
- **Modularity**: Keep test setup separate from test logic
- **Scalability**: Easy to maintain and modify
- **Dependency Injection**: Pytest automatically passes fixtures to tests
- **Cleanup**: Automatic teardown with yield syntax

---

## 3. Parameterized Fixtures

### Using `@pytest.fixture` with `params`

Parameterized fixtures allow you to run the same test with different fixture values:

```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_square(number):
    # This test will run 3 times with values 1, 2, and 3
    result = number ** 2
    assert result == number * number
```

### Multiple Parameters

```python
@pytest.fixture(params=[
    (1, 2, 3),
    (0, 0, 0),
    (-1, -2, -3),
    (10, 20, 30)
])
def coordinates(request):
    return request.param

def test_coordinates(coordinates):
    x, y, z = coordinates
    assert isinstance(x, int)
    assert isinstance(y, int)
    assert isinstance(z, int)
```

### Parameterizing Tests Directly

You can also parameterize test functions directly:

```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
])
def test_square_direct(input, expected):
    assert input ** 2 == expected

# Multiple parameters
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -5, 5),
])
def test_addition(a, b, expected):
    assert a + b == expected

# Combining multiple parametrize decorators
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_combinations(x, y):
    # This creates 4 test combinations: (1,3), (1,4), (2,3), (2,4)
    assert x + y > 0
```

### IDs for Parameterized Tests

```python
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
], ids=["addition1", "addition2", "multiplication"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

---

## 4. Different Types of Fixtures

### Function Scope (Default)

Runs once per test function:

```python
@pytest.fixture(scope="function")  # or just @pytest.fixture
def function_fixture():
    print("Setup for function")
    yield
    print("Teardown for function")
```

### Class Scope

Runs once per test class:

```python
@pytest.fixture(scope="class")
def class_fixture():
    print("Setup for class")
    db = initialize_database()
    yield db
    print("Teardown for class")

class TestDatabase:
    def test_insert(self, class_fixture):
        # Uses same fixture instance
        pass
    
    def test_query(self, class_fixture):
        # Uses same fixture instance
        pass
```

### Module Scope

Runs once per module (file):

```python
@pytest.fixture(scope="module")
def module_fixture():
    print("Setup once for entire module")
    expensive_resource = create_expensive_resource()
    yield expensive_resource
    print("Teardown once for entire module")
```

### Session Scope

Runs once per entire test session:

```python
@pytest.fixture(scope="session")
def session_fixture():
    print("Setup once for all tests")
    config = load_global_config()
    yield config
    print("Teardown after all tests complete")
```

### Autouse Fixtures

Automatically used by all tests without explicit request:

```python
@pytest.fixture(autouse=True)
def setup_teardown():
    print("Before each test")
    yield
    print("After each test")

def test_one():
    assert True  # setup_teardown runs automatically

def test_two():
    assert True  # setup_teardown runs automatically
```

### Built-in Fixtures

Pytest provides several built-in fixtures:

```python
# tmp_path: provides temporary directory (Path object)
def test_tmp_path(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("content")
    assert file.read_text() == "content"

# monkeypatch: modify objects, dictionaries, environment variables
def test_monkeypatch(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_key")
    import os
    assert os.getenv("API_KEY") == "test_key"

# capsys: capture stdout/stderr
def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"

# request: provides information about the requesting test
@pytest.fixture
def custom_fixture(request):
    print(f"Test name: {request.node.name}")
    yield
```

### Fixture Dependencies

Fixtures can depend on other fixtures:

```python
@pytest.fixture
def database():
    db = connect_to_db()
    yield db
    db.close()

@pytest.fixture
def user(database):
    # This fixture depends on database fixture
    user = database.create_user("testuser")
    yield user
    database.delete_user(user.id)

def test_user_login(user):
    # Both database and user fixtures are set up
    assert user.name == "testuser"
```

### Conftest.py

Fixtures can be shared across multiple test files using `conftest.py`:

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def shared_resource():
    """Available to all tests in this directory and subdirectories"""
    return {"api_key": "123456"}

# test_module1.py
def test_one(shared_resource):
    assert shared_resource["api_key"] == "123456"

# test_module2.py
def test_two(shared_resource):
    assert "api_key" in shared_resource
```

### Dynamic Fixtures

```python
@pytest.fixture
def user_factory():
    """Factory fixture that creates users on demand"""
    created_users = []
    
    def _create_user(name, email):
        user = User(name, email)
        created_users.append(user)
        return user
    
    yield _create_user
    
    # Cleanup all created users
    for user in created_users:
        user.delete()

def test_multiple_users(user_factory):
    user1 = user_factory("Alice", "alice@example.com")
    user2 = user_factory("Bob", "bob@example.com")
    assert user1.name == "Alice"
    assert user2.name == "Bob"
```

---

## Best Practices

1. **Keep fixtures simple and focused** - Each fixture should do one thing well
2. **Use appropriate scope** - Choose the narrowest scope that meets your needs
3. **Document fixtures** - Add docstrings explaining what the fixture provides
4. **Avoid fixture overuse** - Don't create fixtures for simple values that can be defined inline
5. **Use conftest.py wisely** - Share common fixtures but avoid making it too large
6. **Name fixtures clearly** - Use descriptive names that indicate what they provide
7. **Prefer composition** - Build complex fixtures from simpler ones
8. **Clean up resources** - Always use yield for fixtures that need cleanup

## Common Pytest Commands

```bash
# Run with coverage report
pytest --cov=myapp tests/

# Run in parallel (requires pytest-xdist)
pytest -n auto

# Stop at first failure
pytest -x

# Show local variables in tracebacks
pytest -l

# Run last failed tests
pytest --lf

# Run tests that failed and then all
pytest --ff

# Generate HTML report (requires pytest-html)
pytest --html=report.html

# Run with specific log level
pytest --log-cli-level=INFO
```

---

## Conclusion

Pytest is a powerful and flexible testing framework that makes writing and maintaining tests straightforward. By understanding fixtures and their various scopes and types, you can create efficient, reusable, and maintainable test suites for your Python projects.