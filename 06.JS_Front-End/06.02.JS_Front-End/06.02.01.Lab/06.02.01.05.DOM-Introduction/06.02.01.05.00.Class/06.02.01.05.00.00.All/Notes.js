/*
Browser API === BOM (Browser Object Model)
- The global object in the browser is the Window; this is to point towards the Global Scope;
- API === Application Programming Interface


Document Object Model
- DOM represents the document as nodes & objects; That way, the programming languages can connect to the page
- The HTML DOM is an Object Model for HTML, which defines:
    - HTML elements as objects;
    - Properties;
    - Methods;
    - Events;
- The Browser parses HTML and creates a DOM tree
- DOM Methods: Actions you can perform on HTML elements (e.g. Add/Delete HTML element);
- DOM Properties: Values of HTL elements that you can set or change;
- JS interacts with webpages via DOM API:
    - Checks contents & Structure of elements on the page;
    - Modify element style and properties;
    - Reading user input and reacting to events;
- Most actions are performed when an event occurs:
    - Events are 'fired' when something of interest happens;
JS code can be executed in a browser webpage in different ways:
    - Directly in Developer Console -> When debugging;
    - As a page Event Handler -> e.g. User clicks on a button;
    - Via inline script -> Using <script> tags;
    - By importing from external file -> Most flexible approach;
*/


/*
HTML Elements
- DOM Tree comprises HTML elements;
- Elements are JS Objects with properties and methods that can be accessed and modified like regular objects;
- To change the contents of the page:
    - Select an element to obtain its reference;
    - Modify its properties;

Attributes are defined by HTML;
- Attributes initialize the DOM properties;
- Property values can change via the DOM API;
- The HTML attribute & the DOM property are technically NOT the same thing; The outcome is the same; so the
difference would almost never be encountered in practise;

DOM Manipulations;
- HTML DOM allows JS to change the content of HTML elements;
    - innerHTML -> Returns inner HTML of n element; It is not a good idea to be used commonly, because of the threat of
    an XSS attack; Better alternative is to use textContent;
    - textContent -> Text content in an element;
    - value -> Gets the values of input fields;
    - style -> Getting (and/or changing) the current style of the element;
    - etc.

*/


/*
Targeting Elements Methods; These methods return a reference to the element, which can be manipulated with JS;
- By ID -> getElementById() => There is only one element with that ID;
- By class name -> getElementsByClassName() => There can be multiple elements with that class; We are searching through
the collection of the elements, sharing the same class;
- By tag name -> getElementsByTagName() => There can be multiple elements with that tag; We are searching through
the collection of the elements, sharing the same class;
- By CSS selector -> querySelector() & querySelectorAll() => Searching through the CSS selectors; querySelector()
returns the 1st found element that has that selector; querySelectorAll() returns a collection of all the elements
with that selector;

NodeList VS HTMLCollection;
- Both interfaces are collections of DOM Nodes;
- NodeList can contain any node type, including text & whitespace;
- HTMLCollection contains nly Element nodes;
- Both have iterations methods; HTMLCollection has an extra namedItem method;
- HTMLCollection is live, while NodeList can be either live or static;
- Iterating through collections;
    - They are NOT arrays, but can be indexed & iterated;
        const elements = document.querySelectorAll('p);
        // Selecting the 1st paragraph on the page;
        const first = elements[0];
        // Iterating over all entries;
        for (let p of elements) {
            // Insert Functionality Here
        }
    - Both can be explicitly converted to an array using:
        const elemArray01 = Array.from(elements);
        const elemArray02 = [...elements];
- Every DOM element has a parent;
    - Parents can be accessed by property parentElement or parentNode;
- When element contains other elements that element is a Parent and the elements inside are Children;
    - The Children elements can be accessed by the property children;

Content can be hidden/reveled by changing its display style; This is a common technique to display content dynamically;
- Hiding an element;
    const element = document.getElementById('main');
    element.style.display = 'none';
- Revealing an element; The display should be set to anything that isn't 'none', including an empty string;
    const element = document.getElementById('main');
    element.style.display = '';

Match n-th Child;
- Sometimes an element needs to be targeted based on its relation to other similar elements (e.g., row/column in a table,
list item, etc.);
- This can be done by index or with CSS selector;
    // // Via index;
    // 1st <ul> element on the page;
    const list = document.getElementsByTagName('ul')[0];
    // 3rd <li> element inside the selected <ul> element;
    const thirdLi = document.getElementsByTagName('li')[2];

    // // Via CSS selector;
    // 3rd <li> element inside the selected <ul> element;
    const thirdLi = document.querySelector('ul li:nth-child(3)');

*/


/*

Using the DOM API


*/