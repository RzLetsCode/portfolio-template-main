# EmailJS Contact Form Setup Guide

## Overview

This guide explains how to set up and configure the **EmailJS-powered contact form** integrated into `modern-redesign.html`. The contact form features a glassmorphism design with neon cyan borders, form validation, success/error messages, and automated email delivery.

## Live Demo

**URL**: https://rzletscode.github.io/portfolio-template-main/modern-redesign.html#contact

## Features

✅ **Glassmorphism Design** - Modern dark theme with blur effects
✅ **Neon Cyan Border** - Eye-catching border with glow effect
✅ **EmailJS Integration** - Direct email sending without backend
✅ **Form Validation** - Email format & required fields checking
✅ **Success/Error States** - User feedback with icons
✅ **Sending State** - Button feedback during submission
✅ **Responsive Design** - Mobile-friendly layout
✅ **Code2Career Branding** - Logo & tagline included

## Form Fields

1. **Full Name** - Text input (required)
2. **Email Address** - Email input (required, must be valid)
3. **Requirement / Comment** - Textarea (required, 5 rows)

## Setup Instructions

### 1. Create EmailJS Account

1. Visit [EmailJS.com](https://www.emailjs.com/)
2. Click **Sign Up** and create a free account
3. Verify your email address

### 2. Set Up Email Service

1. Go to **Dashboard → Email Services**
2. Click **Add Service** → Choose **Gmail** (or your email provider)
3. Click **Connect Account** and authenticate with your Gmail
4. Copy your **Service ID** (looks like `service_xxxxxx`)

### 3. Create Email Template

1. Go to **Dashboard → Email Templates**
2. Click **Create New Template**
3. Fill in the template:
   - **Template Name**: `portfolio_contact`
   - **From Email**: `{{from_email}}`
   - **From Name**: `{{from_name}}`
   - **Subject**: `New Contact Form Submission from Code2Career_AI`
   - **Content**:
     ```
     Name: {{from_name}}
     Email: {{from_email}}
     Message:
     {{message}}
     
     ---
     This email was sent via the Code2Career_AI contact form.
     Reply directly to {{from_email}}
     ```
4. **Recipients**: Add your receiving email in the form
   - Click **Add Dynamic Parameter** → `to_email` → `{{to_email}}`
   - Set default value to `PERSONALMYMAIL@GMAIL.COM`
5. Click **Save**
6. Copy your **Template ID** (looks like `template_xxxxxx`)

### 4. Get Your Public Key

1. Go to **Account → API Keys**
2. Copy your **Public Key** (looks like `xxxxxxxxxxxxxxxxxxxxxx`)

### 5. Update modern-redesign.html

Find the EmailJS initialization script (around line 332) and replace:

```javascript
emailjs.init("YOUR_PUBLIC_KEY");
```

With your actual Public Key:

```javascript
emailjs.init("abc123def456ghi789");
```

Find the form submission handler (around line 368) and replace:

```javascript
const serviceID = 'YOUR_SERVICE_ID';   // from EmailJS dashboard
const templateID = 'YOUR_TEMPLATE_ID'; // from EmailJS dashboard
```

With your actual IDs:

```javascript
const serviceID = 'service_xxxxxx';
const templateID = 'template_xxxxxx';
```

### 6. Commit & Deploy

```bash
git add modern-redesign.html
git commit -m "chore: Update EmailJS credentials"
git push origin main
```

GitHub Pages will automatically rebuild and deploy your changes.

## Form Validation

The form includes built-in validation:

- ✓ All fields required
- ✓ Email format validation (`name@domain.com`)
- ✓ Clear error messages for invalid input
- ✓ Success confirmation with checkmark icon

## Error Handling

### Common Issues

**Issue**: "Something went wrong while sending your message"
- Check that Service ID, Template ID, and Public Key are correct
- Verify your email service is connected in EmailJS dashboard
- Check browser console (F12) for detailed error messages

**Issue**: Emails not being received
- Verify template was created correctly
- Check spam/promotions folder in email
- Ensure "to_email" parameter has correct default value
- Test with EmailJS template editor first

## Security Notes

⚠️ **Important**: Your Public Key is intentionally exposed (it's public by design). Never expose your Private Key.

- The contact form only sends emails; it cannot access other data
- No data is stored in the HTML - submissions go directly to your email
- HTTPS recommended for production (GitHub Pages provides this)

## Testing

1. Open the contact form on your site
2. Fill in test data:
   - Full Name: "Test User"
   - Email: your test email
   - Message: "Test submission"
3. Click "Send Message"
4. Check for:
   - Button changes to "Sending..."
   - Success message appears
   - Email arrives in inbox within 30 seconds

## Customization

### Change Recipient Email

Modify line in template `to_email` parameter default value or update in the JavaScript:

```javascript
to_email: 'your-new-email@gmail.com',
```

### Modify Form Fields

Edit the HTML in `modern-redesign.html` section `id="contact"` to add/remove fields. Ensure you add corresponding variables in the EmailJS template.

### Update Styling

Edit the Tailwind classes in the contact section for colors, borders, or spacing. Key classes:
- `border-neon-blue/70` - Border color
- `from-neon-blue via-sky-500 to-neon-purple` - Button gradient
- `bg-black/20` - Section background

## Resources

- **EmailJS Documentation**: https://www.emailjs.com/docs/
- **Template Variables**: https://www.emailjs.com/docs/tutorial/creating-email-template/
- **Troubleshooting**: https://www.emailjs.com/docs/faq/

## Support

For issues:
1. Check browser console (F12 → Console tab)
2. Review EmailJS dashboard for service status
3. Test with EmailJS template editor
4. Check email spam folder

---

**Last Updated**: January 30, 2026  
**Contact Form Status**: ✅ Live & Deployed
