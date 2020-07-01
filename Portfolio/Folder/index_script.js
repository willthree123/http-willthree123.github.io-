$(document).on("scroll", function() {
    var pageTop = $(document).scrollTop();
    var pageBottom = pageTop + $(window).height();

    var tags = $(".Index_whole");
    for (var i = 0; i < tags.length; i++) {
      var tag = tags[i];
      if ($(tag).position().top < pageBottom) {
        $(tag).addClass("visible");
      } 
      else {
        $(tag).removeClass("visible");
      }
    }

    var tags = $(".ICP_whole");
    for (var i = 0; i < tags.length; i++) {
        var tag = tags[i];
        if ($(tag).position().top < pageBottom) {
          $(tag).addClass("visible");
        } 
        else {
          $(tag).removeClass("visible");
        }
      }
      
      var tags = $(".IBP_whole");
      for (var i = 0; i < tags.length; i++) {
        var tag = tags[i];
        if ($(tag).position().top < pageBottom) {
          $(tag).addClass("visible");
        } 
        else {
          $(tag).removeClass("visible");
        }
      }
  });




