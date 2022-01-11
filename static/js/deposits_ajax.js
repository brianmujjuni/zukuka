
//ajax code to get all  input fields for the deposits form fro members model
$(document).ready(function() {
    $('.accountNumber').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "Maccounttype/",
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
    $('.accountNumber').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "Maccountcurrency/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.mcurrency').value = json.accountCurrency;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  $(document).ready(function() {
    $('.accountNumber').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "Maccountname/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.mName').value = json.accountName;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  $(document).ready(function() {
    $('.accountNumber').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "MaccountNinNUmber/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.mNinNumber').value = json.ninNumber;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });

  $(document).ready(function() {
    $('.accountNumber').change(function(){
        var query = $(this).val();
        //console.log(query);
        $.ajax({
            url : "MBalance/",
            type : "GET",
            dataType: "json",
            data : {
                client_response : query
                },
            success: function(json) {
                document.querySelector('.mBalance').value = json.balance;
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });


  $(document).ready(function() {
    $('.accountNumber').change(function(){
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
                document.querySelector('.mContact').value = json.phoneNo1
            },
            failure: function(json) {
                alert('Got an error dude');
            }
        });
    });
  });


  
  

