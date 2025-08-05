// AZBN Portfolio JavaScript - Citation Safe
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 AZBN Portfolio loaded - Dual deployment active');
    
    // Smooth scrolling for navigation links
    const azbnLinks = document.querySelectorAll('.azbn-link');
    
    azbnLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Header scroll effect
    const azbnHeader = document.querySelector('.azbn-header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            azbnHeader.style.background = 'rgba(255, 255, 255, 0.98)';
        } else {
            azbnHeader.style.background = 'rgba(255, 255, 255, 0.95)';
        }
    });
    
    // Active navigation highlighting
    const sections = document.querySelectorAll('section[id^="azbn-"]');
    
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            
            if (scrollY >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        azbnLinks.forEach(link => {
            link.classList.remove('azbn-active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('azbn-active');
            }
        });
    });
    
    // Deployment status animation
    const deploymentStatus = document.querySelector('.azbn-deployment-status');
    if (deploymentStatus) {
        setTimeout(() => {
            deploymentStatus.style.animation = 'pulse 2s infinite';
        }, 2000);
    }
});

// CSS animation for deployment status
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
`;
document.head.appendChild(style);
