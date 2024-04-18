# ML_project_LearningPath

## Step 1: Create a new environment

1. Navigate to the project folder and open it with Visual Studio Code.
2. Open a new terminal.
3. Run the following command to create a new virtual environment named `myenv`:

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment by running the appropriate command based on your operating system:

    For Windows:
    ```bash
    myenv\Scripts\activate
    ```

## Step 2: Create a .gitignore file

1. In the project folder, create a new file named `.gitignore`.
2. Open the `.gitignore` file in a text editor.
3. Add file paths and patterns for Git to ignore. 
4. Save the `.gitignore` file.

## Step 3: Create a requirements.txt file
 ```bash
   pip install -r requirements.txt
 ```
## Step 4: Create a setup.py file
 ```bash
   This is to install the entire project as a package. Additionally, write a function to read the packages from requirements.txt
 ```
## Step5: Create a folder src
 ```bash
   Include exception, logger, and utils python files. Make this folder as a package by including __init__.py file. The scr folder will include another folder with name components will be created. Include __init__.py also 
 ```
   ### Step 5.1 Create a folder components
 ```bash
   Include data_ingestion, data_transformation, model trainer, and __init_.py. These components are to be interconnected in future. 
 ```
   ### Step 5.2 Create a folder called pipeline
 ```bash
   Create two python files training_pipeline and prediction_pipeline with __init__.py folder
 ```
