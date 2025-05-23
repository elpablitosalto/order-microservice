# Testing Guide

This document provides instructions for running and writing tests for the Order Processing Microservice.

## Running Tests

### Running All Tests
To run all tests, use the following command:
```bash
pytest tests/
```

### Running Specific Test Categories
- To run only unit tests:
```bash
pytest tests/unit/
```

- To run only API tests:
```bash
pytest tests/api/
```

- To run a specific test:
```bash
pytest tests/unit/test_models.py::test_order_creation
```

## Test Structure

The test suite is organized into the following directories:
- `tests/unit/` - Unit tests for models and business logic
- `tests/api/` - API endpoint tests
- `tests/conftest.py` - Test fixtures and configuration

## Test Database

The tests use SQLite as the test database. A fresh database is created and destroyed for each test, ensuring:
- Test isolation
- Clean test environment
- No interference between tests

## Adding New Tests

You can add new tests in the appropriate test files. Here are some examples of tests you might want to add:

### Data Validation Tests
- Input validation
- Data type checking
- Required field validation
- Business rule validation

### Error Handling Tests
- Invalid input handling
- Database error handling
- External service error handling
- Authentication/Authorization error handling

### Business Logic Tests
- Order processing logic
- Payment processing
- Inventory management
- Status transitions

### Integration Tests
- Service-to-service communication
- External API integration
- Message queue integration
- Database integration

## Test Fixtures

The `conftest.py` file contains reusable test fixtures:
- Database session management
- Test client setup
- Common test data

## Best Practices

1. Keep tests focused and atomic
2. Use descriptive test names
3. Follow the Arrange-Act-Assert pattern
4. Clean up resources after tests
5. Use appropriate assertions
6. Mock external dependencies
7. Write tests before implementing features (TDD)

## Need Help?

If you need assistance with:
- Writing specific tests
- Understanding test patterns
- Debugging test failures
- Adding new test categories

Please reach out to the development team for guidance. 