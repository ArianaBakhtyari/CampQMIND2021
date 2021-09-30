# Camp QMIND 2021

## Getting Started
### Step 1: Forking
First you want to create a fork (local copy) of this repository in your own account. Click the ![alt text](https://i.imgur.com/Js2wIHu.png "fork") button at the top right and select your account.

### Step 2: Cloning
On your own fork, clone the repository to your computer. You can find the address in the green code button as shown below.

![alt text](https://i.imgur.com/1ynocH4.png "HTTPS link from the code button dropdown")

Now on your computer it's time to use git. Make sure you have [git installed](https://git-scm.com/downloads) on your computer. You should be running all commands in the git terminal. Open a git terminal, navigate to the folder you want the repository downloaded to ([using the cd command](https://www.howtoforge.com/linux-cd-command/)), and run:

`git clone [the repository URL from the image above]`

Then enter the repository by running:

`cd CampQMIND2021`

### Step 3: Creating a Virtual Environment and Installing Dependencies
A virtual environment is a way of managing dependencies in Python. Insteal of installing them to your computer, you install them to your project's virtual environment. We have included a file `requirements.txt` that lists all dependencies. We will use this file to setup our project.

#### Step 3.1: Without Anaconda

First you need to create a virtual environment. This can be done by running:

`python -m venv env`

Now activate it:

`source env/Scripts/activate`

Check you are in the virtual environment by running the following command and making sure it prints (env) at the end:

`pip -V`

And finally, install your dependencies by running:

`pip install -r requirements.txt`

#### Step 3.2: With Anaconda

> For Anaconda, all commands should be run in the Anaconda Prompt instead of the git terminal.

First you need to create a virtual environment. This can be done by running:

`conda create --name env python=3.8`

Now activate it:

`conda activate env`

You should now see (env) to the right of the command line.

And finally, install your dependencies by running:

`conda install --file requirements.txt`


## Workshop Streams
| Slot | Coding                                             | Data Science                                       | DT                                         |
|------|----------------------------------------------------|----------------------------------------------------|--------------------------------------------|
| 1    | Intro to Python (Nathan)                           | ML / Data Science Tools Review (Adam Farley)       | DT Intro (Matt Wright)                     |
| 2    | Crash Course on Git / GitHub (Sean Sutherland)     | Feature Engineering (Mimi)                         | Quantum Cryptography (Spencer Hill)        |
| 3    | Working with Datasets (Griffin)                | Sourcing data, web-scraping, etc. (Adam Farley)    | Grover's Algorithm (Paul Santilli)         |
| 4    | Working / Communicating in a Team (Ariana)         | Working / Communicating in a Team (Ariana)         | Working / Communicating in a Team (Ariana) |
| 5    | Overview of ML Algorithms (Ethan Callanan)         | Computer Vision (Daniel Stewart)                   | Decentralized Voting System (Bhavan)       |
| 6    | Starting a Project + Picking a Model (Adam Farley) | Starting a Project + Picking a Model (Adam Farley) | Decentralized Auction (Mustafa)            |
