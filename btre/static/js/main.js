const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Create a fadeout for messages
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);