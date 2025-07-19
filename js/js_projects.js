// Expand project card (modal or accordion effect)
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('click', function() {
      this.classList.toggle('expanded');
      // Optionally show more details, tabs, etc.
    });
  });
});

// Example: Tabbed interface for project details (if you use tabs)
document.querySelectorAll('.tabs .tab').forEach(tab => {
  tab.addEventListener('click', function() {
    document.querySelectorAll('.tabs .tab').forEach(t => t.classList.remove('tab-active'));
    this.classList.add('tab-active');
    const target = this.getAttribute('data-target');
    document.querySelectorAll('.tab-content').forEach(content => {
      content.style.display = content.id === target ? 'block' : 'none';
    });
  });
});

// Example: Chart.js visualization (if you use Chart.js)
if (document.getElementById('myChart')) {
  const ctx = document.getElementById('myChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['GDP', 'Inflation'],
      datasets: [{
        label: 'Iran',
        data: [5.2, 3.8],
        backgroundColor: ['#667eea', '#764ba2']
      }]
    }
  });
}