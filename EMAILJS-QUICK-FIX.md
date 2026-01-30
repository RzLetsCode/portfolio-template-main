# ⚡ EmailJS Quick Fix Guide - Contact Form Error "Something went wrong"

## 🔴 Problem

You're seeing this error message in your contact form:
```
Something went wrong while sending your message. Please try again.
```

**Root Cause**: Your EmailJS credentials (Public Key, Service ID, or Template ID) are still **placeholder values** and haven't been replaced with your actual EmailJS account details.

---

## ✅ Solution (5 Minutes)

### Step 1: Create EmailJS Account (2 min)

1. Go to **https://www.emailjs.com/**
2. Click **"Sign Up Free"**
3. Create account with your email
4. Verify email address

### Step 2: Connect Your Email Service (2 min)

1. Login to [EmailJS Dashboard](https://dashboard.emailjs.com/admin)
2. Click **"Email Services"** in left sidebar
3. Click **"Add Service"**
4. Select **"Gmail"** (or your email provider)
5. Click **"Connect Account"**
6. Select your Gmail account
7. Click **"Allow"** for permissions
8. Click **"Create"**
9. **📋 Copy and save your SERVICE ID** (looks like `service_xxxxxx`)

### Step 3: Create Email Template (1 min)

1. Click **"Email Templates"** in left sidebar
2. Click **"Create New Template"**
3. Fill in:
   - **Template Name**: `portfolio_contact`
   - **Subject**: `New Contact Form Submission from Code2Career_AI`
4. Click **"Code Editor"** button
5. Replace template content with:
   ```
   Name: {{from_name}}
   Email: {{from_email}}
   Message:
   {{message}}
   
   ---
   Reply to: {{from_email}}
   ```
6. Click **"Save"**
7. **📋 Copy and save your TEMPLATE ID** (looks like `template_xxxxxx`)

### Step 4: Get Your Public Key

1. Click **"Account"** (or your profile icon) → **"API Keys"**
2. **📋 Copy and save your PUBLIC KEY** (long string of characters)

### Step 5: Update Your HTML File

Go to: `modern-redesign.html`

**Find Line 337** (around the EmailJS section):
```javascript
emailjs.init("YOUR_PUBLIC_KEY");
```

**Replace with your actual public key:**
```javascript
emailjs.init("your_actual_public_key_here");
```

**Find Line 368** (in the form handler):
```javascript
const serviceID = 'YOUR_SERVICE_ID';   // from EmailJS dashboard
const templateID = 'YOUR_TEMPLATE_ID'; // from EmailJS dashboard
```

**Replace with your actual IDs:**
```javascript
const serviceID = 'service_abc123def456';   // YOUR actual service ID
const templateID = 'template_xyz789uvw456'; // YOUR actual template ID
```

### Step 6: Save & Deploy

1. Commit your changes to GitHub:
   ```bash
   git add modern-redesign.html
   git commit -m "Update EmailJS credentials"
   git push origin main
   ```

2. Wait 30-60 seconds for GitHub Pages to deploy

3. **Test the contact form** at: https://rzletscode.github.io/portfolio-template-main/modern-redesign.html#contact

---

## 🐛 Still Getting Error?

### Check These:

1. **Did you replace placeholders?**
   - Open browser DevTools (F12)
   - Go to **Console** tab
   - Fill form and submit
   - Look for error messages

2. **Wrong credentials?**
   - Triple-check your Service ID and Template ID
   - Make sure Public Key is correct
   - No extra quotes or spaces

3. **Email not connected in EmailJS?**
   - Go to Email Services
   - Click on your Gmail service
   - Verify it says "Connected"
   - If not, click "Test" first

4. **Template not set up correctly?**
   - Go to Email Templates
   - Click your template
   - Verify template has the email variables
   - Make sure "Save" was clicked

5. **Check browser console for exact error:**
   - Open F12 (DevTools)
   - Go to **Console** tab
   - Submit form
   - Copy any error messages
   - Paste in EmailJS dashboard → Help

---

## 📋 Checklist Before Testing

- [ ] EmailJS account created
- [ ] Gmail service added & connected
- [ ] Email template created
- [ ] Public Key copied
- [ ] Service ID copied
- [ ] Template ID copied
- [ ] Line 337 updated with Public Key
- [ ] Line 368 updated with Service & Template IDs
- [ ] File committed to GitHub
- [ ] Waited 1 minute for deploy
- [ ] Cleared browser cache (Ctrl+Shift+Del)

---

## 💡 Pro Tips

1. **Use Browser Console**: Open F12 and check console for exact errors
2. **Test in EmailJS Dashboard First**: Go to Email Templates → click your template → "Test" button
3. **Check Spam Folder**: If emails not arriving, check Promotions/Spam in Gmail
4. **No spaces or typos**: Copy-paste credentials, don't type manually
5. **Clear cache**: Press Ctrl+Shift+Del after making changes

---

## 🆘 Still Stuck?

**Check the full setup guide**: [CONTACT-SETUP-GUIDE.md](./CONTACT-SETUP-GUIDE.md)

**EmailJS Official Docs**: https://www.emailjs.com/docs/

---

**Updated**: January 30, 2026
