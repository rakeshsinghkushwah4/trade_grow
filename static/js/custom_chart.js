$( document ).ready(function() {
  $(".show_chart").on('click', function(){
    var value = $(this).attr('data-symbol')
    var url = $(this).attr('data-url')
    let container_id = document.getElementsByTagName("svg")[0]
    document.getElementById(container_id.id).id = "container"+value
    get_data(value, url)
    d3.select("#hello").remove()
  })
});

function get_data(symbol, url){
  $.ajax({
    type: "get",
    url: url,
    success: function(data){
      $.getScript("/static/js/candle_chart.js", function(){
        chart(data, symbol)
      })

    }
  })
}