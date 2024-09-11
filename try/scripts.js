document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab-menu a');
    tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            e.preventDefault();
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
        });
    });
});
