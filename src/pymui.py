from pyreact import component

# Basic MUI components
Button = component(require('@material-ui/core/Button')['default'])
List = component(require('@material-ui/core/List')['default'])
ListItem = component(require('@material-ui/core/ListItem')['default'])
Typography = component(require('@material-ui/core/Typography')['default'])
Input = component(require('@material-ui/core/Input')['default'])
InputLabel = component(require('@material-ui/core/InputLabel')['default'])
Box = component(require('@material-ui/core/Box')['default'])
TextField = component(require('@material-ui/core/TextField')['default'])
Paper = component(require('@material-ui/core/Paper')['default'])
AppBar = component(require('@material-ui/core/AppBar')['default'])
Container = component(require('@material-ui/core/Container')['default'])

# Theming
ThemeProvider = component(require('@material-ui/styles/ThemeProvider')['default'])
useTheme = require('@material-ui/styles/useTheme')['default']
createMuiTheme = require('@material-ui/core/styles/createMuiTheme')['default']
colors = require('@material-ui/core/colors')
makeStyles = require('@material-ui/styles/makeStyles')['default']
styled = require('@material-ui/styles/styled')['default']
