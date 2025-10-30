# PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (Beginner plan or higher for external database access)
- PostgreSQL database (if using external DB)

## Step-by-Step Deployment

### 1. Upload Your Code
```bash
# In PythonAnywhere bash console
git clone https://github.com/yourusername/String-Analyzer-Service.git
# OR upload files via Files tab
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
cd String-Analyzer-Service
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements_pythonanywhere.txt
```

### 4. Configure Environment Variables
- Copy `.env.example` to `.env`
- Update with your actual values:
  - Replace `yourusername` with your PythonAnywhere username
  - Add your database credentials
  - Generate a new SECRET_KEY

### 5. Database Setup
```bash
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
```

### 6. Configure Web App in PythonAnywhere
1. Go to Web tab in PythonAnywhere dashboard
2. Create new web app (Python 3.10)
3. Set source code path: `/home/yourusername/String-Analyzer-Service`
4. Set WSGI file path: `/home/yourusername/String-Analyzer-Service/pythonanywhere_wsgi.py`

### 7. Static Files Configuration
In Web tab, add static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/String-Analyzer-Service/static/`

### 8. Update WSGI File
Edit `pythonanywhere_wsgi.py` and replace `yourusername` with your actual username.

### 9. Reload Web App
Click "Reload" button in Web tab.

## Testing
Visit `https://yourusername.pythonanywhere.com/string-analyzer/list/` to test your API.

## Troubleshooting
- Check error logs in Web tab
- Ensure all paths use your actual username
- Verify database connection settings
- Check ALLOWED_HOSTS in settings.py