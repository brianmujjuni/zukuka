
// function calculate all withdraws
$(function(){
    $(".form-withdraw").keyup(function(){
        
        
        let newBalance = 0
        let totalCharges = 0
        let charges = Number($(".charges").val())
        let olBalance = Number($(".oldBalance").val())
        let withdrawAmount = Number($(".withdrawAmount").val())
        totalCharges = charges + withdrawAmount
        newBalance = olBalance - totalCharges
        $(".newBalance").val(newBalance.toFixed(2))
        
       
    })
})
//function to calculate deposits

$(function(){
    $(".form-deposit").keyup(function(){
        let newBalance = 0
        let depositAmount = Number($(".depositAmount").val())
        let oldBalance = Number($(".oldBalance").val())
        newBalance = depositAmount + oldBalance
        $(".newBalance").val(newBalance.toFixed(2))
        

    })
})

$(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberAccountType/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.accountType').value = json.accountType;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  

  $(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberAccountName/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.accountName').value = json.accountName;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  $(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberAccountCurrency/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.accountCurrency').value = json.accountCurrency;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  $(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberAccountBalance/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.oldBalance').value = json.balance
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });


  $(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberNinNumber/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.ninNumber').value = json.ninNumber;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });



  $(document).ready(function() {
    $('.accountNo').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "memberContact/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.contact').value = json.phoneNo1;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  

  $(document).ready(function() {
    $('.accStand').change(function(){
        var query = $(this).val();
        console.log(query);
        $.ajax({
            url : "standInaccountName/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.accName').value = json.accountName
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });
//function to calculaate charge amounts
$(function(){
    $(".form-charges").keyup(function(){
    
        let newBalance = 0
        let charges = Number($(".chargeAmount").val())
        let olBalance = Number($(".chargeoldBalance").val())
        newBalance = olBalance - charges
        $(".newBalance").val(newBalance.toFixed(2))
        
       
    })
})

//manipulate the charges form with all member data from the members models
$(document).ready(function() {
    $('.chargeAcc').change(function(){
        var query = $(this).val();
        console.log(query);
        $.ajax({
            url : "charge_name/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('#accountName').value = json.accountName;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });
  
  
  
  

  