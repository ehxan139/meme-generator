# Project: Motivational Meme Generator

## Introduction
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. The application can generate a random quote and image from a list of quotes and images. It can also take a user supplied quote and image and generate a meme. It can be used through a CLI or as a web application.

The main modules of the project are:

### Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. 

### Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images and saving them to a directory or displaying them in a browser.

### CLI Usage
To run the application, install the dependencies from requirements.txt file. Then application can be run from the src directory from command line. 

* To generate a random meme, run the following command:
    ```
    python meme.py
    ```

* To generate a meme with a user supplied quote and image, run the following command:
    ```
    python meme.py  --path "image.jpg" --body "I am the quote" --Author "I said it"
    ```

### Web Usage
To the run the application as a web application, run the following command:
    ```
    python app.py
    ```
This will start a web server on port 5000 and host the application in the src directory.
