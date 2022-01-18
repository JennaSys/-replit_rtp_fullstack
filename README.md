# React to Python: Fullstack example

### A simple React/Material-UI fullstack example from chapter 20 of the [React to Python](https://pyreact.com) book.

Click the button below to clone and run it on Replit (A free [Replit](https://replit.com/) account is required):

[![Run on Repl.it](https://repl.it/badge/github/JennaSys/replit_rtp_fullstack)](https://repl.it/github/JennaSys/replit_rtp_fullstack)

Or you can just view the Replit repl [here](https://replit.com/@JennaSys/replitrtpfullstack).

To generate the development JavaScript bundle, run `. ./build.sh` in the shell (note the leading dot!).

Running the repl afterwards will then serve up the generated JavaScript files with Flask.

### About
This Replit repl has been created to give you an idea of what coding a React application in Python looks like, without having to set up a development environment specific to that task yourself.  You can also use this repl as a template for creating your own Python React projects that are based on utilizing the [Transcrypt](https://www.transcrypt.org) transpiler.

This demo deviates a little bit from the book in that the version used here is an example using of the ["No-el"](https://dev.to/jennasys/no-el-eliminate-explicit-calls-to-createelement-when-using-python-to-code-react-applications-5214) approach.  This approach eliminates having to call `React.createElement()` explicitly, as was presented throughout the book, by instead wrapping React functional components in a Python decorator.

### Setup
The first time you run the `build.sh` shell script, it will check for installed dependencies.  If not found, it will do the following:  
- Install Python 3.9 (required by Transcrypt)
- Install Python dependencies
- Install JavaScript dependencies

Once that is done, it will transpile and bundle the generated JavaScript files and then launch a development server. The development server can be stopped with `Ctrl-c`.

After the development server is stopped, you can run the repl which will start up Flask to serve up the generated files.

