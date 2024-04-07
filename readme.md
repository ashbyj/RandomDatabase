# simple database maker

## purpose

i would like to be able to generate databases with random and sensical data.  there are a couple of recent use cases that prompted this.

### viz for the job

i was tasked with building a new dashboard based on vague and uncertain requirements.  i had a general idea of what the data would look like, but no actual data.  if i had been able to build the viz on fake data, i could have just plugged the real data in and been much further ahead.

### hackerrank 

i was practicing for an interview on HackerRank and realized it would be useful to quickly build the small database they described in some of the problems.  its not necessary, but would have been nice to have.

## features needed

- a way to generate random data of different types
    - names (first and last)
    - dates 
    - integers (given a range)
    - continuous values (range, precision)
    - others to be added later
        - geographic locations
            - streets
            - cities
            - addresses
            - countries
            - provinces
        - color codes (rgb, cymk, etc)
        - relationships
        - roles
- a way to take an ERD-like diagram with:
    - table names
    - column names
    - foreign key relationships
        - 1:1
        - 1:many
    - primary keys
        - composite keys?
- a method to communicate with a dbms.  
    - odbc?
    - jdbc?
    - will need to include a way to input/store credentials
    - option to create new sqlite and save as file

## roadmap

### mvp 
- [ ] build hackerrank problem db manually
- [ ] populate above with random data and heavy manual intervention on keys
- [ ] populate above programmatically, keys included
- [ ] take input file for hakcerrank and build db programmatically
    - [ ] decide on input format

### next iteration
- [ ] add more datatypes
- [ ] allow for composite keys

### next iteration
- [ ] allow for input on distributions
    - for example, 3 companies with a 60/20/20 split 
