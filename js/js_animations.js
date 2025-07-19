// Scroll-triggered fade-in animation for sections
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top < window.innerHeight &&
    rect.bottom > 0
  );
}

document.addEventListener('scroll', function() {
  document.querySelectorAll('section').forEach(section => {
    if (isInViewport(section)) {
      section.classList.add('fade-in');
    }
  });
});

// Optional: Add CSS for .fade-in in your components.css
// .fade-in { animation: fadeInUp 1s; opacity: 1 !important; }