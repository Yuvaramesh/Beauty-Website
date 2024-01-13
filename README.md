### Beauty Website using Flask Framework

## Flask:


**The Flask is the web framework to develop the web application using python language.
The flask is working on the two things they are WSGI and Jinja 2 templates**

**WSGI - Web Server Gateway Interface 
=>GET
=>POST**

### Jinja 2 Template :

Its a Expression {{ some exp }} and conditional statements {% condition %}
We have used in this project

**Database:SqlAlchemy ==> Sqlite3
SqlAlchemy class => sqlite3 db => Bootstrap => HTML**

It looks like you've shared HTML code for a webpage, specifically a Django template. This template seems to define a webpage for a beauty-related service, possibly a salon or beauty studio, with sections for different beauty professionals like a Hair Stylist, Makeup Artist, and Henna Artist.

1. **HTML Structure:**
   - Ensure that your HTML structure is correct. Every opening tag should have a corresponding closing tag.

2. **CSS Styling:**
   - You have used inline styles (e.g., `style="width:100px;height:100vh"`) and inline styling with the `style` attribute is generally discouraged. Consider using an external stylesheet for better separation of concerns.

3. **Image Sources:**
   - Make sure to replace the placeholder image URLs with actual image URLs that you have permission to use.

4. **Linking to Other Pages:**
   - You have links to "/items" and "/book" but the corresponding views or routes need to be defined in your Django application for these links to work.

5. **Data Representation:**
   - You're representing a Hair Stylist, Makeup Artist, and Henna Artist with their respective names, experiences, and contact numbers. Ensure that this data is dynamic and can be populated from a backend source.

6. **Consistency:**
   - Ensure consistency in styling across different sections to provide a cohesive look and feel.

7. **Accessibility:**
   - Consider adding appropriate alt text to your images for accessibility.

8. **Optimization:**
   - Optimize your images for web to improve page loading speed.

Remember to integrate this HTML template with your Django project, define the necessary views and URL patterns, and handle data dynamically through Django's templating engine.
