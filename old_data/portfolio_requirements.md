# Portfolio Website Development Requirements

## Project Overview

**Goal:** Transform Alireza Barzin Zanganeh's single-file portfolio website into a professional, multi-file structure optimized for GitHub and Hostinger deployment.

**Profile:** Economics graduate with Econometrics emphasis, transitioning from Senior QA Automation Engineer (7+ years Python) to Data Science/ML Engineering roles.

## Current State Analysis

### Existing Website
- **Structure:** Single HTML file with inline CSS and JavaScript
- **Content:** Data Scientist/ML Engineer portfolio 
- **Sections:** Hero, About, Skills, Projects, Contact
- **Design:** Modern aesthetic with gradient backgrounds, glassmorphism effects, animations
- **Projects:** 6 project placeholders, first implementation: [data-science-portfolio](https://github.com/abzanganeh/data-science-portfolio.git)

## Requirements Specification

### 1. Professional Architecture
- [x] Separate HTML, CSS, and JavaScript files
- [x] Modular component structure
- [x] Clean separation of concerns
- [x] Scalable file organization

### 2. Enhanced Project Showcase
- [ ] **Interactive Project Cards** with expandable details
- [ ] **Tabbed Interface:** Overview | Visualizations | Code | Results
- [ ] **Syntax-highlighted code blocks** with copy functionality
- [ ] **Data visualizations** in responsive grid layouts
- [ ] **Performance metrics** and achievement indicators
- [ ] **Technology stack badges** and labels

### 3. Economics/Econometrics Emphasis
- [ ] **Economics Background Section** highlighting degree and domain expertise
- [ ] **Iran Economic Projects** as featured work (GDP forecasting, inflation prediction)
- [ ] **Methodology Comparison** between econometric and ML approaches
- [ ] **Time Series Analysis** demonstrations
- [ ] **Economic Domain Knowledge** integration throughout

### 4. Deployment Pipeline
- [ ] **Development:** Visual Studio Code setup
- [ ] **Version Control:** Git with conventional commits
- [ ] **GitHub:** Repository setup and documentation
- [ ] **Hostinger:** File manager deployment or FTP

## Technical Architecture

### File Structure
```
portfolio/
├── index.html                      # Main landing page
├── css/
│   ├── styles.css                 # Core styling
│   ├── components.css             # Component-specific styles  
│   └── responsive.css             # Media queries and mobile
├── js/
│   ├── main.js                    # General functionality
│   ├── projects.js                # Project interactions
│   └── animations.js              # Scroll effects and animations
├── projects/
│   ├── economics-models/          # Iran economic projects
│   │   ├── images/               # Economic visualizations
│   │   ├── code-snippets/        # Python/R econometric code
│   │   └── data/                 # Economic datasets and metrics
│   ├── data-science-portfolio/    # ML transition projects
│   │   ├── images/               # ML visualizations  
│   │   ├── code-snippets/        # Python ML code
│   │   └── data/                 # Project data and results
│   └── comparative-analysis/      # Economics vs ML studies
├── assets/
│   ├── images/                    # General site images
│   ├── icons/                     # UI icons and badges
│   └── documents/                 # Resume, papers, etc.
└── README.md                      # Project documentation
```

### Current Features to Preserve
- **Navigation:** Fixed header with smooth scrolling
- **Responsive Design:** Mobile-first approach
- **Animations:** CSS transitions and scroll effects  
- **Form Handling:** Contact form functionality
- **Modern Styling:** Gradient backgrounds, glassmorphism

### Enhanced Features to Implement
- **Project Expandability:** Modal or accordion-style details
- **Code Syntax Highlighting:** Prism.js or similar
- **Data Visualization:** Interactive charts and graphs
- **Performance Metrics:** Achievement showcases
- **Technology Badges:** Skill and tool indicators

## Development Phases

### Phase 1: Foundation Setup
- [x] Create professional file structure
- [x] Extract inline CSS and JavaScript from single file
- [x] Establish modular component architecture
- [x] Set up development environment

### Phase 2: Content Enhancement  
- [ ] Implement enhanced project display components
- [ ] Add economics background and Iran projects
- [ ] Create interactive project tabs and code displays
- [ ] Integrate data visualizations and metrics

### Phase 3: Economics Integration
- [ ] Highlight econometrics expertise and methodology
- [ ] Feature Iran economic modeling projects
- [ ] Create comparative analysis section (Econ vs ML)
- [ ] Add time series analysis demonstrations

### Phase 4: Deployment & Documentation
- [ ] Set up GitHub repository with proper documentation
- [ ] Configure Hostinger deployment pipeline  
- [ ] Implement CI/CD workflow
- [ ] Create comprehensive README and project docs

## Learning Objectives

### Technical Skills
- Modern file organization and separation of concerns
- Professional CSS architecture and component design
- JavaScript modularization and best practices
- Git workflow and deployment processes
- Responsive design implementation
- Code documentation and maintenance

### Career Development
- Portfolio optimization for Data Science roles
- Showcasing domain expertise (Economics/Econometrics)
- Demonstrating technical transition capabilities
- Professional web development practices
- Industry-standard deployment workflows

## Success Criteria

### Technical
- [x] Clean, maintainable code structure
- [ ] Responsive design across all devices
- [ ] Fast loading times and optimized performance
- [ ] Accessible and SEO-optimized content
- [ ] Professional deployment pipeline

### Career Impact
- [ ] Clear demonstration of Economics → Data Science transition
- [ ] Showcase of both domain expertise and technical skills
- [ ] Professional presentation suitable for job applications
- [ ] Interactive project demonstrations
- [ ] Comprehensive skill and experience documentation

## Timeline & Priorities

**Target Completion:** Aligned with January 2026 job search timeline

1. **Immediate (Current):** File structure and basic enhancement
2. **Short-term (1-2 weeks):** Economics content integration and project showcase
3. **Medium-term (1 month):** Advanced features and interactive components  
4. **Long-term (Ongoing):** Continuous updates with new projects and skills

## Notes

- Emphasize unique combination: Economics degree + Python expertise + QA background
- Position as domain expert transitioning to technical implementation
- Showcase both theoretical foundation and practical application
- Maintain professional standards suitable for senior-level positions