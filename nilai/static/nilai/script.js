$(document).ready(

	function(){
		showData()
		$('.tombol1').click(function(event){
			event.preventDefault();
			tambahData();
		});
	}

	function showData(){
		var dataRes = ""

		$.ajax({
			url: url,
			error: function(){
				alert("Something went wrong, try again.")
			},
			success: function(data){
				console.log(data);

				$('#nomor_semester').empty()
			}
		})
	}

	function tambahData(){
		$.ajax({
			url: url2,
			type: 'POST',
			data: $('form#form-matkul').serialize(),
			error: function(){
				alert("Something went wrong, try again.")
			},
			success: function(data){
				console.log(data);
				if(data.success == true){
					showData();
				} else if(data.success == false){
					alert("Failed")
				}
			},
		})
	}
);