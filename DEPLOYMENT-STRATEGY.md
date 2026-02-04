# Dual-Site Deployment Strategy: RzLetsCode Portfolio + Code2Career_AI

## Architecture Overview

This repository uses a **monorepo approach** with dedicated directories for each site:

```
portfolio-template-main/
├── portfolio/                 # Personal Portfolio (Industry Expert)
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── css/
│   │   ├── main.css
│   │   └── theme-dark.css
│   └── assets/
├── code2career/              # Code2Career_AI (EdTech Platform)
│   ├── index.html
│   ├── courses.html
│   ├── about.html
│   ├── css/
│   │   ├── brand.css
│   │   └── components.css
│   └── assets/
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions for dual deployment
└── README.md
```

## Deployment URLs

### Personal Portfolio
- **URL**: `https://rzletscode.github.io/portfolio-template-main/portfolio/`
- **Purpose**: Professional resume, technical skills, projects showcase
- **Design**: Dark mode, minimalist, enterprise-grade
- **Target Audience**: Recruiters, Tech Leads, Hiring Managers

### Code2Career_AI
- **URL**: `https://rzletscode.github.io/portfolio-template-main/code2career/`
- **Purpose**: EdTech platform, course listings, brand presence
- **Design**: Modern, vibrant, future-forward (deep blue + teal)
- **Target Audience**: Students, Professionals, Learners

## Git Strategy

### Branch Structure

```bash
# Main branches
main                          # Production (deploys both sites)
feature/portfolio-redesign   # Personal portfolio improvements
feature/code2career-redesign # Code2Career platform improvements

# Feature branches follow naming convention
feature/{site}/{feature-name}
```

### Recommended Git Commands

```bash
# Clone repository
git clone https://github.com/RzLetsCode/portfolio-template-main.git
cd portfolio-template-main

# Create feature branch for portfolio
git checkout -b feature/portfolio/dark-theme-upgrade

# Make changes to portfolio/ directory
# Commit with descriptive message
git commit -m "refactor(portfolio): Implement dark theme with enhanced typography"

# Create feature branch for Code2Career
git checkout -b feature/code2career/hero-section-redesign

# Make changes to code2career/ directory
git commit -m "feat(code2career): Create premium hero section with gradient backdrop"

# Push and create pull request
git push origin feature/code2career/hero-section-redesign
```

## GitHub Actions Deployment

The `.github/workflows/deploy.yml` automatically:

1. **Detects Changes**: Identifies which site directory was modified
2. **Builds Site**: Prepares static assets
3. **Deploys to GitHub Pages**: Publishes to correct subdirectory
4. **Maintains Isolation**: Ensures sites don't overwrite each other

### How It Works

```yaml
# On push to main:
# 1. Portfolio changes → Deploy to /portfolio/
# 2. Code2Career changes → Deploy to /code2career/
# 3. Both → Deploy both
```

## Local Development

### Setup

```bash
# Clone repo
git clone https://github.com/RzLetsCode/portfolio-template-main.git

# Create local directories
mkdir -p portfolio code2career

# Test Portfolio locally
cd portfolio
python -m http.server 8000
# Visit http://localhost:8000

# In another terminal, test Code2Career
cd code2career
python -m http.server 8001
# Visit http://localhost:8001
```

### Live Reload (Optional)

Use a tool like `live-server` for hot reloading:

```bash
npm install -g live-server

cd portfolio
live-server
```

## Design Philosophy

### Personal Portfolio
- **Color Scheme**: Deep dark backgrounds (#0f1419), silver accents (#e0e0e0)
- **Typography**: Inter, Roboto (sans-serif, clean)
- **Spacing**: Generous whitespace, 16px base
- **Components**: Card-based, glassmorphism effects
- **Focus**: Code quality, architectural knowledge, enterprise experience

### Code2Career_AI
- **Color Scheme**: Deep blue (#1a365d), teal accents (#14b8a6), gradient overlays
- **Typography**: Poppins, Inter (modern, friendly)
- **Spacing**: Balanced, 18px base
- **Components**: Gradient headers, feature cards, call-to-action sections
- **Focus**: Learning path, community, transformation

## Continuous Integration Checklist

- [ ] Changes committed to correct site directory
- [ ] CSS follows BEM naming convention
- [ ] HTML is semantic and accessible (a11y)
- [ ] Images optimized (<100KB each)
- [ ] Mobile responsive (tested on 320px, 768px, 1920px)
- [ ] Performance lighthouse score >80
- [ ] No console errors or warnings

## Troubleshooting

### Both Sites Not Deploying

```bash
# Check GitHub Actions logs
# Settings > Actions > Workflows > Deploy

# Common issues:
# - Files not in correct directory
# - YAML syntax errors in deploy.yml
# - Branch push not to 'main'
```

### Portfolio/Code2Career Overwriting Each Other

```bash
# Ensure .gitignore is correct:
echo "# Build outputs" >> .gitignore
echo "/dist/" >> .gitignore
echo "node_modules/" >> .gitignore
```

### Testing Before Merge

```bash
# Create local test build
git checkout feature/your-feature

# Build and test
cd portfolio (or code2career)
open index.html

# Verify no breaking changes
```

## Future Enhancements

1. **Custom Domain**: Point both sites to subdomains (portfolio.yoursite.com, code2career.yoursite.com)
2. **CDN Integration**: Use Cloudflare for faster global delivery
3. **Analytics**: Add Google Analytics tracking per site
4. **Dynamic Content**: Integrate CMS for blog updates
5. **Newsletter**: Add email signup functionality to both

## Contact & Support

- **GitHub**: [RzLetsCode](https://github.com/RzLetsCode)
- **Issues**: [Portfolio-Template-Main Issues](https://github.com/RzLetsCode/portfolio-template-main/issues)

---

**Last Updated**: February 4, 2026
**Status**: Active Development
**Version**: 2.0.0
