$(function() {
  $(".customer").on("click", function(){

    function customerDetailSuccess(json) {
      $("#customer-details").html("");
      $("#customer-details").html("<ul><li>Age: "+json.age+"</li><li>Sex: "+json.sex+"</li></ul>");
    }

    function customerDetailFailure() {
      console.log("OH MY GOD");
    }

    var customerId = $(this).attr("data-customer-id");
    $.ajax({
      url: "/customers/" + customerId,
      datatype:"application/json",
      method: "GET",
      success: customerDetailSuccess,
      error: customerDetailFailure
    });
  });
});
