function setOptionSelect(){
	var elements = document.querySelectorAll("[type=checkbox]");
	for (i = 0; i< elements.length;i++)
	{
		cookie = document.cookie;
		var z = elements[i].getAttribute("name");
		if (elements[i].checked==true){
			document.cookie = z+"="+"1";	
		}
		else{
			document.cookie = z + "=" + "0";	
		}
	}
	var x = document.querySelectorAll("[title='test']");   
}

function limitAmount(){
	alert("capture event");
}