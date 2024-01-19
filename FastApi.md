# DOJO 1

## Fast API:
We talked about basics of python, web serving, and fast api. Now lets put it all together and create our own server.
Goal is to create a website that will show people how to create a website themselves. Tune in next week for more info
to add to the website, and eventually we will deploy it to the internet but for now lets start with the basics. 
### Creating a Fast API application:
We will provide a skeleton for you to start with. You can find this in main.py. Routes to build:
* [get] /: This will be the home page. This page should have a navigation bar with links to the other pages and a brief description of the website.
* [get] /basics: This page will include information from basics.md
* [get] /web_serving: This page will include information from web_serving.md
* [get] /fast_api: This page will include information from fast_api.md
* [get] /web_development: This page will include information from web_development.md
* [get] /notes 
* [post] /notes

### Serving static files:
We will be serving 2 static files, a css file and a js file. These files will be in the static directory. 
* static/css/style.css
* static/js/script.js

### Templates: