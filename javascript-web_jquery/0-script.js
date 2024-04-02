// This script replaces the header element to Red.
document.addEventListener('DOMContentLoaded', function () {
    var headerElement = document.querySelector('header');
    if (headerElement) {
      headerElement.style.color = '#FF0000';
    }
  });
