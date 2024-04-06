# Day_023

Day_023 of the #100daysofalxse 
#DoingHardThings

I continued to look into Unittest, unittest.mock and integration tests
Today, I included an exercise to to orchestrate usage


## Overview
### Unit Tests
Unit testing involves testing individual units or components of the codebase in isolation. These tests verify that functions return expected outputs for given inputs. It's crucial to test both standard inputs and corner cases to ensure robustness. Additionally, unit tests should focus solely on the logic encapsulated within the function being tested. External dependencies should be mocked, especially for operations like network or database calls.

Goal: To verify if the function behaves correctly under different scenarios, assuming external dependencies function as expected.

### Integration Tests
Integration tests examine the interaction between different parts of the codebase to validate end-to-end functionality. Unlike unit tests, integration tests typically don't mock low-level functions that interact with external resources such as HTTP requests, file I/O, or database operations.

Goal: To ensure seamless interaction between various components of the system and validate the overall behavior of the application.

## Resources covered
1. [Unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)
2. [Unittest Mock](https://docs.python.org/3/library/unittest.mock.html)
3. [Video] https://www.youtube.com/watch?v=WFRljVPHrkE&ab_channel=redshiftzero