$(document).ready(function(){
  var searchBarTop = $(".main-search")[0].getBoundingClientRect().top;
  var searchBtnBottom = $(".search-button")[0].getBoundingClientRect().bottom;

  $(window).scroll(function(){
    var scrollPos= $(this).scrollTop();

    //Fades IN the first text line and image

    if(scrollPos >= 0){
      $(".desc-text-1").css({"opacity":"1"});
    }
    if(scrollPos >= 50){
      $(".desc-image-1").css({"opacity":"1"});
    }

    //Fades IN the second text line and image

    if(scrollPos >= searchBarTop){
      $(".desc-text-2").css({"opacity":"1"});
    }
    if(scrollPos >= searchBarTop+50){
      $(".desc-image-2").css({"opacity":"1"});
    }

    //Fades IN the third text line and image

    if(scrollPos >= searchBtnBottom){
      $(".desc-text-3").css({"opacity":"1"});
    }
    if(scrollPos >= searchBtnBottom+50){
      $(".desc-image-3").css({"opacity":"1"});
    }

    //Fades OUT the first text line and image

    if(scrollPos <= 10){
      $(".desc-text-1").css({"opacity":"0"});
    }
    if(scrollPos <= 60){
      $(".desc-image-1").css({"opacity":"0"});
    }

    //Fades OUT the second text line and image

    if(scrollPos <= searchBarTop){
      $(".desc-text-2").css({"opacity":"0"});
    }
    if(scrollPos <= searchBarTop+50){
      $(".desc-image-2").css({"opacity":"0"});
    }

    //Fades OUT the second text line and image

    if(scrollPos <= searchBtnBottom){
      $(".desc-text-3").css({"opacity":"0"});
    }
    if(scrollPos <= searchBtnBottom+50){
      $(".desc-image-3").css({"opacity":"0"});
    }


  });
});
