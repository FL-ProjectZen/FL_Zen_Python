# Addition

# Requirement : Perform addition of 2 numbers and print in console.

# State
x = 10
y = 20

# Behavior
result = x + y
print("Addition is : ", result)

# Requirement* / Story* / Ticket* / Task*  / Incident / Service Request

''' 
Requirement : Adding Numbers
 
Solution: Developers must translate this into systematic scenarios before coding.
          This is the core of unit testing and modern testing methodology.      

Below are the steps for end to end process: 

    Step 1: Understand the Requirement Like a Developer
    Step 2: Create Scenario Buckets (Testing Methodology)
    Step 3: Expand Each Bucket Into Scenarios
    Step 4: Convert Scenarios → Test Cases (Unit Testing Standard)
    Step 5: How Developers Derive All Scenarios (Mindset Training)
    Step 6: Why This Matters (Developer + QA Alignment)


Step 1: Understand the Requirement Like a Developer:
====================================================
        - A requirement ALWAYS has dimensions(Input Parameter Category)
          Here for addition requirement has 4 dimensions
             1. Count → how many inputs?
             2. Type → positive/negative/zero
             3. Datatype → int/float
             4. Zero handling → allowed or not

        - Each dimension expands the possibilities(Input Variations)
          
        ** This expansion is what creates test scenarios. i.e, 
            “Each input parameter category produces its own set of input variations that developers must cover through test scenarios.”

Step 2: Create Scenario Buckets (Testing Methodology):
======================================================
        - A developer thinks in scenario buckets, not random test cases.
        - For this requirement, the scenario buckets are:
            A. Count-based Scenarios  : Does the function handle 2 numbers? 3 numbers? N numbers?
            B. Type-based Scenarios   : How does addition behave with +, –, and 0?
            C. Datatype Scenarios     : What happens with int vs float combinations?
            D. Zero-handling Scenarios: Is zero allowed? Does it change the result?

        ** These buckets ensure maximum coverage with minimum duplication, which is exactly what professional unit testing requires.

Step 3: Expand Each Bucket Into Scenarios:
==========================================
        - Now we expand each bucket into concrete scenarios.
          Scenarios are behavior descriptions, not input/output yet.
          
        A. Count-Based Scenarios:
        --------------------------
        | Scenario                    | Meaning                                               |
        | --------------------------- | ----------------------------------------------------- |
        | 1. Add exactly 2 numbers    | Basic operation (most common)                         |
        | 2. Add 3 numbers            | Multi-argument support                                |
        | 3. Add 4 or more numbers    | Scalability of the addition logic                     |
        | 4. Add 1 number (edge case) | Should return the same number                         |
        | 5. Add zero numbers         | Should raise error OR return 0 (based on requirement) |
        
        B. Type-Based Scenarios:
        ------------------------
        | Scenario                           | Meaning               |
        | ---------------------------------- | --------------------- |
        | 1. Both positive                   | Normal addition       |
        | 2. Both negative                   | Sum remains negative  |
        | 3. First positive, second negative | Mixed signs           |
        | 4. First negative, second positive | Reverse mixed signs   |
        | 5. Zero + positive/negative        | Zero-neutral behavior |
        | 6. Positive/negative + zero        | Same as above         |
        
        C. Datatype-Based Scenarios:
        ----------------------------
        | Scenario                         | Meaning                               |
        | -------------------------------- | ------------------------------------- |
        | 1. Both int                      | Integer arithmetic                    |
        | 2. Both float                    | Floating point arithmetic             |
        | 3. int + float                   | Type promotion expected (int → float) |
        | 4. float + int                   | Same as above                         |
        | 5. Non-numeric datatypes (error) | Strings, booleans, lists              |
        
        D. Zero-Handling Scenarios:
        ---------------------------
        | Scenario                | Meaning                |
        | ----------------------- | ---------------------- |
        | 1. Zero allowed         | Valid input            | 
        | 2. Zero not allowed     | Raise validation error |
        | 3. Zero as first input  | No effect              |
        | 4. Zero as middle input | No effect              |
        | 5. Zero as last input   | No effect              |

Step 4: Convert Scenarios → Test Cases (Unit Testing Standard)
=================================================================
        A test scenario becomes a test case when you attach concrete inputs + expected outputs.
        
        Example:  
        Scenario: Both numbers positive
                Test Case:        Input: 4 + 5        Expected Output: 9
        Scenario: int + float
                Test Case:        Input: 10 + 2.5     Expected Output: 12.5
        Scenario: Zero not allowed
                Test Case:        Input: add(0, 4)    Expected Output: Raise ValueError("Zero not allowed")
        
        This separation is what makes your engineers think clearly.

Step 5: How Developers Derive All Scenarios (Mindset Training):
=================================================================
        1. Break the requirement into independent dimensions  : Count, Type, Datatype, Zero
        2. For each dimension, ask               : “What can vary?” and “What can go wrong?”
        3. For every variation, define a scenario: This ensures coverage.
        4. Combine independent variations only when required
                Example:
                Positive + float
                Negative + float
                Zero + int
                        But avoid unnecessary duplicates.
        5. Validate each scenario against expected behavior
        
        This produces the final test cases.

Step 6: Why This Matters (Developer + QA Alignment):
====================================================
        This approach creates:
            ✔ Complete scenario coverage
            ✔ Minimal redundancy
            ✔ Predictable behavior
            ✔ High-quality unit tests
            ✔ Strong debugging confidence
            ✔ Professional-level testing habits
            
        This is exactly how senior developers think during:
            – TDD : Test Driven Development
            – Code reviews
            – Feature validation
            – API testing
            – Edge-case handling


'''