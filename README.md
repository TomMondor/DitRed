# DitRed

## To use locally :

- Clone the repository.
  ```
    git clone https://github.com/TomMondor/DitRed.git
  ```

- Create a .env file to store your mySQL username and password.
  ```
    USER=myUserNameNoQuotesAround
    PASSWORD=myPasswordNoQuotesAround
  ```
  
- Create a conda environment using the environment.yml file.
  ```
    conda env create --file environment.yml
  ```

- Run the `DB_populate_script.py` to create and populate the database with fake, random data.
