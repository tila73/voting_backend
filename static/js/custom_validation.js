function removevalidation() {
    document.getElementById("title").innerHTML = ""; 
    document.getElementById("nauthor").innerHTML = ""; 
    document.getElementById("ndate").innerHTML = ""; 
    document.getElementById("nslug").innerHTML = ""; 
    document.getElementById("nimage").innerHTML = ""; 
    document.getElementById("ndesc").innerHTML = ""; 
}


function validateform(){  
var ttitle=document.myform.news_title.value;  
var nauthor=document.myform.news_author.value;  
var ndate=document.myform.news_date.value;  
var nslug=document.myform.slug.value;  
var nimage=document.myform.news_img.value;  
var ndesc=document.myform.news_description.value;  
  
if (ttitle==null || ttitle==""){  
  document.getElementById("title").innerHTML = "Title can't be blank"; 
//   document.getElementById('subbtn').disabled = true;
  return false;  
}
else if(nauthor==null || nauthor==""){  
document.getElementById("nauthor").innerText="required"
  return false;  
  } 

else if(ndate==null || ndate==""){  
document.getElementById("ndate").innerText="required "
  return false;  
  } 
else if(nslug==null || nslug==""){  
document.getElementById("nslug").innerText="required"
  return false;  
  } 
else if(nimage==null || nimage==""){  
document.getElementById("nimage").innerText="required"
  return false;  
  } 
else if(ndesc==null || ndesc==""){  
document.getElementById("ndesc").innerText="required"
  return false;  
  } 
return true;
}  



