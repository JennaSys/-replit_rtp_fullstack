# React to Python: Fullstack example

## A simple fullstack example from chapter 20 of the React to Python book.

Click the button below to clone and run it on Replit (A free [Replit](https://replit.com/) account is required):

[![Run on Repl.it](https://repl.it/badge/github/JennaSys/replit_rtp_fullstack)](https://repl.it/github/JennaSys/replit_rtp_fullstack)

To generate the development JavaScript bundle, run `. ./build.sh` in the shell (note the leading dot!).

Running the repl afterwards will then serve up the generated JavaScript files with Flask.

### Setup
The first time you run the `build.sh` shell script, it will check for installed dependencies.  If not found, it will do the following:  
- Install Python 3.9 (required by Transcrypt)
- Install Python dependencies
- Install JavaScript dependencies

Once that is done, it will transpile and bundle the generated JavaScript files and then launch a development server. The development server can be stopped with `Ctrl-c`.

After the development server is stopped, you can run the repl which will start up Flask to serve up the generated files.

