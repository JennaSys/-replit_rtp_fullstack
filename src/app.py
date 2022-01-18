from pyreact import render, useState, useEffect, component, Option
from pymui import Box, TextField
from jsutils import fetch


@component
def StyledTextField(props):
    new_props = {'type': 'text',
                 'fullWidth': True,
                 'variant': 'outlined',
                 'InputLabelProps': {'shrink': True},
                 'InputProps': {'margin': 'dense'},
                 'margin': 'dense',
                }

    new_props.update(props)
    return TextField(new_props)


@component
def UserVu(props):
    users = props['users'] if props['users'] else []

    def userToRow(user):
        return Option({'key': user[0], 'value': user[0]}, user[1])

    return [userToRow(user) for user in users]


@component
def App():
    users, setUsers = useState([])
    userID, setUserID = useState("")
    firstName, setFirstName = useState("")
    lastName, setLastName = useState("")
    username, setUsername = useState("")

    def handleChange(event):
        target = event['target']
        setUserID(target['value'])
        setFirstName("")
        setLastName("")
        setUsername("")

    def getUser():
        def _getUser(data):
            user_info = data if data else {}
            if len(user_info) > 0:
                setFirstName(user_info['FirstName'])
                setLastName(user_info['LastName'])
                setUsername(user_info['Username'])
            else:
                setFirstName("")
                setLastName("")
                setUsername("")

        if len(userID) > 0:
            fetch(f"/api/user/{userID}", _getUser)

    def getUsers():
        def _getUsers(data):
            user_list = data if data else []
            user_list.sort(key=lambda user: user[1])
            setUsers(user_list)
            setUserID("")

        fetch("/api/users", _getUsers)

    useEffect(getUser, [userID])
    useEffect(getUsers, [])

    return Box({'key': 'App', 'style': {'width': '200px'}},
              Box({'alignItems': 'center'},
                 StyledTextField({'label': "Select User",
                                      'value': userID,
                                      'onChange': handleChange,
                                      'select': True,
                                      'SelectProps': {'native': True},
                                      'autoFocus': True,
                                     },
                    Option({'key': '', 'value': ''}),  # Blank row
                    UserVu({'users': users}),
                   ),
                ),
              StyledTextField({'label': 'First Name',
                                   'value': firstName,
                                   'disabled': True,
                                  }
                ),
              StyledTextField({'label': 'Last Name',
                                   'value': lastName,
                                   'disabled': True,
                                  }
                ),
              StyledTextField({'label': 'Username',
                                   'value': username,
                                   'disabled': True,
                                  }
                ),
             ),

render(App, None, 'root')
