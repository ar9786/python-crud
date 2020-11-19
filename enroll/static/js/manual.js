$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
    $('[data-toggle="popover"]').popover();
});
/* smooth scroll starts here */
$(document).ready( function(){
  $('.hashscroll').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
           if (target.length) {
            $('html, body').animate({
              scrollTop: target.offset().top -100
            }, 1000);
            return false;
          }
      }
  });
});
/* smooth scroll starts here */

$(document).on('click', '.trigger_aside', function(event) {
  event.preventDefault();
  $("body").toggleClass('bodyshrink');
});