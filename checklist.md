
# Assessment criteria for 4 project (Data Centric Development)


Hello everyone!

So here we have all the criteria that are taken for assessment of database 4 project in one clean easy access markdown document! 

- Don't leave your editor while checking your criteria for project :)
- Get better understanding from what grade is coming from. 
- Get instant access to requirements.   

Just tick them [x] while developing. It can be used in case of previous projects - just delete not applicable section.

## Application Features
## App logic

- [ ] Each of the Django apps that form the projectcomponents in an app make sense within the context of that app.
- [ ] Each of the Django apps that form the project is built correctly and functions well.
- [ ] Each app matches a natural aspect of the project, with no app being too small or too big.
- [ ] All files and components in an app make sense within the context of that app.

### Cross-app logic

- [ ] The Django apps that form the project are designed to work well with one another.
- [ ] Application urls are set up in a consistent manner
- [ ] Any data in the models that is relevant to multiple apps is shared, rather than duplicated.
- [ ] The Django apps that form the project are designed to work well with one another.
- [ ] Application urls are set up in a consistent manner
- [ ] Any data in the models that is relevant to multiple apps is shared, rather than duplicated.

### E-commerce

- [ ] The site contains e-commerce functionality, which works well with a test credit card (4242 4242 4242 4242).
- [ ] Successful and unsuccessful purchases are indicated to the user with a helpful message.
- [ ] The site contains e-commerce functionality, which works well with a test credit card (4242 4242 4242 4242).
- [ ] Successful and unsuccessful purchases are indicated to the user with a helpful message.

### Authentication and Security
- [ ] Any functionality that requires log-in is available only to logged-in users (and anonymous users are redirected to login).
- [ ] The log-in and registration pages are only available to anonymous users (and logged-in users are redirected out automatically).
- [ ] Users are never asked to submit data that the site already has, e.g., if you have a Contact Us form, don’t ask for the email of a logged-in user.
- [ ] If different users have different permissions, then check their access levels are appropriate. (e.g., a non-admin user should not be able to edit another user’s post).
- [ ] Any functionality that requires log-in is available only to logged-in users (and anonymous users are redirected to login).
- [ ] The log-in and registration pages are only available to anonymous users (and logged-in users are redirected out automatically).
- [ ] Users are never asked to submit data that the site already has, e.g., if you have a Contact Us form, don’t ask for the email of a logged-in user.
- [ ] If different users have different permissions, then check their access levels are appropriate. (e.g., a non-admin user should not be able to edit another user’s post).

## Code Quality

### Appropriate use of Django
The Django file structure is consistent and logical, following the Django conventions.
All logic appears in the component where it is best suited. e.g., data handling logic is in the models, business logic is in the views
There is no unneeded complexity.
The Django file structure is consistent and logical, following the Django conventions.
All logic appears in the component where it is best suited. e.g., data handling logic is in the models, business logic is in the views
There is no unneeded complexity.

## Code Quality

### Appropriate use of Python

- [ ] Your project includes sufficient custom Python logic to to demonstrate your proficiency in the language	
- [ ] It includes functions with compound statements such as if conditions and/or loops.	
- [ ] Your Python code is consistent in style and preferably conforms to the PEP8 style guide	
- [ ] Check your Python indentation is valid.

### Appropriate use of the template language

- [ ] Your template code is valid and well organised.	
- [ ] Your template code demonstrates solid understanding of template tags and template inheritance.	
- [ ] There is no unneeded complexity

## Software Development practises

### Data Store Integration

- [ ] The project makes good use of a data store (database, or data files such as json) to maintain data in a consistent and well-organized manner.	
- [ ] The contents of the data store are persisted between requests.	
- [ ] As Heroku does not support media file upload, have you stored them on an external service?	
- [ ] The data store configuration is kept in a single location and can be changed easily.	
- [ ] Regular users are not able to access the data store directly without going through your code.

### Deployment Implementation

- [ ] There are well-kept Procfile, requirements.txt file, settings files, etc., including separate versions/branches of these if relevant.	
- [ ] All secret keys are hidden in environment variables or in files that are in .gitignore.	
Debug mode (e.g. in Flask or Django) is disabled for the deployed version

### Deployment Write-up

- [ ] Your README describes the deployment procedure including settings files, environment variables, dependencies and any other differences between the dev and live versions	
- [ ] If you have created an automated script to help deploy the project, you should include it (or link to it) in your write-up.

### Appropriate use of JavaScript

