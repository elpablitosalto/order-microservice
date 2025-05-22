# Testing Guide for Order Processing Microservice

## 1. Unit Tests

1. Run unit tests:
```bash
pytest tests/unit/
```

2. Run tests with coverage report:
```bash
pytest --cov=app tests/unit/
```

## 2. Integration Tests

1. Run integration tests:
```bash
pytest tests/integration/
```

2. Run all tests with coverage:
```bash
pytest --cov=app tests/
```

## 3. API Tests

1. Start the service:
```bash
docker compose up -d
```

2. Run API tests:
```bash
pytest tests/api/
```

## 4. Performance Tests

1. Install locust:
```bash
pip install locust
```

2. Run performance tests:
```bash
locust -f tests/performance/locustfile.py
```

3. Open http://localhost:8089 in your browser

## 5. Test Reports

1. Generate HTML coverage report:
```bash
pytest --cov=app --cov-report=html tests/
```

2. Open `htmlcov/index.html` in your browser

## 6. Test Data

1. Test data is located in `tests/data/`
2. Fixtures are in `tests/fixtures/`

## 7. Test Configuration

1. Test configuration is in `pytest.ini`
2. Environment variables for tests are in `.env.test`

## 8. Continuous Integration

1. Tests are automatically run on push to main branch
2. Coverage report is generated and published
3. Performance tests are run daily

## 9. Test Maintenance

1. Keep test data up to date
2. Update tests when API changes
3. Monitor test coverage
4. Review and update performance test scenarios

## 10. Troubleshooting

1. If tests fail:
   - Check test data
   - Verify environment variables
   - Check service logs
   - Review recent changes

2. If performance tests fail:
   - Check system resources
   - Verify network connectivity
   - Review test scenarios
   - Check service configuration 