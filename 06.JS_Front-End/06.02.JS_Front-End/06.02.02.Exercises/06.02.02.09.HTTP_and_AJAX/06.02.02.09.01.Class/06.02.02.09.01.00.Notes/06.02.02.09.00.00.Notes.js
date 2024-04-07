/*
HTTP Overview & Developer Tools
- Hyper Text Transfer Protocol;

- Text-based client-server protocol for the Internet;
- Transferring Web Resources (HTML files, images, styles, etc.);
- Request-response based;

- Defines methods to indicate the desired action to be performed on the identified resource;
    - GET -> Retrieve/Load a resource;
    - POST -> Create/Store a resource;
    - PUT -> Update a resource;
    - DELETE -> Delete(Remove) a resource;
    - PATCH -> Update resource partially;
    - HEAD -> Retrieve the resource's headers;
    - OPTIONS -> Returns HTTP methods that the server support for the specified URL;

- HTTP Response: Status Codes -> Action => Description;
    - 200 ->  OK => Successfully retrieved resource
    - 201 ->  Created => A new resource was created
    - 204 ->  No Content => Request has nothing to return
    - 301/302 -> Moved => Moved to another location (redirect)
    - 400 -> Bad Request => Invalid request / syntax error
    - 401/403 -> Unauthorized => Authentication failed / Access denied
    - 404 ->  Not Found => Invalid resource
    - 409 ->  Conflict => Conflict was detected, e.g. duplicated email
    - 500/503 ->  Server Error => Internal server error / Service unavailable

- Content-Type/Content-Disposition headers specify how the HTTP request/response body should be processed;
*/


/*
REST & RESTful Services;
- Representational State Transfer;

- Rest
    - Architecture for Client-Server Communication over HTTP;
    - Resources have URI (address); Resources are logical abstraction; Resources can be nested;
    - Can be Created/Retrieved/Modified/Deleted;
    - Convention for creating Request and Responses following specific rules;

- RESTful API/RESTful Service;
    - Provided access to server-side resources via HTTP and REST;
*/


/*
NPM & package.json

- Node Package Manager (NPM);
    - Package manager for JS and Node.js projects;
    - Simplifies installing, managing, sharing libraries and tools in web development;
    - Bundled with Node.js; Offers command-line interface;
    - Facilitates integrating third-party packages to reuse existing code & speed up development;
    - Helps manage project dependencies, ensuring required packages are available;
    - Allows defining & running scripts through the project's package.json file;

- package.json;
    - Metadata file used in Node.js projects to provide information about the project, its dependencies, and various
    configurations;
    - Includes details as project's name, version, description, author, license, etc., making it a central place to
    document essential project information;
    - Integral to Node.js & NPM ecosystem; When sharing project, including the package.json file lets others quickly
    understand & recreate your project's environment; It makes it easy for others to install the correct dependencies
    with a single command - npm install;
*/