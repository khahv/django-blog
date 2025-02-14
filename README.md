# Django Blog with Interactive Linux Lab  

This is an open-source blog platform built with **Django (Python)**, designed for content creation and hands-on learning. The website allows **admins and editors** to write and manage articles, while also providing an interactive **noVNC-powered Linux lab** for online lessons.  

## Features  
- ✅ **Content Management**: Admins and editors can create, edit, and publish blog posts.  
- ✅ **User Roles**: Role-based access control for different levels of content management.  
- ✅ **Interactive Linux Lab**: Integrated **noVNC** to connect to Linux servers, allowing users to practice directly in their browsers.  
- ✅ **Cloud Integration**: Easily deployable on cloud platforms.  
- ✅ **Modern UI**: Responsive and user-friendly interface.  

## Getting Started  

### Prerequisites  
Make sure you have **Python 3.x** and **pip** installed.  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/khahv/django-blog
   cd django-blog

2. Install dependencies and run the server:
    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
