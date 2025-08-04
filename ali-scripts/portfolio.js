// Ali's Portfolio JavaScript - Unique Implementation
document.addEventListener('DOMContentLoaded', function() {
    console.log('Ali Portfolio loaded successfully');
    
    // Custom page functionality
    const aliMobileTrigger = document.querySelector('.ali-mobile-trigger');
    const aliMenuList = document.querySelector('.ali-menu-list');
    
    if (aliMobileTrigger && aliMenuList) {
        aliMobileTrigger.addEventListener('click', function() {
            aliMenuList.classList.toggle('ali-mobile-visible');
        });
    }
    
    // Custom scroll effect for header
    let lastScrollTop = 0;
    const aliHeader = document.querySelector('.ali-main-header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            aliHeader.style.transform = 'translateY(-100%)';
        } else {
            aliHeader.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
});
