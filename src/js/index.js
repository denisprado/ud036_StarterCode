import "../scss/style.scss";
import $ from "jquery";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";


// listen menu clicks and show respective itens by css classes
$(function() {
  //run when the DOM is ready
  $(".nav-link").click(function() {
    //use a class, since your ID gets mangled
    $(this).addClass("active"); //add the class to the clicked element
    var genreClass = $(this).attr('class').replace("nav-link","").replace("active","").replace(/ /g,"")
    var genreName = $(this).attr('class').replace("nav-link","").replace("active","")
    
    // showing the genre movies listed
    $("#showing").html("<span role='alert'>Showing <span class='text-primary'>" + genreName + "</span> movies</span>");
    if (genreClass=="All") {
      $(".movies__item").show();  
    } else{
      $('.movies__item').hide()
      $('.'+genreClass).show()
    }
  });
});


// Pause the video when the modal is closed
$(document).on("click", ".hanging-close, .modal-backdrop, .modal", function(
  event
) {
  // Remove the src so the player itself gets removed, as this is the only
  // reliable way to ensure the video stops playing in IE
  $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on("click", ".movie-tile", function(event) {
  var trailerYouTubeId = $(this).attr("data-trailer-youtube-id");
  var sourceUrl =
    "http://www.youtube.com/embed/" + trailerYouTubeId + "?autoplay=1&html5=1";
  $("#trailer-video-container")
    .empty()
    .append(
      $("<iframe></iframe>", {
        id: "trailer-video",
        type: "text-html",
        src: sourceUrl,
        frameborder: 0
      })
    );
});