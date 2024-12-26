 document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Get form data
    const form = e.target;
    const formData = new FormData(form);

    // Submit form data to Google Apps Script
    fetch('https://script.google.com/macros/s/AKfycbzlw2MBr5aCh7OWLQx3vsC-2pMAUE0qw7Io0EwYtjQAEwccrPEULZG60V9Fm0oDzFgDQw/exec', {
      method: 'POST',
      body: formData
    })
      .then((response) => {
        if (response.ok) {
          // Show success message
          document.getElementById('successMessage').style.display = 'block';

          // Clear form fields
          form.reset();
        } else {
          alert('There was an error submitting your form. Please try again.');
        }
      })
      .catch((error) => {
        alert('Network error. Please check your internet connection and try again.');
        console.error('Error:', error);
      });
  });