from common import require, document, window, __new__  # __:skip


# Load React and ReactDOM JavaScript libraries into local namespace
React = require('react')
ReactDOM = require('react-dom')


# Map React javaScript objects to Python identifiers
# createElement = React.createElement
useState = React.useState
useEffect = React.useEffect
createContext = React.createContext
useContext = React.useContext


def component(component):
    def react_element(props, *children):
        return React.createElement(component, props, *children)

    return react_element


Fragment = component(React.Fragment)

# Modal = component(require('react-modal'))
# ReactGA = require('react-ga')

Form = component('form')
Label = component('label')
Input = component('input')
Ol = component('ol')
Li = component('li')
Option = component('option')
Button = component('button')
Div = component('div')
Span = component('span')
P = component('p')
A = component('a')
Img = component('img')
H1 = component('h1')
H2 = component('h2')


def render(root_component, props, container):
    def main():
        querystring = window.location.search
        params = __new__(window.URLSearchParams(querystring)).entries()
        new_props = {'pathname': window.location.pathname,
                     'params': {p[0]: p[1] for p in params if p}}
        new_props.update(props)
        ReactDOM.render(
            root_component(new_props),
            document.getElementById(container)
        )

    document.addEventListener('DOMContentLoaded', main)
    window.addEventListener('popstate', main)

