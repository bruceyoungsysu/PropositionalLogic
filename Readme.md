# Readme

## 1. Basic info:

- Collaborators: No other collaborators.

- File structure:

  ```
  ./
  + -- TT_check.py    #model check main logic
  + -- resolve.py     #resolution main logic
  + -- propositional_logic.py    #basic propositional logic structure
  + -- CNF.py    # hardcoded problems and cnf logic needs tests
  
  ```

## 2.How to build

- To check the result of model check, simply run:

  ```shell
  python ./TT_check.py
  ```

  To check the result of resolution, simply run:

  ```
  python ./resolve.py
  ```

  the output of both files will be

  ```shell
  problem1: 
  Q : True
  ********************
  problem2: 
  p21 : False
  ********************
  problem3: 
  mythical : False
  horned : True
  magical : True
  ********************
  problem4_a: 
  A : False
  B : False
  C : True
  ********************
  problem4_b: 
  A : True
  B : False
  C : False
  ********************
  problem5: 
  A : False
  B : False
  C : False
  D : False
  E : False
  F : False
  G : False
  H : False
  I : False
  J : True
  K : True
  L : False
  ********************
  problem6_a: 
  X : True
  Y : False
  Z : False
  W : False
  ********************
  problem6_b: 
  X : True
  Y : False
  Z : False
  W : False
  ********************
  ```

- The problems are hardcoded in `./CNF.py`. To check the algorithms with other problems. Please formulate the problem as a `problem` class:

  ```python
  import problems from CNF
  class my_problem(problems):
      def __init__(self):
          problems.__init__(self)
          self.name = "problem1"  # name your problem
          self.chars = ["P", "Q"] # the name of symbols in your problems, symbols will be auto generated
          self.qs = ["Q"]  # the name of symbols you want to check correctness
          self.init_models()  # auto generate symbols
          self.kb = [pl_imply(P,Q),P] # hardcode your knowledge base for model check
          self.kb_r = [{P}, {pl_not(P), Q}, {pl_not(Q)}] # hardcode your kb for resolution
  ```

  For how to build a knowledge base and the basic propositional logic data structure, please refer to the writeup for more details. 