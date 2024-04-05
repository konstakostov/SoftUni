/*
DOM Manipulation
- Create, Append, Remove HTML elements dynamically;
    - appendChild() -> Adds Child Element to Parent Element; Moves Child Element from one Parent Element to another.
    - removeChild() -> Removes Child Element from Parent Element;
    - replaceChild() -> Replaces Child Element from one Parent Element with another.

- HTML elements are created with a Factory Patter;
    - document.createElement() -> Creating a HTML element;
    - The created variables are live -> If the content is modified, the DOM is updated; If you insert it somewhere in
    the DOM, the original is moved;
    - Text added to textContent will be escaped;
    - Text added to innerHTML will be parsed and turned into actual HTML elements; This is prone to XSS attacks;
    - The elements are created in memory - they don't exist on the page;
    - For the elements to become visible, they must be appended to the DOM tree;

- Manipulating the Node Hierarchy;
    - appendChild() -> Adds new Child as the last Child;
    - prepend() -> Adds new Child as the first Child;
*/

// Creating a new DOM element;
let p = document.createElement('p');
let li = document.createElement('li');

// Creating a copy/clone of a DOM element;
let li01 = document.getElementById('my-list');
let newLi01 = li.cloneNode(true);

// Adding new Child as the last Child;
let p02 = document.createElement('p');
let li02 = document.createElement('li');
li.appendChild(p02)
li.appendChild(li02)

// Adding new Child as the first Child;
let p03 = document.createElement('p');
let li03 = document.createElement('li');
li.prepend(p03)
li.prepend(li03)


/*
The DOM Event
- Event Object;
    - It calls it's associated function;
    - It passes a single argument to the function -> Reference to the event object;
    - It contains properties that describe the event;
        - Which element triggered the event;
        - Screen coordinates where it occurs;
        - What is the event type;
    - Some of the event types are: Mouse, Touch, DOM/UI, Keyboard, Focus, Form events;
*/


/*
Event Handling

- Event Handler;
    - Event registration is done by providing a Callback function;

- Ways to Register for Event;
    - With HTML Attributes ->
    - Using DOM Element Properties ->
    - Using DOM Event Handler -> Preferred Method;

- Event Listener (Registering ro Event using DOM Event Handler);
    - addEventListener() -> Adds event listener; Allows adding multiple listeners to the same element, without
    overwriting the existing ones;
    - removeEventListener() -> Removes event listener;
*/

// Adding event listener;
htmlRef.addEventListener('click', handler);

// Adding Multiple Listeners;
element.addEventListener("click", myFirstFunction);
element.addEventListener("click", mySecondFunction);
element.addEventListener("mouseover", myThirdFunction);
element.addEventListener("mouseout", myFourthFunction);

// Removing event listener;
htmlRef.removeEventListener('click', handler);


/*
Event Propagation
- Mechanism by which events are handed and propagated through the DOM; In the DOM events can occur on various elements,
and they can propagate in different phases: Capturing, Target and Bubbling Phase;

- Main phases of Event Propagation;
    - Capturing Phase -> Simple: From the outside to the inside; In this phase, the event is captured from the root of
    the DOM hierarchy down to the target element. During this phase, the event travels from the outermost ancestor
    element to the target element. Event handlers attached at higher levels in the DOM hierarchy will be triggered first.
    - Bubbling Phase -> Simple: From the inside to the outside; After the event reaches the target element, it enters
    the bubbling phase. In this phase, the event bubbles up from the target element to its ancestors in the DOM levels
    in the DOM hierarchy will be triggered first.

    - The capturing and bubbling phases provide an opportunity for event handlers to intercept and handle events at
    different levels of the DOM hierarchy. Event propagation can be controlled using the addEventListener() method by
    specifying the third parameter useCapture, which determines whether the event should be captured during the
    capturing phase (true) or during the bubbling phase (false, default behavior).

- Events in DOM by default are propagated with the Bubbling Phase;
*/

/*
Default Browser Behavior
- preventDefault -> Stops the browser from executing default behavior (Navigating to a new page when <a> is clicked,
Submitting HTTP request via forms);
*/