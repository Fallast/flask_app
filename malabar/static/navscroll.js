function close_drops(){
   $(".dropdown-toggle").each(function(){
      if($(this).attr('aria-expanded') === 'true')
         $(this).dropdown('toggle');
   });
}

document.addEventListener("DOMContentLoaded", function(){

   var path = window.location.pathname;
   var page = path.split("/").pop();
   el_autohide = document.querySelector('.autohide');

   if(el_autohide && page == "home"){
      var last_scroll_top = 0;
      window.addEventListener('scroll', function() {
         let scroll_top = window.scrollY;
         if(scroll_top < last_scroll_top) {
            el_autohide.classList.remove('scrolled-down');
            el_autohide.classList.add('scrolled-up');
         }
         else {
            el_autohide.classList.remove('scrolled-up');
            el_autohide.classList.add('scrolled-down');
            close_drops();
         }
         last_scroll_top = scroll_top;
      }); 
   }
}); 