- [ ] Your project includes sufficient custom JavaScript logic to demonstrate your proficiency in the language.	
- [ ] In particular, it includes functions with compound statements such as if conditions and/or loops.	
- [ ] Your JavaScript code passes through a linter (we recommend jshint.com) with no major issues.	
- [ ] Check that there are no errors in the console during all interaction with the site.	
- [ ] The code is indented in a consistent manner to ease readability, and there is consistent use of empty lines.	
- [ ] All non-trivial JavaScript code should be kept in an external file(s) linked to at the bottom of the body element (or bottom of the head element if needs loaded before the body HTML).

### Appropriate use of JavaScript APIs (if used)

- [ ] Your project includes JavaScript code that uses external and/or internal APIs (e.g. TMDb, Google Maps, Canvas, dc.js, etc.) in an effective manner.	
- [ ] There is a clear separation between input logic, processing, and presentation logic.	
- [ ] There are no bugs or unneeded complexity	
- [ ] The code is robust against race-conditions - the code never relies on the duration of specific processes	
- [ ] The API-related code demonstrates a solid understanding of asynchronicity and callbacks/promises.

## Usability and Real-World application

### Project Purpose

- [ ] The project has a clear, well-defined purpose addressing the needs of a particular target audience (or multiple related audiences).	
- [ ] The project’s purpose is evident to a new user without having to look in the documentation.	
- [ ] The project’s documentation provides a clear rationale for the development of this project.

### UX design

- [ ] The project's documentation describes the UX design work undertaken for this project and the reasoning behind it.	
- [ ] Any wireframes, mock-ups, diagrams etc... you created as part of the design process are included in the project
- [ ] Suitability for purpose
- [ ] The site's design, as implemented, provides a good solution to the users' demands and expectations.	
- [ ] A regular user would not immediately think "there's a much better way to do this" about any part of the project.

### Navigation

- [ ] All resources on the site are easy to find, allowing users to navigate the layout of the site intuitively.	
- [ ] The site’s navigation is consistent and reasoned.	
- [ ] There is never a need to use the Back button to move through the site.	
- [ ] For any external links, the target=”_blank” attribute is used.	
- [ ] There are no broken links.

### Ease of Use

- [ ] It is easy and straightforward for a new user to figure out how to use your site without having to read any documentation	
- [ ] Have you had others (for example, family members, friends and/or other students) try out your site and they all said so?	
- [ ] The site is intuitive to use and never confuses the user or surprise them in a negative way.	
- [ ] The user has full control of their interaction with the project and at no point needs to “fight” it.	
- [ ] The site avoids aggressive automatic pop-ups and autoplay of audio; instead of allowing the user to initiate such actions.	
- [ ] All input elements are clearly labelled, and provide placeholders and default values whenever relevant.	
- [ ] The project follows common and consistent UI/UX conventions - there are plenty of online resources you can take inspiration from, such as GoodUI.

### Information Architecture

- [ ] All information displayed on the site is presented in an organised fashion with each piece of information being easy to find and none feeling out of place.	
- [ ] Headers are used to convey structure - each section has a header that’s easy to see and clear to understand.	
- [ ] The written language used on your sites is straightforward for the user to follow.	
- [ ] Whenever relevant, the site provides interactivity to make the information easier to consume.

### Defensive Design

- [ ] A customer is not be able to break the site by clicking buttons out of the expected order or by providing any unexpected inputs.	
- [ ] All forms intelligently handle empty or invalid input fields.	
- [ ] Navigating between pages via the back/forward buttons can never break the site.	
- [ ] This includes unexpected actions such as navigating back to the login page after already being logged in.	
- [ ] User actions should not cause internal errors in the console	
- [ ] Clear feedback to the user is given for any action disallowed by the developer.

## Layout and Visual Impact

### Responsive Design

