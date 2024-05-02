# Day_050

- #100daysofalxse 
- #DoingHardThings
- #DailyGrowth

This is a great milestone
Half way into the challenge

Today I built and exercise on unittest in JS. This follows yesterday's efforts of reading and familiarizing with various libraries of unit tests in JavaScript such as  Mocha, Chai, and Sinon. 

I read and went through the following:

- How to use Mocha to write a test suite
- How to use different assertion libraries (Node or Chai)
- How to present long test suites
- When and how to use spies
- When and how to use stubs
- What are hooks and when to use them
- Unit testing with Async functions
- How to write integration tests with a small node server

## Tasks
### Basic test with Mocha and Node assertion library
Install Mocha using npm.
Set up scripts in package.json to run Mocha tests.
Implement a basic function calculateNumber and its test suite using Node's assert library.


### Combining descriptions
- Upgrade the calculateNumber function to handle different types of operations (SUM, SUBTRACT, DIVIDE).
- Rewrite the test suite using assert.
- Organize test cases using describe.


### Basic test using Chai assertion library
- Install Chai using npm.
- Rewrite the previous task's code using Chai's expect syntax for assertions.


### Spies
- Install Sinon using npm.
- Create spies to test function calls and behavior.
- Ensure proper usage of spies within test suites.


### Stubs
- Use Sinon to create stubs for function calls.
- Stub expensive or external functions to control test behavior.
- Verify correct usage and restoration of stubs.


### Hooks
- Utilize Mocha's hooks (beforeEach, afterEach) to perform pre-test and post-test actions.
- Ensure proper setup and teardown of resources for each test.