# CTCTF 2015: Kelvin's Corner

### Problem

**Points**: 15

**Description**: 

> Kelvin just created his personal website. See if there's anything suspicious!  
> Kelvin's Website

**Hint**: 

> Try viewing the page source

### Solution

The hint explicitly says to look at the [page](http://ctctf.io/problem_data/Kelvin/website.html)'s source, which is the raw HTML that specifies how the page should be formatted. In Chrome, we can view the [page source](website.html) using <kbd>CTRL</kbd>+<kbd>U</kbd> (or <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>J</kbd>, which opens up the developer console).

The flag is in the comment, which is marked with `<!--` and `-->`, after the image element.

**Flag**: `don't_take_food`

### Other Resources

* [HTML Tutorial](http://www.w3schools.com/html/)
