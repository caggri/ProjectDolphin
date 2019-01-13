# ProjectDolphin
Repository for CS461-Artificial Intelligence course. It will contain Homework and Project.

It is an AI program that solves New York Times Daily Mini crossword puzzle prepared by Joel Fagliano.

Instructor: Prof. Varol AKMAN

# Usage

For homeworks, you can simply compile source codes and see the outputs.

## Project
* You need Node, ReactJS and Python 3 to run the project.
* Clone the project folder.
### ***Front-End***




* Start React server:
```
$ cd Front-End
```
```
$ npm install
```
```
$ npm start
```

Front-End server should be working now.

### ***Back-End***
* For Back-end we use Python 3 to install it is highly recommended to use a Virtual Environment.
* Before installing Back-End server make sure you have Python 3, pip and Virtual Environment. Make sure you have downloaded Python > 3.4, pip is bundled with newer versions. 

* If you don't have Python 3, pip, Virtual Environment do following steps.

  1. Check your Python version
      * for Windows by typing
          ```
          python --version
          ```  
      * for UNIX-Like Operation Systems (Mac OS X / OS X / macOS / GNU Linux Distributions) by typing
          ```
          python3 --version
          ```
      * If you don't have Python 3
         * Python 3 can be downloaded from
             ```
             https://www.python.org/
             ```

  2. Installation of  Virtual Environment
      * for Windows by typing
          ```
          py -m pip install --upgrade pip
          ```  
      * for UNIX-Like Operation Systems by typing
          ```
          python3 -m pip install --user --upgrade pip  
          ```


* To create and start a Virtual Environment
  * Create a Virtual Environment by typing
     ```
     python3 -m venv virtual_environment_name
     ```
     This command will create a folder with the given name.

  * To start Virtual Environment go to created folder
    * for Windows by typing
        ```
        tutorial-env\Scripts\activate.bat
        ```  
    * for UNIX-Like Operation Systems by typing
        ```
       source bin/activate
        ```


* All project dependencies listed in requirements.txt file in back-end folder.
    * to install dependencies, type
        ```
        pip install -r requirements.txt
        ```  
        This command will install all dependencies automatically.

### ***Crawler***
* Crawler needs Google Chrome. Download the suitable ChromeDriver from here http://chromedriver.chromium.org
* Specify the path of ChromeDriver in line 161 in crawler<span></span>.py

<br/>

Installation process completed, now you can run the Back-End server by typing:

```
python server.py
```
  
* Virtual Environment can be deactivated by typing,
```
deactivate
```




<!-- Bunu nereye koyacağımı bilemedim > It's all done! Happy hacking :)-->