- [ ] All page elements look well on screens as small as 360 pixels wide and as big as 3840 pixels wide (4K).	
- [ ] The site uses Bootstrap grid sizes or CSS3 media queries to ensure the layout changes appropriately and reflows when the screen is resized.
- [ ] ### Image Presentation
- [ ] Graphics are consistent in style and colour.	
- [ ] The background never distracts from the foreground information.	
- [ ] All kinds of multimedia content used in the project work well on the different popular browsers.	
- [ ] Whenever needed, multiple alternative file types are used.	
- [ ] Images always maintain their original aspect ratio when the screen is resized (crop don’t stretch).	
- [ ] All images are of sufficient resolution to not appear pixelated.	
- [ ] Image files are not bigger than is needed - full-screen images are under 3MB, while smaller images are <500kB.	
- [ ] If any larger files are being loaded, there is a progress indicator.	
For large video/audio resources, prefer an external hosting platform (e.g., YouTube, S3….)
- [ ] Graphics are consistent in style and colour.	
- [ ] The background never distracts from the foreground information.	
- [ ] All kinds of multimedia content used in the project work well on the different popular browsers.	
- [ ] Whenever needed, multiple alternative file types are used.	
- [ ] Images always maintain their original aspect ratio when the screen is resized (crop don’t stretch).	
- [ ] All images are of sufficient resolution to not appear pixelated.	
- [ ] Image files are not bigger than is needed - full-screen images are under 3MB, while smaller images are <500kB.	
- [ ] If any larger files are being loaded, there is a progress indicator.	
- [ ] For large video/audio resources, prefer an external hosting platform (e.g., YouTube, S3….)
- [ ] There is sufficient contrast between background and foreground colors.	
- [ ] The color scheme used on the site consists of a palette of colors that work well together.	
- [ ] The typefaces used complement one another.	
- [ ] All text is legible; particular attention to legibility is maintained when text formatting effects are in use.	
- [ ] Text is never obscured by images or colors.

### Appropriate use of HTML5

- [ ] Your HTML passes through the official validator with no issues.	
- [ ] Semantic HTML5 elements are used whenever this makes sense.	
- [ ] All non-text elements have a text equivalent for the visually impaired (e.g. alt attributes in img elements).	
- [ ] Code is indented in a consistent manner to ease readability.

### Appropriate use of CSS3

- [ ] Your project includes sufficient custom written CSS code to demonstrate your proficiency in the language.	
- [ ] Your CSS passes through the official (Jigsaw) validator with no issues.	
- [ ] Your CSS is split/indented into well-defined and commented sections.	
- [ ] CSS code is kept in external file(s) that are linked to in the HTML file’s head element.	
- [ ] CSS classes are used effectively and there is no unnecessary duplication of properties.	
- [ ] Code is indented in a consistent manner to ease readability.

### Appropriate use of code

- [ ] There is no unneeded complexity, as well as no commented-out code.	
- [ ] Code is indented in a consistent manner to ease readability.	
- [ ] Functions are used for reuse of identical/similar code sections to encapsulate implementation detail and promote abstraction.

## Software Development Practices

### Directory Structure and File Naming

- [ ] Your project’s files are named clearly and consistently, and located in appropriately named directories.	
- [ ] Whenever relevant, files are grouped in directories by file type (e.g., a static directory will contain all static files and may be organized into sub-directories such as CSS, images, etc.)	
- [ ] There is a clear separation between your files and any external files (for example, library files are all inside a directory named 'libraries').	
- [ ] File names are descriptive and consistent. For cross-platform compatibility, file and directory names shouldn’t have spaces in them and should be lower-case only.

### Version Control

- [ ] Your code is managed in git, with a separate well-named commit for each feature/fix.	
- [ ] You avoid very large commits, because this makes it harder to understand your development process and may lead the assessor to suspect plagiarism.
- [ ] Testing implementation
- [ ] Testing implementation

### Testing write-up

- [ ] Your testing (both manual and automated) is well documented either in the README or a separate file.	
- [ ] Your write-up discusses any interesting bugs found and their fixes.	
- [ ] Your write-up mentions and explains any bugs that were left unfixed.

### Readme file

- [ ] The project includes a readme file named README.md which is intended as an introduction for other developers who would like to use and contribute to this project. Note that submitting a project without a readme is an immediate fail.	
- [ ] The readme file describes the project's components, the technologies used and any other important details.	
- [ ] The readme is well-structured and easy to follow.	
- [ ] Your readme file is written in markdown and uses markdown formatting consistently and effectively.	
- [ ] The readme describes the project’s purpose, components, technologies, and all other important details.

### Comments

- [ ] All code files include clear and useful comments, wherever they are relevant.	
- [ ] Consider your intent, the reasoning and any trade-offs behind your code.	
- [ ] Your comments explain the “why” rather than the “what”.

### Deployment implementation

- [ ] Your site is deployed online on Github Pages, Heroku or any other system with full functionality.	
- [ ] The deployed version is identical to the development version except as explicitly mentioned in the deployment section in the documentation

### Deployment write-up

- [ ] The deployment procedure is fully documented in a section in the readme file.	
- [ ] Any differences between the development code and deployed code are fully explained.
