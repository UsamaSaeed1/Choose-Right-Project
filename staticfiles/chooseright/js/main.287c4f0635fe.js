console.log("loaded")

// Navigation-bar hamburger menu qurries
$("#search-mobile").on( 'click', function(){
	$(".search-box-container").toggleClass('search-mobile-active');
	$(".header-wrapper").toggleClass('search-extended');
});

const menuBtn = document.querySelector('.nav-menu-dropdown-btn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
	if (!menuOpen) {
		menuBtn.classList.add('open');
		menuOpen = true;
	}
	else{
		menuBtn.classList.remove('open');
		menuOpen = false;
	}
	});

// Navigation-bar hamburger menu activation
$("#nav-menu-dropdown-btn-toggle").on( 'click', function(){
	$(".nav-menu-dropdown-btn_burger").toggleClass('active-index');
	$(".nav-menu-dropdown-overlay").toggleClass('active');
});


// User Profile menu activation
$("#user-profile-dropdown-btn").on( 'click', function(){
	$("#user-profile-menu-options").toggleClass('active-menu');
});

// Preventing searchbox pop-up
document.addEventListener('invalid', (function () {
  return function (e) {
    e.preventDefault();
    document.getElementById("search").focus();
  };
})(), true);


//Enabling sorting for data 
$(function(){
      // bind change event to select
      $('#sortby').on('change', function () {
          var url = $(this).val(); // get selected value
          if (url) { // require a URL
              window.location = url; // redirect
          }
          return false;
      });
    });

function getSearchQuery(url){
	document.getElementById("max-value").required = true;
	document.getElementById("mini-value").required = true;
	var max_value = document.getElementById("max-value").value;
	var min_value = document.getElementById("mini-value").value;
	if(min_value == "" & max_value =="" ){
		alert("Please Specify Your Budget");
	}
	else if (url){ // require a URL
		window.location = url + '&' + 'mini=' + min_value + '&' + 'max=' + max_value; // redirect
    }
}

function getInputValue(url){
	document.getElementById("max-value").required = true;
	document.getElementById("mini-value").required = true;
	var max_value = document.getElementById("max-value").value;
	var min_value = document.getElementById("mini-value").value;
	if(min_value == "" & max_value =="" ){
		alert("Please Specify Your Budget");
	}
	else if (url){ // require a URL
		window.location = url + '?' + 'mini=' + min_value + '&' + 'max=' + max_value; // redirect
    }
}

// Fuctions for specification template
function myDetailsFunction() {
	document.getElementById("detailstab").style.background = "linear-gradient(#E1DADA,#D3D3D3)";
	document.getElementById("product-details").style.display = "block";
	document.getElementById("product-reviews").style.display = "none";
	document.getElementById("product-specifications").style.display = "none";
}

function myReviewsFunction() {
	document.getElementById("product-details").style.display = "none";
	document.getElementById("product-reviews").style.display = "block";
	document.getElementById("product-specifications").style.display = "none";
}

function mySpecificationFunction() {
	document.getElementById("product-details").style.display = "none";	
	document.getElementById("product-reviews").style.display = "none";
	document.getElementById("product-specifications").style.display = "block";
}
