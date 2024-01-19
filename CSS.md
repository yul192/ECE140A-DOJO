# DOJO 1:

## CSS Basics:
### Structure:

### How to Use:
CSS can be included in a webpage in a few different ways. Firstly, it can be definied directly in the HTML page by using the style tag as shown below.
```html
<style>
    body {
        background-color: blanchedalmond;
    }
</style>
```
Isn't css so cool? You can add all kinds of colors. We choose blanchedalmond because it is the best sounding color.

The snippet above will change the background color of the body tag (essentially the whole visible webpage) to the specified color. CSS supports raw RGB, hex, and other color formats, as well as some pre-defined names.
***
In addition to the style element, CSS can be contained in its own file, separate from the HTML, and then essentially imported by the HTML page.
```html
<head>
    <link rel="stylesheet" href="static/css/index.css">
</head>
```
```css
body {
    background-color: blanchedalmond;
}
```
The ```<link>``` tag tells the browser that it needs to request the stylesheet resource located at ```css/index.css```, and to load it as a stylesheet. Using an external stylesheet is helpful when you have multiple different web-pages and want to share style between them (not having to write the same code multiple times).
***
The last main way CSS can be used in a web-page is inline through the ```style``` attribute on any element in an HTML page.
```html
<body>
    <h1 style="color: red;">Welcome to the ECE 140A Dojo!</h1>
</body>
```
Notice that when inline styling is used, the selector is omitted, and the rule is directly written there. Inline style is useful when trying small tweaks to perfect your layout.