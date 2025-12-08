# LibraryProject 
Initial Django project setup for the ALX Django LearnLab.
This is my first Django project created for the ALX Django Learning Lab.

# LibraryProject Permissions Setup

## Groups & Permissions

### Groups
- **Viewers**: Can view books only (`can_view`)
- **Editors**: Can create and edit books (`can_create`, `can_edit`)
- **Admins**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`)

### Testing
1. Create users and assign them to the appropriate group.
2. Log in and test that access is enforced according to group permissions.



## Security Measures Implemented

1. CSRF Protection
   - All forms use {% csrf_token %} to prevent cross-site request forgery.
2. Content Security Policy (CSP)
   - Middleware adds CSP header to block scripts/styles/images from untrusted sources.
3. XSS and Clickjacking Protection
   - SECURE_BROWSER_XSS_FILTER=True
   - X_FRAME_OPTIONS='DENY'
   - SECURE_CONTENT_TYPE_NOSNIFF=True
4. Secure Cookies
   - CSRF_COOKIE_SECURE=True
   - SESSION_COOKIE_SECURE=True
5. Safe Data Access
   - All queries use Django ORM.
   - User inputs are validated using Django forms to prevent SQL injection.


## HTTPS Deployment Notes

- In production, the site should be served via HTTPS using SSL/TLS certificates.
- Example Nginx configuration (for deployment):




